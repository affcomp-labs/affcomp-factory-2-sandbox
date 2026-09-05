"""Deterministic health response used by the AffComp 2.0 thin slice."""

from __future__ import annotations


def health_payload() -> dict[str, str]:
    """Return a stable, side-effect-free health payload."""
    return {"status": "ok", "factory": "affcomp-2.0"}
