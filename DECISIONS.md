# DECISIONS.md

## Decision — Hard cost cap via DAILY_LIMIT

`DAILY_LIMIT` in `src/main.py` is a hard numeric cap checked before every API call.
Rationale: prevent runaway costs in AI experiments; the cap is the core safety invariant.

## Decision — Secret hygiene via detect-secrets + TruffleHog

Pre-commit hooks enforce no secrets in commits. API key loaded via `os.getenv("OPENAI_API_KEY")` only — never hardcoded.
Rationale: structural prevention of leakage; accidental commit is blocked before it happens.

## Decision — requirements.txt over pyproject.toml (current)

Minimal dependency declaration at project start. Not yet migrated.
Rationale: speed of initial setup. Migration to `pyproject.toml` is a future option.
