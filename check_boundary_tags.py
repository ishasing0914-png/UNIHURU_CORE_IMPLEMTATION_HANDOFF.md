#!/usr/bin/env python3
"""CI check: ensure Python files have a Boundary tag in the first 5 lines."""
import sys
from pathlib import Path

exclude_dirs = {".git", "venv", "env", "__pycache__", ".pytest_cache"}
failed = []

for p in Path('.').rglob('*.py'):
    if any(part in exclude_dirs for part in p.parts):
        continue
    # Allow scripts in tests/ and scripts/ to be boundary-tagged too, but still enforce
    with p.open('r', encoding='utf-8') as fh:
        head = ''.join([next(fh) for _ in range(5)]) if p.stat().st_size > 0 else ''
    if '# Boundary:' not in head:
        failed.append(str(p))

if failed:
    print('Files missing Boundary tag:')
    for f in failed:
        print(' -', f)
    sys.exit(1)
print('Boundary tag check passed.')
