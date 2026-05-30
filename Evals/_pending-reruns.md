# Pending eval re-runs

Each row was registered when a mapped source file changed. A row is cleared only when a fresh eval run lands in `Evals/<suite>/results/` with date ≥ the source file's last edit date.

`/peer-review` and `/go-nogo` block any artifact citing a `pending`-status suite.

## Schema

- **Suite**: the affected suite
- **Source file changed**: the file that triggered registration
- **Source commit SHA**: `git rev-parse HEAD` at registration time
- **Registered date**: YYYY-MM-DD
- **Status**: `pending` | `cleared`
- **Cleared by run**: path to the result file that cleared it (filled when status flips to `cleared`)

## Ledger

| Suite | Source file changed | Source commit SHA | Registered date | Status | Cleared by run |
|---|---|---|---|---|---|

(append-only; no row deletion; status `pending` → `cleared` only)
