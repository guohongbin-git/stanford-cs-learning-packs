#!/usr/bin/env python3
"""Review ONE course pack directory: same checks as verify_pack.py plus
relation-DAG analysis (cycles, dangling targets, self-edges).

Usage:  python3 tools/verify_course.py docs/courses/cs336
Exit code 1 if any check fails.
"""
from __future__ import annotations
import json, os, re, sys, hashlib
from collections import Counter

REQ_CONCEPT_FIELDS = ["id", "type", "status", "definition", "why",
                      "failure_conditions", "example", "relations", "weeks", "source_weeks"]


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


def check(root: str):
    fails, notes = [], []
    if not os.path.isdir(root):
        return [f"{root}: not a directory"], notes

    # manifest bytes/sha256
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
        notes.append(f"manifest {len(mf['files']) - len(bad)}/{len(mf['files'])} ok")
        if bad:
            fails.append(f"manifest mismatches: {bad[:5]}")
    else:
        fails.append("package_manifest.json missing")

    concepts = json.load(open(os.path.join(root, "concepts.json")))
    ir = json.load(open(os.path.join(root, "course_ir.json")))
    items = list(concepts.values()) if isinstance(concepts, dict) else concepts

    # HTML self-containment + embedded JSON equality
    htmls = [f for f in os.listdir(root) if f.endswith(".html") and f != "index.html"]
    if htmls:
        html = open(os.path.join(root, htmls[0]), encoding="utf-8", errors="replace").read()
        ext = re.findall(r'(?:src|href)="https?://', html)
        notes.append(f"html {len(html.encode())}B, external refs={len(ext)}")
        if ext:
            fails.append(f"HTML {len(ext)} external references")
        m = re.search(r"<script[^>]*type=['\"]application/json['\"][^>]*>([\s\S]*?)</script>", html)
        if not m:
            fails.append("HTML no embedded JSON payload")
        else:
            emb = json.loads(m.group(1))
            if not (emb.get("concepts") == concepts and emb.get("course_ir") == ir):
                fails.append("embedded JSON differs from standalone JSON")

    # concept field completeness
    for c in items:
        miss = [k for k in REQ_CONCEPT_FIELDS if c.get(k) in (None, "")]
        if miss:
            fails.append(f"{c.get('id')}: missing {miss}")

    # relation targets resolve
    names = {c.get("id") for c in items}
    edges, selfedges, dangling = [], [], []
    for c in items:
        for r in (c.get("relations") or []):
            t = r.get("target")
            if t == c.get("id"):
                selfedges.append(c.get("id"))
            elif t not in names:
                dangling.append((c.get("id"), t))
            else:
                edges.append((c.get("id"), t, r.get("kind")))

    # cycle detection (only over intra-course edges)
    adj = {c.get("id"): [] for c in items}
    for a, b, _ in edges:
        adj[a].append(b)
    color = {c: 0 for c in adj}  # 0 white 1 gray 2 black
    cyc = []

    def dfs(u, stack):
        color[u] = 1
        for v in adj[u]:
            if color[v] == 1:
                cyc.append(stack[stack.index(v):] + [v])
            elif color[v] == 0:
                dfs(v, stack + [v])
        color[u] = 2

    for c in adj:
        if color[c] == 0:
            dfs(c, [c])

    notes.append(f"relations {len(edges)} edges, {len(selfedges)} self, {len(dangling)} dangling")
    for a, b in dangling:
        fails.append(f"dangling relation {a} -> {b}")
    if selfedges:
        notes.append(f"self-edges: {selfedges[:5]}")
    if cyc:
        fails.append(f"CYCLE: {' -> '.join(cyc[0])}")

    ok = not fails
    print(f"[{'PASS' if ok else 'FAIL'}] {os.path.basename(root)}  " + " | ".join(notes))
    for f in fails:
        print("    ! " + f)
    return fails


def main(argv):
    roots = argv[1:] or [os.path.join("docs", "courses", d)
                         for d in sorted(os.listdir("docs/courses"))]
    total = 0
    for r in roots:
        total += len(check(r))
    print(f"\n{'ALL PASS' if total == 0 else str(total) + ' FAILED packs'}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
