#!/usr/bin/env python3
"""CI search for forbidden imports and agentic phrases."""
import re
import sys
from pathlib import Path

FORBIDDEN = [
    r"\bchild_process\b",
    r"\bsubprocess\b",
    r"\bos\.system\b",
    r"\bspawn\b",
    r"\bexec\b",
    r"\blangchain\b",
    r"\bautogen\b",
    r"act as an agent",
    r"act as an execution engine",
    r"run this"
]

exclude_dirs = {".git", "venv", "env", "__pycache__", ".pytest_cache"}
pattern = re.compile('|'.join(f'({p})' for p in FORBIDDEN), re.I)

def scan():
    hits = []
    for p in Path('.').rglob('*'):
        if p.is_file() and p.suffix in {'.py', '.md', '.txt'} and not any(part in exclude_dirs for part in p.parts):
            try:
                text = p.read_text(encoding='utf-8')
            except Exception:
                continue
            for m in pattern.finditer(text):
                hits.append((str(p), m.group(0).strip()))
    return hits

if __name__ == '__main__':
    hits = scan()
    if hits:
        print('Forbidden patterns found:')
        for f, match in hits:
            print(f' - {f}: "{match}"')
        sys.exit(1)
    print('CI grep check passed.')
