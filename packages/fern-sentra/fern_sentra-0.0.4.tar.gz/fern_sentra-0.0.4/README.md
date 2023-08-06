# Sentra Python Library

[![pypi](https://img.shields.io/pypi/v/fern-sentra.svg)](https://pypi.python.org/pypi/fern-sentra)
[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)

## Installation

Add this dependency to your project's build file:

```bash
pip install fern-sentra
# or
poetry add fern-sentra
```

## Usage

```python
from sentra.client import Sentra

sentra_client = Sentra(
  environment="https://sentra.io/api",
)

filter = sentra_client.alerts.get_filter(
  name="filter-name",
);

print(filter)
```

## Async Client

```python
from sentra.client import AsyncSentra

import asyncio

sentra_client = AsyncSentra(
  environment="https://sentra.io/api",
)

async def get_filter() -> None:
    filter = sentra_client.alerts.get_filter(
      name="filter-name",
    );
    print(filter)

asyncio.run(get_filter())
```

## Timeouts
By default, the client is configured to have a timeout of 60 seconds. You can customize this value at client instantiation. 

```python
from sentra.client import Sentra

client = Sentra(environment="https://sentra.io/api", timeout=15)
```

## Handling Exceptions
All exceptions thrown by the SDK will sublcass [sentra.ApiError](./src/sentra/core/api_error.py). 

```python
from sentra.core import ApiError
from sentra import NotFoundError

try:
  sentra_client.connectors.get(1234)
except NotFoundError as e: 
  # handle bad request error
except APIError as e:  
  # handle any api related error
```

Error codes are as followed:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |

## Beta status

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning the package version to a specific version in your pyproject.toml file. This way, you can install the same version each time without breaking changes unless you are intentionally looking for the latest version.

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically. Additions made directly to this library would have to be moved over to our generation code, otherwise they would be overwritten upon the next generated release. Feel free to open a PR as a proof of concept, but know that we will not be able to merge it as-is. We suggest opening an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
