# Thin-slice issue

**Title:** Add a deterministic text rendering for the health payload

**Labels:** `af2:r0`, then `af2:ready`

## Objective

Add `render_health()` to `src/health.py`. It must return exactly `status=ok;factory=affcomp-2.0`. Add a focused unit test and update the README example. Keep the change inside `src/**`, `tests/**`, and `README.md`.

## Acceptance

- `python -m unittest discover -s tests -v` passes.
- Existing `health_payload()` behavior is unchanged.
- No dependencies or factory/control files change.
- The PR is created by the 2.0 App, required `test` CI runs automatically, and native squash auto-merge lands it without an owner state-transition click.
- The issue/PR record includes base, branch, head, and merged SHAs, attempts, elapsed time, and model cost.
