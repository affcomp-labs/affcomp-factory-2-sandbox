# AffComp AI Factory 2.0 Sandbox

> **AFFCOMP 2.0 EXPERIMENTAL — NOT CONNECTED TO PRIOR SYSTEMS**

A public, disposable, secret-free repository for proving a bounded Claude Code GitHub Action issue-to-PR-to-CI-to-squash-auto-merge loop.

The sample application exposes a deterministic health payload through `src.health.health_payload()`, and a matching text rendering through `src.health.render_health()` (`status=ok;factory=affcomp-2.0`). Run the tests with:

```bash
python -m unittest discover -s tests -v
```

Operational policy is in [`FACTORY.md`](FACTORY.md). Nothing here is production or customer-facing.
