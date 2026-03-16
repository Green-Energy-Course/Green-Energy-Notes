Cost of electricity
===================

Electricity is central in energy systems due to its ease of transport and the many ways that it can be converted into other types of energy. It is also the type of energy with the most advanced *market*, which we'll get to below. For those reasons, we'll use electricity to introduce economic concepts which also apply for other products. Before describing the market, which determines a *price*, we'll discuss the *cost* of electricity.

There are several ways to measure the cost of electricity, since it takes a lot of different types recourses to get 220 V and 50 Hz continuous alternating current into the electrical outlets in the walls of all our buildings. In this module, we'll cover two types of cost:

-  *emissions cost*, which quantifies the climate impact of a unit of electrical energy. An emissions cost is one part of a *life-cycle assessment* (see the slides on absalon), where the *functional unit* is a megawatt hour of electricity. Emissions cost is measured in kg CO2 per MWh
- *financial cost*, which is the minimum average price that you would need to sell electricity for in order to reasonably expect to make a profit over the lifetime of an electricity-producing project. The main way of calculating it is as a **levelized cost of electricity**. Financial cost is measured in Euro (or another currency) per MWh. 

We'll go into the two types of costs in more deatil below, with examples. The solutions to the examples are in the [accompanying jupyter notebook](https://github.com/Green-Energy-Course/Green-Energy-Notes/blob/main/notes/w2_examples.ipynb). 

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

See [here](https://github.com/Green-Energy-Course/Green-Energy-Notes/blob/main/notes/w2_examples.ipynb) for solutions.

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

See [here](https://github.com/Green-Energy-Course/Green-Energy-Notes/blob/main/notes/w2_examples.ipynb) for solutions.

Financial cost
--------------
The main financial way to describe the cost of electricity is as the **levelized cost of electricity** (LCOE)

- LCOE, typical unit: \[EUR / MWh\]

The levelized cost is defined as the sum of costs of a project divided by the total electricity generated by the project over its lifetime, with a catch: _money now is worth more than money later_. In otherwords, both the future costs and the future electricity $E$ to be sold are "discounted" by a certain amount each year. This amount, usually expressed in percent, is the _discount rate_, $r$. The costs can be divided into capital expenditure ($\mathrm{CAPEX}$) and operation expenditure $\mathrm{OPEX}$. All of these are summed over the years $y$ of a project starting in year 0 and up until its lifetime $L$.

- $\mathrm{LCOE}_y$, typical unit \[EUR/MWh\]
- $\mathrm{CAPEX}_y$, typical unit \[EUR\]
- $\mathrm{OPEX}_y$, typical unit \[EUR\]
- $E_y$, typical unit \[MWh\]
- $r$, typical unit \[%\]

As an equation, the LCOE is written:

$\mathrm{LCOE} = \frac{\sum_y^L \frac{\mathrm{CAPEX}_y + \mathrm{OPEX}_y}{(1+r)^y}}{\sum_y \frac{E_y}{(1+r)^y}}$

Typically, LCOE is calculated in a spreadsheet with each column representing a year. For a project that is built entirely in one year and starts generating electricity the following year, the following assumptions hold:

| year ($y$)         | 0                  | 1, 2, ...                | 
|--------------------|--------------------|--------------------------|
|$\mathrm{CAPEX}_y$  | $\mathrm{CAPEX}_0$ | 0                        | 
|$\mathrm{E}_y$      | 0                  | $C \cdot P_\mathrm{max} \cdot 1 \mathrm{yr}$ | 

where: 

- $C$ is the capacity factor, typical unit \[%\]
- $P_\mathrm{max}$ is the nameplate capacity, typical unit \[MW\]

Financial cost example: wind power
----------------------------------
You're considering investing in a small onshore wind farm, with five 3-MW wind turbines (15 MW).

You can buy the turbines for 3 million EUR a piece. They have a lifetime of 30 years. Assume that on-shore wind where you are building gets a capacity factor of 35%. Assume that operating expenditures and capital expenditures are negligible compared to the cost of the turbines.

What is the levelized cost of electricity?

See [here](https://github.com/Green-Energy-Course/Green-Energy-Notes/blob/main/notes/w2_examples.ipynb) for solutions.


Energy Markets
==============

The trouble with natural monopolies
-----------------------------------

In the late 1800's, major European and North-American cities were lit by gas lamps. Natural gas extraction and transportation had yet to be developed, so gas was typically generated nearby by *coal gasification* plants, or gas houses. Coal gasification is done by heating up coal in the presence of steam (pressurised water vapor), and proceeds by the following reactions:

C + H2O --> CO + H2

CO + H2O --> CO2 + H2  

CO + 3 H2 --> CH4 + H2O

The resulting flammable mixture of of hydrogen, methane, carbon monoxide, and carbon dioxide, was called town gas. It also contained significant amounts of hydrogen sulfide, H2S, resulting from the sulfur content of the coal. The sulfur was removed by purification with lime (calcium hydroxide), since otherwise it resulted in sulfuric acid when burned, unacceptable since town gas was also used for indoor lighting. The purification process resulted in toxic waste and a terrible smell around the gas houses.

In New York City, private companies built and operate the gas plants and pipes that delivered the gas to street lights and buildings. In a fascinating moment of energy history, these companies would often engage in turf wars:

- In the second half of the nineteenth century, with six major gas companies operating in New York City, the streets were constantly being torn up by one company or another installing or repairing their own mains – or removing those of a rival, occasionally leading to fights between rival “gas house gangs". 

Quoted from: Resurrecting the Ethnic Village: Mid-East Side: https://ethnic-village.org/the-gas-house-district/#_ednref12 

This is clearly a terribly inefficient situation. 

