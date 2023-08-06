# Imgbb Python Client Library

## Features

- Easy image uploading to Imgbb's servers.
- Supports JPG, PNG, GIF, base64, and URL image sources.
- Automatic retry with configurable retry intervals for robustness.
- Clear and intuitive API for quick integration.

## Installation

its recommended to use a virtual environment to install the package

```bash
pip install imgbb-client
```

## Usage

```python
from imgbb_client import ImgbbClient

client = ImgbbClient("your-api-key")

# Upload image from URL
result = client.upload("https://example.com/image.jpg", name="My Image", expiration=3600)

```

## Changelog

For a list of changes and release notes, see the [CHANGELOG](CHANGELOG.md) file.

## License

For license information, please see [LICENSE](AfricanUnboundLicense.md)

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

Built with ❤️ by [Adivhaho Mavhungu](https://twitter.com/adivhaho_dev)
