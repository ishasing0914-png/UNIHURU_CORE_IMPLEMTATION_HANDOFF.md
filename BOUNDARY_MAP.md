# UniGuru Boundary Map (Template)

This file maps repository files to UniGuru boundaries. Maintain this document and keep it up-to-date. CI will fail if new top-level files are missing a `Boundary:` tag comment.

## Format
| File/Path | Boundary Role | Owner | Why | Must-never contain |
|---|---:|---|---|---|
| `src/uniguru/core.py` | **UniGuru Core** | `@intelligence` | deterministic orchestration, pure transforms | network calls, tool execution, agent logic |
| `src/adapters/` | Adapter | @adapters | RESERVED — not present in this phase | any execution or policy logic |
| `src/enforcement/` | Enforcement Engine | `@enforcement` | authoritative allow/rewrite/block decisions | execution logic, direct runtime tooling |

## Tagging rule
Every source file must start with a single-line comment with one of these values:

```
# Boundary: UniGuru-Core
# Boundary: Adapter
# Boundary: Enforcement
# Boundary: Task-System
# Boundary: Product-Shell
```

CI will run `scripts/check_boundary_tags.py` to enforce this.

## Process
- Add entries for each file you add.
- Assign CODEOWNERS for sensitive boundaries.
- For any exception, record the reason and approval in this file.
