# Cachier Python Client

[![Downloads](https://static.pepy.tech/personalized-badge/base-python-package-template?period=total&units=none&left_color=grey&right_color=green&left_text=Downloads)](https://pepy.tech/project/base-python-package-template)
[![Test](https://github.com/cachier-cache/cachier-python-client/actions/workflows/test.yaml/badge.svg)](https://github.com/cachier-cache/cachier-python-client/actions/workflows/test.yaml)

A template of README best practices to make your README simple to understand and easy to use.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)

## Installation

Install the package using pip:

```sh
pip install base
```

## Usage

```python
from cachier_client import CachierClient

client = CachierClient("localhost", 8080).connect()

print("should be None:", client.get("greetings"))
client.set("greetings", "Hello, World!", 10)
print("should be something:", client.get("greetings"))
import time
time.sleep(11)
print("should be None:", client.get("greetings"))
```

## Support

Please [open an issue](https://github.com/cachier-cache/cachier-python-client/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/cachier-cache/cachier-python-client/compare/).
