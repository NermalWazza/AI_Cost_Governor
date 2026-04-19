# NEXT_STEPS

## URGENT — Security — requires human action

### 1. Rotate BOTH OpenAI API keys

TruffleHog found two live, verified API keys in local files. Neither is committed to git,
but rotation is recommended as a precaution.

| Location | Status | Action |
|----------|--------|--------|
| `.env` — Key A | Untracked, gitignored — local only | Rotate as precaution |
| `config\.env.local` — Key B | Untracked, gitignored — local only | Rotate as precaution |

Rotate at: https://platform.openai.com/api-keys

### 2. Clean orphaned git blob

An older key (Key B) exists as an orphaned git object in `.git\objects\bd\b272...`
This blob was staged but never committed (pre-commit likely blocked it).
It cannot be pushed, but to clean it locally:

```powershell
git gc --prune=now
```

### 3. Untrack cost_log.csv from git

`cost_log.csv` is a runtime file currently tracked by git despite being in `.gitignore`.
Once tracked, `.gitignore` has no effect on an already-tracked file.

Fix (requires a commit):
```powershell
git rm --cached cost_log.csv
git commit -m "Remove runtime file from tracking"
```

---

## Recommended — after rotation

- [ ] Re-run: `.venv\Scripts\pre-commit.exe run --all-files`
  TruffleHog will still flag `.env` and `config\.env.local` (expected — local live keys)
  These files are gitignored and cannot be committed. The hook is working correctly.

- [ ] Confirm pre-commit hooks re-installed after clone:
  `.venv\Scripts\pre-commit.exe install`

- [ ] Install TruffleHog system-wide if scanning other repos:
  `winget install trufflesecurity.trufflehog`

- [ ] Pin Python dependencies:
  `pip freeze > requirements-lock.txt` for reproducible installs.

- [ ] Add `.env.example` at repo root:
  Documents required env vars without real values. Helps onboarding.
