# stactools-nisar-sim

[![PyPI](https://img.shields.io/pypi/v/stactools-nisar-sim)](https://pypi.org/project/stactools-nisar-sim/)

- Name: nisar-sim
- Package: `stactools.nisar_sim`
- [stactools-nisar-sim on PyPI](https://pypi.org/project/stactools-nisar-sim/)
- Owner: @jjfrench @wildintellect
- [Dataset homepage](https://uavsar.jpl.nasa.gov/science/documents/nisar-sample-products.html)
- STAC extensions used:
  - [proj](https://github.com/stac-extensions/projection/)
  - [sat](https://github.com/stac-extensions/sat)
- [Browse the example in human-readable form](https://radiantearth.github.io/stac-browser/#/external/raw.githubusercontent.com/stactools-packages/nisar-sim/main/examples/collection.json)

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

**Dither**: Indicates whether the data has been dithered or not:

- "X": not dithered,
- "G": dithered with gaps,
- "D": dithered with no gaps.

**Nmode**: NISAR mode, a 3-digit mode number associated a specific center
  frequency, bandwidth, and polarization.

- "129"
- "138"
- "143"

Read more about the _Dither_ and _Nmode_ namings [here](https://uavsar.jpl.nasa.gov/science/documents/nisar-sample-products.html#Product%20Description:~:text=about%20dithered%20products.-,Naming%20Convention,-The%20simulated%20NISAR).

```shell
stac nisarsim create-item <source/> <destination/> --dither <dither> --nmode <nmode>

stac nisarsim create-item
https://downloaduav.jpl.nasa.gov/Release2v/winnip_31604_12061_004_120717_L090_CX_07/
example.json --dither X --nmode 129
```

Use `stac nisarsim --help` to see all subcommands and options.

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
./scripts/test
```
