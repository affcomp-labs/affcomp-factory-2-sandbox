import unittest

from src.health import health_payload, render_health


class HealthPayloadTests(unittest.TestCase):
    def test_health_payload_is_deterministic(self) -> None:
        self.assertEqual(
            health_payload(),
            {"status": "ok", "factory": "affcomp-2.0"},
        )


class RenderHealthTests(unittest.TestCase):
    def test_render_health_is_deterministic(self) -> None:
        self.assertEqual(render_health(), "status=ok;factory=affcomp-2.0")


if __name__ == "__main__":
    unittest.main()
