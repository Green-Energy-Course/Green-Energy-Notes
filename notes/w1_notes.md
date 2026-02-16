The world is changing
=====================

In this course, we deal with a changing world. 
- That's why we have so many guest speakers from the frontlines: academics by ourselves would fall behind. 
- That's also why we don't have a textbook: the closest to up-to-date texts on e.g. power-to-X in existance are written for industrialists and sold at industrial prices.
- And this is why we have to understand the mathematics of societal change.

The exponential function
------------------------

A lot of things change at relative rates that are approximately constant - in other words, grow or shrink by about the same percent rate each year. 
The compound interest on a bank account is a classic example 
(even if it is a bit less relateable in the 2020's, after over a decade of ~0 interest followed by a few years of turbulence).
The value of something growing at a regular fractional increase, or *growth rate*, $r$, is

$V = V_0 \cdot (1 + r)^{\frac{t}{\Delta t}}$ 

where $V_0$ is the initial value (the value at $t=0$), $t$ is the time passed, and 
$\Delta t$ is the time interval corresponding to the growth rate $r$. For an annual growth rate, 
the most common in economics, $\Delta t = 1 \mathrm{yr}$. The growth rate is usually given in percent, e.g. $3\% = 0.03$.

For $r \ll 1$, the above equation can be rewritten using the natural (i.e. base- $e$ =2.718...) exponential function as 

$V = V_0 \cdot \exp\left(r \frac{t}{\Delta t}\right)$

The natural exponential function is mathematically nice because of identities like the one used above, but an easier base for intuitive understanding is 2. 
We can convert the above to base-2 as follows:

$V = V_0 \cdot 2^{r \frac{t}{\ln(2)\Delta t}}$

which we can rewrite as 

$V = V_0 \cdot 2^{\frac{t}{\tau_2}} $

where we've introduced the **doubling time** $\tau_2$.

This implies that the following relationship between the doubling time $tau_2$ and the increase rate $r$:

$\tau_2 = \frac{\ln(2) \Delta t}{r}$

The value of the natural log of 2 is approximately 0.7, so this becomes the following easy-to-remember "rule of 70":

**The doubling time is 70 years divided by the annual growth rate in percent**

Something that grows 1% year-on-year will double every 70 years. Something that grows 2% year-on-year will double every 35 years. And so on.


Population, economy, energy and CO2 emissions
---------------------------------------------

The defining identity of the natural exponential function is:

$\frac{\mathrm{d} \exp(x)}{\mathrm{d} x} = \exp(x)$

In other words, you get an exponential function any time something grows at a rate proportional to itself.

All else equal, this includes **population**: people make people, so the more people there are, the more people get made.

For a long period following the globalization of the industrial revolution, from approximately 1900 to 2000, population grew at about 1.7% per year. Using the rule-of-70 derived above, 
this means a doubling time of about 41 years. This is about right if you look at the time it took for world population to increase from 2 to 4 billion, or 3 to 6 billion.

Now, global population growth has decreased significantly to about 1.1% per year, attributed to changing culture with wealth and/or women's rights and girls' education as the main drivers, 
depending on who you ask. The world population growth rate is expected to keep decreasing, until it crosses 0 and world population peaks at around 10 billion people.

See here for details: https://ourworldindata.org/population-growth-over-time

**Economic output** also grows exponentially. Part of this can be explained by population growth, but the modern global 
economy also obeys the fundamental definition of an exponential function on its own: the more productive people are, the 
more surplus time and resources they have, and this surplus can be used to become more productive. This is at the core of
capitalism: wealth can grow at a rate proportional to the amount of wealth available to grow it with. The world economy is
more sensitive to events like financial crises, wars and pandemics than the world population, but usually bounces back, 
such that over the past many decades it hasn't strayed for long from an avaerage annual growth rate of about 3%.

**Global energy consumption** also grows exponentially, probably mainly due to its coupling to economic output, 
at an annual rate of about 2.2% in recent years. 

Since the industrial revolution, most of that energy comes from burning fossil fuels, 
and the chemistry of the planet changes as a result: 
**Global CO2 emissions** have grown with energy consumption. They are growing slower now, but are still growing, at an average annual rate of 0.8% per year over the past ten years. 75% of CO2 emissions come from energy consumption.

The following table summarizes these four descriptors of our changing world (check that the doubling times obey the rule-of-70)!:

|               | Current value (world) | Annual growth rate* |  Doubling time |
|---------------|-----------------------|---------------------|----------------|
| Population    | 8.3 billion           | 1.1%                | 64 years       |
| Economy       | 117 trillion USD / yr | 3.0%                | 23 years       |
| Energy use    | 20 Terawatts          | 1.6%                | 44 years       |
| CO2 emissions | 40 gigatons CO2 / yr  | 0.8%                | 87 years       |

*for the most recent ten-year period with available data (2015-2025 or 2014-2024). All data from ourworldindata.org. 

Units of energy and power
-------------------------

Economic output, energy use, and CO2 emissions are all stated in the above table as fluxes, i.e. amounts per time. This is explicit in the "per year" part of the units for economy and CO2 emissions, whereas for energy use it is implicit in the use of a unit of *power* rather than *energy*.
Make sure you are conceptually very clear on the difference:

$\mathrm{power} = \frac{\mathrm{energy}}{\mathrm{time}}$

$\mathrm{energy} = \mathrm{power}\cdot\mathrm{time}$

A Terawatt (TW) is a unit of power - a very large one, of course, since it's used here to describe the average energy consumption rate of the whole world. Specifically:

$1 \mathrm{[TW]} = 10^{12} \mathrm{[W]} = 10^{12} \mathrm{[J/s]} $

where the unit \[J\] is Joule, the SI unit for energy. 

To get a sense of how much power that is, consider the following walk up the SI prefixes:

| power scale | electrical examples                           | (bio-)chemical example                                     |
|-------------|-----------------------------------------------|------------------------------------------------------------|
| W           | small appliances, laptops                     | A human brain consumes energy at an average rate of ~ 25 W |
| kW          | large household appliances, solar panels      | A kitchen gas stove consumes fuel at a rate of ~ 20 kW     |
| MW          | wind turbines, solar farms                    | While re-fueling, energy enters a gasoline car at ~ 5 MW   |
| GW          | large power plants                            | The Palisades wildfire of burned through forest at ~ 80 GW |
| TW          | world installed capacity of many technologies | Photosynthesis in the Amazon rainforest captures ~ 3 TW    |

Energy, especially electricity, is often described in units that explicitly refer to a power times a time. These units are based on the raltionship that a Joule is a Watt-second:

$1 [\mathrm{W}\cdot \mathrm{s}] = 1 [\mathrm{J}] $

This is most commonly done with 1 hr as the unit of time. Electricity is bought and sold in kilowatt-hours. Since an hour has 60*60 = 3600 seconds, a kilowat-hour is 3600 kilowatt-seconds, which is 3600 kilojoules aka 3.6 megajoules:

$1 [\mathrm{kWh}\] = 3.6 [\mathrm{MJ}] $

and likewise up the SI prefixes: 1 MWh = 3.6 GJ, 1 GWh = 3.6 TJ, and 1 TWh = 3.6 PJ.

Electricity consumption rates are often stated in kWh/year. This may offend your scientific sensibility, since there's time in both the numerator and the denominator, but it's a unit that makes sense when doing accounting and trying to figure out how much of your annual income you spend on electricity. To convert, we use the fact that a year has 365.25 * 24 = 8766 hours. Thus, a kilowat of average power is the same as 8766 kilowatt hours per year, aka (with rounding) 8.8 megawatt-hours per year:

$1 [\mathrm{kW}\] = 8.8 [\mathrm{MWh}/\mathrm{yr}] $

and likewise up the SI prefixes: 1 MW = 8.7 GWh/yr, 1 GW = 8.8 TWh/yr, and 1 TW = 8.7 PWh/yr.

Thermal and chemical energy consumption, on the other hand, are usually given in (a very large number of) joules per year. For example, Denmark's primary energy consumption [as reported by Energistyrelsen](https://ens.dk/en/analyses-and-statistics/key-figures) in 2023 was 696 PJ. To convert to power units, we use (you guessed it!) the fact that one year is about 31.5 million seconds. Thus, 1 kilowatt is about 31.5 gigajoules per year:

$1 [\mathrm{kW}\] = 31.5 [\mathrm{GJ}/\mathrm{yr}] $

and likewise up the SI prefixes: 1 MW = 31.5 TJ/yr, 1 GW = 31.5 PJ/yr, and 1 TW = 31500 PJ/yr (I've never seen anyone use exajoules in this context).

The following table might come in handy:

| **1 kW** =| 8.77 MWh/yr  =| 31.5 GJ/yr  |
|-----------|---------------|-------------|
| 114 W    =| **1 MWh/yr** =| 3.60 GJ/yr  |
| 31.7 W   =| 278 kWh/yr   =| **1 GJ/yr** |


CO2 emissions and energy of chemicals
-------------------------------------

All of the (bio-)chemical examples of energy fluxes in the table in the previous section are assigned energy due to reaction with oxygen. In other words, the energy content of a chemical is the magnitude of its *free energy of combustion*. By "free energy", we mean the standard Gibbs free energy of combustion, $\Delta_c G^\circ$. We use the Gibbs free energy because it is by definition the maximum amount of useful kinetic energy or electricity that could theoretically be extracted from the chemical via reaction with oxygen. And we use standard conditions because, regardless of the temperature and pressure at which the reaction occurs, fuels are generally purchased at ambient conditions, and if you're expelling products at high temperature or high pressure, you're wasting energy. Similarly, we'll assume liquid water (in other words, deal with "higher heating values"), since if you're discarding uncondensed water vapor, you're wasting energy.

The standard free energy of combustion for most chemicals can be looked up directly, but it's important to know how to calculate it from the most commonly tabulated thermochemical values, which are the *standard enthalpy of formation*, $\Delta_f H^\circ$ and the *standard entropy*, $S^\circ$. From these, we can calculate the standard entropy, enthalpy, and free energy of combustion as follows:

$\Delta_c H^\circ = \sum_i \nu_i \Delta_f H^\circ_i $

$\Delta_c S^\circ = \sum_i \nu_i S^\circ_i $

$\Delta_c G^\circ = \Delta_c H^circ - T^\circ \cdot \Delta_c S^\circ $

Here $\nu_i$ is the stoichiometric coefficient of each species $i$ appearing in the reaction, and is negative for reactants and positive for products. $T^\circ=298.15 \text{K}$ is the thermochemical standard temperature. All $G$, $H$, and $S$ here (and in this course) are molar values.

For example, we calculate here the combustion of methane (CH4), which is the main component of natural gas, using the following tabulated values (from [NIST Chemistry webbook](https://webbook.nist.gov/cgi/cbook.cgi?ID=C74828&Units=SI&Mask=1#Thermo-Gas)): 

molecule | $\Delta_f H^\circ$ / [kJ/mol] | $S^\circ$ / [J/K/mol] |
|--------|-------------------------------|-----------------------|
| CH4    | -74.6  | 186.3 |
| O2     | 0      | 205.2 |
| H2O(l) | -285.8 | 70.0  |
| CO2    | -393.5 | 213.8 |

The combustion reaction is CH4 + 2 O2 --> CO2 + 2 H2O, so we have
$\nu_\text{CH4}=-1$, $\nu_\text{O2}=-2$, $\nu_\text{CO2}=1$, and $\nu_\text{H2O}=2$

Plugging it in gives:

$\Delta_c H^\circ = -890 \text{[kJ/mol]}$ 

$\Delta_c S^\circ = -523 \text{[J/K/mol]}$ 

$\Delta_c G^\circ = -818 \text{[kJ/mol]}$ 

Burning one mol of methane thus consumes 818 kJ of *primary energy*, no matter how good you are at getting something useful out of it. If you could convert it to electricity with 100% efficiency, you'd get 818 kJ (which is 0.23 kWh) out of a mole of methane.

Burning one mol of methane will also, by the stoichiometry of the combustion reaction, produce one mol of CO2. Without carbon capture, that is CO2 emissions. The ratio of emissions to energy is the *emissions intensity of energy*, EIE. The exact energy being considered needs to be specified! The EIE for the primary energy from a fuel takes a constant value given by:

$EIE_{\text{primary, fuel}} = \frac{\nu_{\text{CO2}}}{\nu_{\text{fuel}}}\frac{M_{\text{CO2}}}{\Delta_c G^\circ_{\text{fuel}}}$

For methane:

$EIE_{\text{primary, CH4}} = \frac{1}{-1}\cdot\frac{44 \text{[g/mol]}}{-818 \text{[kJ/mol]}} = 0.054 \text{[g/kJ]} = 193 \text{[g/kWh]}$

The emissions for generation of a kWh of electricity will necessarily be higher.

We can compare this to the global average emissions intensity of energy, using the global data. 75% of CO2 emissions, or 30 Gt/yr, of the global 40 Gt/yr of CO2 emissions are associated with primary energy consumption. The global primary energy consumption rate, meanwhile, was 20 TW. 

$EIE_{\text{primary, world}} =  \frac{30 \text{[Gt/yr]}}{20 \text{TW}} = 171 \text{[g/kWh]}$

Apparently, methane captures the average carbon intensity of the world's primary energy pretty well: There is a similar amount of energy consumed from the more carbon-intensive coal and oil as from the major carbon-free sources of hydropower, nuclear, wind, and solar. 

It follows from the fact that global primary energy consumption is growing at a faster annualized rate than global CO2 emissions that the carbon intensity of the world's primary energy consumption is decreasing. But is it decreasing fast enough?

Climate change
--------------
The fact that CO2 emissions cause climate change is not new science:

- In 1824, Joseph Fourier predicted the principle mechanism of the greenhouse effect: The atmosphere is relatively transparent to the visible light coming from the sun, but is relatively opaque to the infrared light leaving the earth. Fourier also correctly speculated that human activity could change the radiative balance of the earth. 
- In 1856, Eunice Newton Foote made the first experimental observation of CO2 as a greenhouse gas: A test tube filled with "carbonic acid gas" heated up more than a test tube filled with air in sunlight. She correctly surmised that "if... the air had mixed with it a larger proportion than at present, an increased temperature from its action... must have necessarily resulted." Many other scientists in the years after came to similar conclusions. 
- in 1859, John Tyndall made the first infrared spectra of pure gases were reported, identifying water vapor, CO2, and methane as greenhouse gases.
- Svante Arrhenius made the first quantitative estimate of the greenhouse effect of CO2 resulting from the burning of coal, predicting that a double in atmospheric CO2 (i.e., form 280 in his time to a hypothetical 560 ppm - we are now more than half way) would increase the world's temperature by about 5-6 C. (He apparently overestimated somewhat.) He thought this would take hundreds of years... he forgot to account for the exponential increase in energy use.

The exponential function starts slow but picks up speed. In the 1960's, scientists began to be confident that they were observing the actual increase in global average temperatures resulting from the greenhouse effect. Now there is no doubt.

This figure shows the average surface temperature of the earth as a function of atmospheric CO2 concentration. Each point represents both values averaged over a calendar year:

![figure](../figures/T_vs_CO2_concentration.svg)

This figure is made with data from Our World In Data [by the script here](../figures/plot_world_temperature_vs_CO2.py).


Global climate policy: A brief history of the UNFCCC
----------------------------------------------------




Energy conversion technologies
==============================






