Cost of electricity
===================

Electricity is central in energy systems due to its ease of transport and the many ways that it can be converted into other types of energy. It is also the type of energy with the most advanced *market*, which we'll get to below. For those reasons, we'll use electricity to introduce economic concepts which also apply for other products. Before describing the market, which determines a *price*, we'll discuss the *cost* of electricity.

There are several ways to measure the cost of electricity, since it takes a lot of different types recourses to get 220 V and 50 Hz continuous alternating current into the electrical outlets in the walls of all our buildings. In this module, we'll cover first the *emissions cost*, which quantifies the climate impact of a unit of electrical energy; and then the *financial cost*, which is the minimum average price that you would need to sell electricity for in order to reasonably expect to make a profit over the lifetime of an electricity-producing project. Emissions cost is measured in kg CO2 per MWh, while financial cost is measured in Euro (or another currency) per MWh. 

These notes should be read together with the [accompanying jupyter notebook](https://github.com/Green-Energy-Course/Green-Energy-Exercises/blob/main/w2_examples.ipynb) with the worked examples. 

Emissions cost
--------------

The _emissions intensity of electricity_, EIE, can be defined as follows:

$\mathrm{EIE} = \frac{\text{lifetime emissions}}{\text{lifetime electricity generated}}$

$\mathrm{EIE}$ typical units: \[kg CO2\] / \[MWh\]

We ca break the lifetime emissions into an _emissions intensity of capital_, EIC, which is the CO2 emissions associated with installing a unit of nameplate power capacity, and the _emissions intensity of operation_, EIO, which is the emissions per unit of nameplate power capacity per unit of time. The lifetime emissions of electricity is, for fossil fuel power plants, dominated by the fuel consumption, part of EIO. For renewable electricity sources it is typically much lower and dominated by the embodied emissions in the materials, part of EIC.

- $\mathrm{EIC}$ typical units: \[t CO2 / MW\]
- $\mathrm{EIO}$ typical units: \[t CO2 / MW / year \] 

As an equation, the emissions intensity of electricity becomes

$\mathrm{EIE} = \frac{\mathrm{EIC}\cdot P + \mathrm{EIO}\cdot P \cdot L}{P\cdot C\cdot L} $

where $P$ is the installed nameplate power, $L$ is the lifetime of the project, and $C$ is the capacity factor

- $P$ typical units: \[MW\]
- $L$ typical units: \[year\]
- $C$ typical units: \[%\]

The emissions intensity of capital can be further broken up into embodied emissions in the materials used, $\mathrm{EIC}\_\text{mat}$, 
the emissions associated with processing the materials, $\mathrm{EIC}\_\text{proc}$, 
and the emissions associated with installation, $\mathrm{EIC}\_\text{inst}$.

$\mathrm{EIC}= \mathrm{EIC}\_{\text{mat}} + \mathrm{EIC}\_{\text{proc}} + \mathrm{EIC}\_{\text{inst}}$

The emboidied emissions associated with the materials can be described as the sum over materials of the _mass intensity_ of that material per power for that technology, MI, times the material's emissions _characterization factor_, CF.

- $\mathrm{MI}$, typical units \[t/MW\]
- $\mathrm{CF}$, typical units \[t CO2 / t\]

As an equation, this is written:
$\mathrm{EIC}_{\text{mat}} = \sum_i^{\text{materials}} \mathrm{MI}_i \cdot \mathrm{CF}_i$

Emissions cost example: wind vs solar
-------------------------------------

What is **embodied carbon per MW of installed capacity** ($\mathrm{EIC}\_{\text{mat}}$) for **(a) wind** and **(b) solar**? 

Use the following materials requirements (MI) for wind and solar:

| material | MI for wind / \[t/MW\] | MI for solar / \[t/MW\] | 
|----------|------------------------|-------------------------|
|concrete  | 500                    | 500                     | 
|steel     | 50                     | 100                     | 
|aluminium | 0                      | 60                      | 
|copper    | 5                      | 4                       | 
|silicon   | 0                      | 5                       | 

And the following characterization factors:

| material | CF / \[t CO2 / t\] | 
|----------|--------------------|
|concrete  | 0.18               |
|steel     | 1.9                |
|aluminium | 6.8                |
|copper    | 4.6                |
|silicon   | 10                 |

What is the **emissions intensity of electricity** for **(c) wind** and **(d) solar** assuming that the above-calculated $\mathrm{EIC}\_{\text{mat}}$ is the dominant cause of emissions over the project lifetime (approximate $\mathrm{EIC}\_{\text{proc}}$, $\mathrm{EIC}\_{\text{proc}}$, and $\mathrm{EIO}$ to all be zero). Use the following lifetimes and capacity factors:

|                | wind | solar |
|----------------|------|-------|
|$L$ / \[years\] | 25   | 30    |
|$C$             | 50%  | 10%   |

Emissions payback time
----------------------

The emissions payback time, $\mathrm{EPT}$, is the amount of time, in years, for a project to come out emissions neutral compared to a situation in which the project was not built.

- $\mathrm{EPT}$, typical units \[year\]

This is equal to the emissions due to installation divided by the _emissions saving rate_ saved per installed capacity per year of operation, ESR:

$\mathrm{EPT} = \frac{\mathrm{EIC}}{\mathrm{ESR}}$

- $\mathrm{ESR}$, typical unit \[t CO2 / yr\] 

Here, the emissions saving rate is the _marginal emissions of electricity_ generated minus the marginal emissions of electricity for the electricity that it replaces in the grid. For renewables, since we are assuming for now that the entire lifetime emissions is due to the materials cost (EIO=0), we can also approximate the marginal emissions due to a unit of electricity generated as zero. The emissions saving rate for renewables is therefore the average electricity generation rate per unit installed power times the emissions intensity of electricity in the present mix in the grid:

$\mathrm{ESR}(\text{renewables}) = C \cdot \mathrm{EIE}_{\text{grid}}$


where we have used that capacity factor $C$ can be defined as the average electricity generation rate per unit of installed power.



Emissions payback time example: wind and solar
----------------------------------------------

Using the results of the previous example and an average grid emissions intensity $\mathrm{EIE}_{\text{grid}}$ for Denmark in 2024 of 120 [g/kWh], **what is the emissions payback** time for **(a) solar** and **(b) wind**?


