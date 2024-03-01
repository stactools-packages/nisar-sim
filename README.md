# stactools-nisar-sim

- Name: nisar-sim
- Package: `stactools.nisar_sim`
- Owner: @jjfrench @wildintellect
- [Dataset homepage](https://uavsar.jpl.nasa.gov/science/documents/nisar-sample-products.html)
- STAC extensions used:
  - [proj](https://github.com/stac-extensions/projection/)
  - [sat](https://github.com/stac-extensions/sat)

stactools package for use with the simulated NISAR products.

## STAC Examples

- [Collection](examples/collection.json)
- [Item](examples/winnip_31604_12061_004_120717_L090_CX_07/winnip_31604_12061_004_120717_L090_CX_07.json)

## Installation

```shell
pip install stactools-nisar-sim
```

## Command-line Usage

Command line functions

```shell
stac nisarsim create-collection <destination/>

stac nisarsim create-collection example-collection.json
```

```shell
stac nisarsim create-item <source/> <destination/>

stac nisarsim create-item tests/data/NISAR_L0_PR_RRSD_001_005_A_128S_20081012T060910_20081012T060926_P01101_F_J_001.h5 examples/NISAR_L0_PR_RRSD_001_005_A_128S_20081012T060910_20081012T060926_P01101_F_J_001.json
```

Use `stac nisarsim --help` to see all subcommands and options.

## Contributing

We use [pre-commit](https://pre-commit.com/) to check any changes.
To set up your development environment:

```shell
pip install -e '.[dev]'
pre-commit install
```

To check all files:

```shell
pre-commit run --all-files
```

To run the tests:

```shell
./scripts/test
```

If you've updated the STAC metadata output, update the examples:

```shell
scripts/update-examples
```
