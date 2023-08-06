import unittest
import coverage

from decouple import config

from imgbb.client import ImgbbClient


cov = coverage.Coverage()
cov.start()


class TestImgbbClient(unittest.TestCase):
    """Imgbb client test case."""

    def setUp(self) -> None:
        """Set up test case."""
        self.client = ImgbbClient(config("IMGBB_API_KEY"))
        self.image_url = (
            "https://res.cloudinary.com/demo/image/upload/v1312461204/sample.jpg"
        )
        self.image_file = "static/img/image.png"

    def test_url_upload(self) -> None:
        response = self.client.upload(self.image_url, name="test", expiration=3600)
        self.assertEqual("data" in response, True)

    def test_file_upload(self) -> None:
        response = self.client.upload(self.image_file, name="test1", expiration=3600)
        self.assertEqual("data" in response, True)


cov.stop()
cov.save()

if __name__ == "__main__":
    cov.report()
    cov.html_report()
    unittest.main()
