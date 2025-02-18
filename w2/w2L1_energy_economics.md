Cost of electricity
===================

This lecture covered the *cost* of electricity. The *price* was discussed on the following course day.

Emissions cost
--------------

The _emissions intensity of electricity_, EIE, can be defined as follows:

$\mathrm{EIE} = \frac{\text{lifetime emissions}}{\text{lifetime electricity generated}}$

EIE typical units: \[kg CO2\] / \[MWh\]

We ca break the lifetime emissions into an _emissions intensity of capital_, EIC, which is the CO2 emissions associated with installing a unit of nameplate power capacity, and the _emissions intensity of operation_, EIO, which is the emissions per unit of nameplate power capacity per unit of time. The lifetime emissions of electricity is, for fossil fuel power plants, dominated by the fuel consumption, part of EIO. For renewable electricity sources it is typically much lower and dominated by the embodied emissions in the materials, part of EIC.

- EIC typical units: \[ton CO2\ / MW\]
- EIO typical units: \[ton CO2\ / MW / year \] 

As an equation, the emissions intensity of electricity becomes

$\mathrm{EIE} = \frac{\mathrm{EIC}\cdot P + \mathrm{EIO}\cdot P \cdot L}{P\cdot C\cdot L} $

where $P$ is the installed nameplate power, $L$ is the lifetime of the project, and $C$ is the capacity factor

- $P$ typical units: \[MW\]
- $L$ typical units: \[year\]
- $C$ typical units: \[%\]

The emissions intensity of capital can be further broken up into embodied emissions in the materials used, EIC$_{\text{mat}}$, the emissions associated with processing the materials, EIC$_{\text{proc}}$, and the emissions associated with installation, EIC$_{\text{inst}}$.

$\mathrm{EIC}= \mathrm{EIC}_{\text{mat}} + \mathrm{EIC}_{\text{proc}} + \mathrm{EIC}_{\text{inst}}$

The emboidied emissions associated with the materials can be described as the sum over materials of the _mass intensity_ of that material per power for that technology, MI, times the material's emissions _characterization factor_, CF.

- MI, typical units \[t/MW\]
- CG, typical units \[t CO2 / t\]

As an equation, this is written:
$\mathrm{EIC}_{\text{mat}} = \sum_i^{\text{materials}} \mathrm{MI}_i \cdot \mathrm{CF}_i$

Emissions cost example: wind vs solar
-------------------------------------
