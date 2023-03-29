# stactools-nisar-sim

[![PyPI](https://img.shields.io/pypi/v/stactools-nisar-sim)](https://pypi.org/project/stactools-nisar-sim/)

- Name: nisar-sim
- Package: `stactools.nisar_sim`
- [stactools-nisar-sim on PyPI](https://pypi.org/project/stactools-nisar-sim/)
- Owner: @githubusername
- [Dataset homepage](http://example.com)
- STAC extensions used:
  - [proj](https://github.com/stac-extensions/projection/)
- Extra fields:
  - `nisar-sim:custom`: A custom attribute
- [Browse the example in human-readable form](https://radiantearth.github.io/stac-browser/#/external/raw.githubusercontent.com/stactools-packages/nisar-sim/main/examples/collection.json)

A short description of the package and its usage.

## STAC Examples

- [Collection](examples/collection.json)
- [Item](examples/item/item.json)

## Installation

```shell
pip install stactools-nisar-sim
```

## Command-line Usage

Description of the command line functions

```shell
stac nisar-sim create-item source destination dither
```

Use `stac nisar-sim --help` to see all subcommands and options.

## Contributing

We use [pre-commit](https://pre-commit.com/) to check any changes.
To set up your development environment:

```shell
pip install -e .
pip install -r requirements-dev.txt
pre-commit install
```

To check all files:

```shell
pre-commit run --all-files
```

To run the tests:

```shell
pytest -vv
```
