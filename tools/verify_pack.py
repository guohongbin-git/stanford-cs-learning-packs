#!/usr/bin/env python3
"""Mechanical verifier for a Stanford CS learning pack.

Usage:  python3 tools/verify_pack.py docs/courses/cs336

Checks
  1. package_manifest.json — declared bytes + sha256 match the files on disk
  2. interactive HTML — self-contained (no external src/href) and its embedded
     `<script type="application/json">` payload equals the standalone JSON files
  3. concepts.json — required fields, id == dict key, non-empty weeks,
     relation targets resolve, no duplicate ids
  4. week linkage — concept.weeks matches the week lists in course_ir.json
     (theme lists for seminar packs)
  5. template detector — normalises concept names and digits, then counts
     records sharing one sentence skeleton (>= 3 hits means filler)
Exit code 1 if any check fails.
"""
from __future__ import annotations
import json, os, re, sys, hashlib
from collections import Counter

REQ_CONCEPT_FIELDS = ["id", "type", "status", "definition", "why",
                      "failure_conditions", "example", "relations", "weeks", "source_weeks"]
TEXT_FIELDS_CONCEPT = ["definition", "why", "failure_conditions", "example"]
TEXT_FIELDS_WEEK = ["question", "why", "objectives", "pitfalls"]


def skeleton(value, cid):
    parts = value if isinstance(value, list) else [value]
    out = []
    for s in parts:
        t = str(s).replace(cid, "\u00a7")
        t = re.sub(r"CS\s?\d+[A-Z]*", "CSx", t)
        t = re.sub(r"\d+", "#", t)
        t = re.sub(r"(课程|系统|模型|数据|算法|方法|技术|理解|掌握|知道|能够)", "#", t)
        out.append(re.sub(r"[\s，。、；：,.\u3001]+", "", t))
    return "|".join(out)


def template_hits(items, fields):
    hits = {}
    for f in fields:
        c = Counter(skeleton(x.get(f, ""), x.get("id", "")) for x in items)
        hits[f] = sum(n for k, n in c.items() if n >= 3 and len(k) > 4)
    return hits


def main(root: str) -> int:
    fails, notes = [], []

    # 1. manifest
    mfp = os.path.join(root, "package_manifest.json")
    if os.path.exists(mfp):
        mf = json.load(open(mfp))
        bad = []
        for f in mf.get("files", []):
            p = os.path.join(root, f["path"])
            if not os.path.exists(p):
                bad.append((f["path"], "missing")); continue
            b = open(p, "rb").read()
            if len(b) != f.get("bytes") or hashlib.sha256(b).hexdigest() != f.get("sha256"):
                bad.append((f["path"], "bytes/hash mismatch"))
        print(f"[1] manifest: {len(mf.get('files', [])) - len(bad)}/{len(mf.get('files', []))} verified")
        if bad:
            fails.append(f"manifest mismatches: {bad[:5]}")
    else:
        fails.append("package_manifest.json missing")

    concepts = json.load(open(os.path.join(root, "concepts.json")))
    ir = json.load(open(os.path.join(root, "course_ir.json")))
    items = list(concepts.values()) if isinstance(concepts, dict) else concepts

    # 2. HTML self-containment + embedded JSON equality
    htmls = [f for f in os.listdir(root) if f.endswith(".html") and f != "index.html"]
    if htmls:
        html = open(os.path.join(root, htmls[0]), encoding="utf-8", errors="replace").read()
        ext = re.findall(r'(?:src|href)="https?://', html)
        print(f"[2] html: {len(html.encode())} bytes, external refs: {len(ext)}")
        if ext:
            fails.append(f"HTML has {len(ext)} external references (must be self-contained)")
        m = re.search(r"<script[^>]*type=['\"]application/json['\"][^>]*>([\s\S]*?)</script>", html)
        if not m:
            fails.append("HTML has no embedded application/json payload")
        else:
            emb = json.loads(m.group(1))
            same_c = emb.get("concepts") == concepts
            same_i = emb.get("course_ir") == ir
            print(f"    embedded == standalone: concepts={same_c} course_ir={same_i}")
            if not (same_c and same_i):
                fails.append("embedded JSON differs from standalone JSON files")

    # 3. concept schema
    viol = [x.get("id") for x in items if any(k not in x for k in REQ_CONCEPT_FIELDS)]
    ids = [x["id"] for x in items]
    dupes = [i for i, n in Counter(ids).items() if n > 1]
    key_drift = [k for k, v in concepts.items() if k != v.get("id")] if isinstance(concepts, dict) else []
    idset = set(ids)
    dangling = sorted({r.get("target") for x in items for r in x.get("relations", [])
                       if r.get("target") not in idset})
    empty_weeks = [x["id"] for x in items if not x.get("weeks")]
    print(f"[3] concepts: {len(items)} | schema violations {len(viol)} | dup ids {len(dupes)} | "
          f"key drift {len(key_drift)} | dangling relations {len(dangling)} | empty weeks {len(empty_weeks)}")
    if viol or dupes or key_drift or dangling or empty_weeks:
        fails.append(f"concept schema/linkage problems: viol={viol[:3]} dupes={dupes[:3]} "
                     f"drift={key_drift[:3]} dangling={dangling[:5]} empty_weeks={empty_weeks[:3]}")

    # 4. week/theme linkage
    groups = list(ir.get("weeks", [])) + list(ir.get("themes", []))
    n2g = {}
    for g in groups:
        gid = g.get("id")
        for n in g.get("concepts", []) or []:
            n2g.setdefault(n, set()).add(gid)
    norm = lambda v: (str(v).lower() if str(v).lower().startswith("w") else f"w{re.sub(r'[^0-9]', '', str(v)) or ''}")
    mism = [x["id"] for x in items if x["id"] in n2g and {norm(v) for v in x["weeks"]} != {norm(v) for v in n2g[x["id"]]}]
    orphans = [x["id"] for x in items if x["id"] not in n2g]
    print(f"[4] linkage: mismatched {len(mism)} | unlinked {len(orphans)}")
    if mism or orphans:
        fails.append(f"week linkage: mismatch={mism[:5]} orphan={orphans[:5]}")

    # 5. template detector
    ch = template_hits(items, TEXT_FIELDS_CONCEPT)
    wh = template_hits(ir.get("weeks", []), TEXT_FIELDS_WEEK)
    print(f"[5] template skeletons: concept {ch} | week {wh}")
    total = sum(ch.values()) + sum(wh.values())
    if total:
        fails.append(f"template filler detected: {total} records")



    # 6. quiz cross-week dedup (issue #2/#3/#5)
    weeks = ir.get("weeks", [])
    qtexts = []
    for w in weeks:
        q = w.get("quiz") or {}
        qtexts.append(json.dumps(q.get("q", "") + "|" + "|".join(q.get("choices", [])), ensure_ascii=False))
    dup_q = len(qtexts) - len(set(qtexts))
    print(f"[6] quiz cross-week duplicates: {dup_q} of {len(weeks)} weeks")
    if dup_q:
        fails.append(f"{dup_q} weeks share an identical quiz (placeholder repetition)")

    # 7. failure_conditions must be list[str] (issue #4)
    bad_fc = [x.get("id") for x in items if not isinstance(x.get("failure_conditions"), list)]
    print(f"[7] failure_conditions not list[str]: {len(bad_fc)}")
    if bad_fc:
        fails.append(f"failure_conditions must be list[str] for: {bad_fc[:5]}")

    print()
    if fails:
        print("FAIL")
        for f in fails:
            print(" -", f)
        return 1
    print("PASS — structure, integrity, linkage and template checks are clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))