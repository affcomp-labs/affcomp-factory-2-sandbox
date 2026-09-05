import unittest

from src.health import health_payload


class HealthPayloadTests(unittest.TestCase):
    def test_health_payload_is_deterministic(self) -> None:
        self.assertEqual(
            health_payload(),
            {"status": "ok", "factory": "affcomp-2.0"},
        )


if __name__ == "__main__":
    unittest.main()
