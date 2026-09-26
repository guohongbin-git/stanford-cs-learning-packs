#!/usr/bin/env python3
"""Regenerate package_manifest.json for one course pack.

Usage:  python3 tools/gen_manifest.py docs/courses/cs336

Walks the pack directory, records every file (relative path, byte length,
sha256) and writes package_manifest.json. Excludes package_manifest.json
itself. Sorted by path for determinism. Preserves existing `package`/`note`
fields and matches the existing 2-space, no-trailing-newline formatting so
a regenerated manifest round-trips byte-for-byte.
"""
from __future__ import annotations
import hashlib, json, os, sys


def build(root: str) -> dict:
    out = os.path.join(root, "package_manifest.json")
    existing = {}
    if os.path.exists(out):
        try:
            existing = json.load(open(out, encoding="utf-8"))
        except Exception:
            existing = {}
    pkg = existing.get("package") or os.path.basename(os.path.normpath(root))
    note = existing.get("note")
    files = []
    for dirpath, _dirs, fnames in os.walk(root):
        for fn in fnames:
            p = os.path.join(dirpath, fn)
            if os.path.basename(p) == "package_manifest.json":
                continue
            rel = os.path.relpath(p, root).replace(os.sep, "/")
            b = open(p, "rb").read()
            files.append({
                "path": rel,
                "bytes": len(b),
                "sha256": hashlib.sha256(b).hexdigest(),
            })
    files.sort(key=lambda f: f["path"])
    m = {"package": pkg, "files": files}
    if note:
        m["note"] = note
    return m


def main(argv):
    roots = argv[1:] or sorted(
        os.path.join("docs", "courses", d) for d in os.listdir("docs/courses"))
    for root in roots:
        m = build(root)
        out = os.path.join(root, "package_manifest.json")
        tmp = out + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(m, fh, ensure_ascii=False, indent=2)
        os.replace(tmp, out)
        print(f"[gen] {os.path.basename(root)}: {len(m['files'])} files -> {os.path.basename(out)}")


if __name__ == "__main__":
    main(sys.argv)
