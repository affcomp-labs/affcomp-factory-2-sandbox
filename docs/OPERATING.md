# AF2 Operating Card — v2 (2026-09-05)

**Purpose:** one page that says what to do on every surface, so nothing drifts.
**Rule zero:** GitHub is the only place state lives. If a decision or status exists anywhere else, it doesn't exist. The 2.0 record is `affcomp-labs/affcomp-2` `docs/`.

## The five surfaces

| Surface | Role | You open it |
|---|---|---|
| **GitHub** (phone app or web) | Intake, status, escalation. The only daily surface. | Daily |
| **GitHub notifications** (email / phone app; repo watch = *participating*) | Sentinel: `af2:blocked` applied, R2 PR opened, PR merged. | Daily, 5 min |
| **Claude Code, local** (Windows, clone of this repo) | R2 work only, you at the keyboard. Never autonomous. | Weekly at most |
| **Codex** (GitHub code review, ChatGPT Pro) | Independent reviewer. You read its PR comments; you never open Codex. | Never directly |
| **Claude Project "AffComp 2.0"** | Guide. Reads the 2.0 record; drafts issues, files, and decisions; never holds state. | As needed |

Routine R0/R1 work runs inside GitHub Actions on your Claude Max subscription. You never open Claude Code for it.

## The label state machine (source of truth)

```
ISSUE:  af2:r0 | af2:r1  (risk, apply FIRST)
        → af2:ready      (apply LAST — this is the trigger)
        → af2:running
        → closed by PR merge ("Closes #N")

PR:     af2:auto  af2:attempt-1 → -2 → -3
        af2:repair  (transient, bot-applied)
        af2:blocked (needs you)
```

## If you are on… do…

**Phone, morning (5 min).** Read GitHub notifications: merged / blocked.
If anything is `af2:blocked`: open GitHub, read the last bot comment, then either rewrite the issue and re-label, or close it. Never debug inside the PR. Five-minute cap.

**GitHub, intake (2–3× a week, 15–20 min).**
1. New issue from the template: objective, acceptance test, allowed paths.
2. Risk label first, `af2:ready` last.
3. One at a time: wait until the run starts before labeling the next issue.
4. Keep 5–10 drafted issues in the backlog *without* `af2:ready`. Zero = idle factory; more than ten = stale backlog.

**GitHub, an R2 PR is waiting.** Read Codex's review and CI. Merge, or request changes. That one click is yours by design.

**Claude Code, local (R2 only).** Open Claude Code in your clone of this repo. Confirm `gh auth status` shows your account and `git remote -v` shows only this repo. Branch `af2/r2-<slug>`. Push, open the PR, let Codex review, merge it yourself. Never run this unattended.

**Claude Project "AffComp 2.0".** Use for: drafting issues from a rough list, blocked-issue comments, tier calls, changes to `FACTORY.md` or this card (R2), post-incident analysis. Every session ends with a pasted issue, a file to commit, or a PR. If it produced none, it produced nothing.

**Codex.** Never comment `@codex fix it` on an `af2:` PR — that starts a second writer on the branch and collides with the repair loop.

## Alerts

Immediate (two only): `af2:blocked` applied; R2 PR opened.
Everything else is read in the morning pass.
Set the repo's GitHub watch to "participating" so those two reach you and nothing else does.

## Weekly (30 min)

Scorecard: merges, reverts, manual recoveries, cost/turns from PR bodies, zero-click ratio, Max-plan usage vs quota.
Exit condition (D-004): one clean merge, one revert, one observed self-repair — or 3–5 clean merges. Then the factory moves to `affcomp-labs/affcomp-2`.
Limits are lowered on evidence, never raised silently.

## Kill order

1. Disable `af2-factory.yml` 2. Suspend the App installation 3. Revoke the OAuth token (overwrite `AF2_CLAUDE_CODE_OAUTH_TOKEN` with a dead value; regenerate locally) 4. Archive the repo.
Revert a bad merge: run the `af2-revert` workflow with the squash SHA (one dispatch → one auto-merging PR).

## Drift rules

- No state outside GitHub.
- No new surface, bot, or tool without an R2 PR that edits this card.
- If a routine step needs more than one click from you, that is a factory bug to file, not a task to do.
- The sandbox repo is disposable. Prefer teardown over rescue.
