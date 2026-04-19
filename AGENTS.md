# AGENTS.md

Guidance for AI coding agents (Claude, Codex, etc.) working in this repo.

## What this repo is

A minimal Python tool that calls OpenAI with a hard daily cost cap.
The cost guard (`DAILY_LIMIT` in `src/main.py`) is the core safety invariant —
do not weaken or bypass it.

## Key files

| File | Purpose |
|------|---------|
| `src/main.py` | All application logic — cost tracking, API call, output |
| `requirements.txt` | Runtime deps (openai, python-dotenv) |
| `.env` | Local secrets — never read values aloud, never commit |
| `cost_log.csv` | Runtime CSV log written by the app — do not modify manually |
| `.pre-commit-config.yaml` | Pre-commit hooks — detect-secrets, pre-commit-hooks, TruffleHog |
| `.secrets.baseline` | detect-secrets baseline — regenerate with `.venv\Scripts\detect-secrets.exe scan` after adding allowlisted items |

## Invariants — do not break these

- `DAILY_LIMIT` must remain a hard numeric cap checked before every API call.
- The API key must only be loaded via `os.getenv("OPENAI_API_KEY")` — never hardcoded.
- `cost_log.csv` must never be committed (it is runtime state).

## Running the app

```powershell
.venv\Scripts\Activate.ps1
python src/main.py "your prompt here"
python src/main.py "your prompt here" output\result.txt
```

## Running pre-commit

```powershell
.venv\Scripts\pre-commit.exe install
.venv\Scripts\pre-commit.exe run --all-files
```

## Secrets handling

- Never print, log, or include the value of `OPENAI_API_KEY` in any output.
- If detect-secrets flags a false positive, add an inline allowlist comment, then regenerate the baseline.
- If a secret is accidentally committed, stop immediately and report — do not try to scrub it silently.
