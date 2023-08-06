# vlclient

API Wrapper for VALORANT's client API

**NOTE**: This is a fork of the new inactive [valclient.py](https://github.com/colinhartigan/valclient.py)
with some edits of my taste.

## Fork changes

Skipped some configurations files I did not even understand and went straight
to using Poetry.

## Installation

Using `pip`:

```sh
pip install vlclient
```

Using [poetry](https://python-poetry.org):

```sh
poetry add vlclient
```

## Usage

```python
from vlclient.client import Client

client = Client(region="na")
client.activate()

# get MatchID of latest match
history = client.fetch_match_history(queue_id="unrated")
print(history["History"][0]["MatchID"])
```

## Documentation

Refer to [Techdoodle's documentation](https://github.com/techchrism/valorant-api-docs/tree/trunk/docs) for exact API details.

Most endpoints are implemented in this wrapper, but some are missing.
Please consider contributing.