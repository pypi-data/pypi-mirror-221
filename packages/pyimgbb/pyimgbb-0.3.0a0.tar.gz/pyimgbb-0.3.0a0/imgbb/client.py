import base64
import io
import time

import requests
from PIL import Image


class ImgbbClient(object):
    """Imgbb client."""

    IMGBB_API_URL: str = "https://api.imgbb.com/1/upload"
    _RETRY_TIMES: int = 3
    _RETRY_BACKOFF: list = [5, 10, 20]

    def __init__(self, imgbb_api_key: str) -> None:
        self.imgbb_api_key = imgbb_api_key

    def _get_image_data(self, image: str) -> tuple:
        """
        Get image data from file, url, or base64 string.

        Parameters:
        -----------
        image : str
            The image file path, url, or base64 string.

        Returns:
        --------
        tuple
            A tuple containing the image data and the source type.
            The image data is represented as bytes.
            The source type can be 'file', 'url', or 'base64'.

        Raises:
        -------
        ValueError
            If there was an error reading the image.
        """
        try:
            if image.startswith("data:image"):
                _, image_data = image.split(",", 1)
                image_data = base64.b64decode(image_data)
                return image_data, "base64"
            else:
                image = Image.open(image)
                with io.BytesIO() as output:
                    image.save(output, format=image.format)
                    return output.getvalue(), "file"
        except Exception as error:
            raise ValueError(f"Failed to read image: {error}") from error

    def _is_valid_url(self, url: str) -> bool:
        """
        Check if the URL is valid.

        Parameters:
        -----------
        url : str
            The URL to check.

        Returns:
        --------
        bool
            True if the URL is valid, False otherwise.
        """
        try:
            response = requests.head(url)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def upload(
        self,
        image: str,
        name: str = None,
        expiration: int = None,
    ) -> dict:
        """
        Upload image to imgbb.

        Note:
        -----
        The image can be a file path, url, or base64 string.

        Parameters:
        -----------
        image : str
            The image file path, url, or base64 string.
        name : str, optional
            The name to assign to the uploaded image.
        expiration : int, optional
            The time in seconds for the uploaded image to expire.

        Returns:
        --------
        dict
            A dictionary containing the response from the Imgbb API.

        Raises:
        -------
        requests.exceptions.RequestException
            If there was an error making the HTTP request.
        """
        if self._is_valid_url(image):
            image_data, source_type = image, "url"
        else:
            image_data, source_type = self._get_image_data(image)

        payload = self._create_payload(image_data, source_type, name, expiration)

        for _ in range(self._RETRY_TIMES):
            try:
                response = self._make_request(payload)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException:
                time.sleep(self._RETRY_BACKOFF[_])

        raise requests.exceptions.RequestException(
            f"Could not connect after {self._RETRY_TIMES} retries."
        )

    def _create_payload(self, image_data, source_type, name: int, expiration: int):
        return {
            "key": self.imgbb_api_key,
            "image": base64.b64encode(image_data)
            if source_type in ["base64", "file"]
            else image_data,
            "name": name,
            "expiration": expiration,
        }

    def _make_request(self, payload: dict):
        return requests.post(self.IMGBB_API_URL, data=payload)
