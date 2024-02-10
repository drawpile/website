from django.test import TestCase


class NormalizationTest(TestCase):
    def test_email_normalization(self):
        from .normalization import normalize_email

        SAMPLES = (
            ("", ""),
            ("ARGH", "argh"),
            ("test@example.com", "test@example.com"),
            (" TÄßt@example.com\n", "tässt@example.com"),
            ("exam.ple@example.com", "exam.ple@example.com"),
            ("example@gmail.com", "example@gmail.com"),
            ("exam.ple@gmail.com", "example@gmail.com"),
            ("e.xa.mp....le@gmail.com", "example@gmail.com"),
            ("example+dp@protonmail.ch", "example@protonmail.ch"),
            ("example+something+else@gmail.com", "example@gmail.com"),
            ("example+@pm.me", "example@pm.me"),
            ("example+++@proton.me", "example@proton.me"),
            ("+leading@googlemail.com", "+leading@googlemail.com"),
            ("not+leading@googlemail.com", "not@googlemail.com"),
            ("exa.mple+test@protonmail.ch", "example@protonmail.ch"),
        )

        for given, expected in SAMPLES:
            self.assertEqual(
                normalize_email(given), expected, msg=f"Normalizing {repr(given)}"
            )
