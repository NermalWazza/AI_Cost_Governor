# AI_Cost_Governor

## Overview

Minimal Python control layer for interacting with AI models with explicit cost tracking and enforced secret hygiene.

Built to demonstrate:

* cost-aware AI usage
* deterministic execution
* practical DevSecOps guardrails

---

## Key Capabilities

* **Per-call cost visibility**
  Surfaces tokens, cost, and running totals

* **Secret-safe by default**
  `.env.local` isolation + commit blocking via `detect-secrets`

* **Pre-commit enforcement**
  Prevents accidental leakage of API keys and sensitive data

* **Structured runtime outputs**
  Logs cost data for inspection and extension

---

## Structure

```text
src/        # application logic
config/     # local secrets (.env.local, not committed)
data/       # runtime logs
audit/      # local scan outputs (ignored)
docs/       # documentation
```

---

## Security Model

* Secrets never enter version control
* Audit artefacts are quarantined
* Pre-commit scanning blocks unsafe commits

This repo is designed to make accidental leakage **structurally difficult**, not just discouraged.

---

## Run

```powershell
python src/main.py "your prompt"
```

---

## Intent

A minimal, extensible foundation for:

* AI cost governance
* safe API usage patterns
* lightweight DevSecOps integration

---

## Notes

* Requires local `.env.local` with API key
* Rotate any exposed keys immediately
* Designed for clarity over completeness
