"""Deterministic health response used by the AffComp 2.0 thin slice."""

from __future__ import annotations


def health_payload() -> dict[str, str]:
    """Return a stable, side-effect-free health payload."""
    return {"status": "ok", "factory": "affcomp-2.0"}


def render_health() -> str:
    """Return a deterministic text rendering of the health payload."""
    payload = health_payload()
    return f"status={payload['status']};factory={payload['factory']}"
