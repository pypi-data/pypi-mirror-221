# BalderHub Package `balderhub-rfb`

This is a BalderHub package for the [Balder](https://docs.balder.dev) test framework. It allows 
you to test RFB/VNC clients, without the need of writing own tests. If you are new to Balder check out the
[official documentation](https://docs.balder.dev) first.

## Installation

You can install the latest release with pip:

```
python -m pip install balderhub-rfb
```

## Import scenarios

You can activate scenarios by importing them into your project:

```python
# file `scenario_balderhub_rfb.py
from balderhub.rfb.scenarios.client.handshaking import ScenarioRfbHandshakingIllegalProt, \
    ScenarioRfbHandshakingNoSecType, ScenarioRfbHandshakingSecHandshakeFailed, ScenarioRfbHandshakingSecTypeNone, \
    ScenarioRfbHandshakingSecTypeVnc
```

If you add a file that imports the scenario classes, Balder will automatically collect them (if they are in a file 
that starts with file starting with ``scenario_*.py``).

## Create a setup

Checkout [the example section of the documentation](https://hub.balder.dev/projects/rfb/en/latest/examples.html) 
for more details.

# Check out the documentation

If you need more information, 
[checkout the ``balderhub-rfb`` documentation](https://hub.balder.dev/projects/rfb).


# License

This BalderHub package is free and Open-Source

Copyright (c) 2023 Max Stahlschmidt and others

Distributed under the terms of the MIT license