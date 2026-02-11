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
(even if it is a bit less relateable in the 2020's, after over a decade of ~0 interest followed by a few years of turbulence.
The value of something growing at a yearly fractional increase $r$ is

$V = V_0 \cdot (1 + r)^{\frac{t}{\Delta t}}$ 

where $V_0$ is the initial value (the value at $t=0$), $t$ is the time passed, and 
$\Delta t$ is the time interval corresponding to the increase rate $r$ (normally $\Delta t = 1 \mathrm{yr}$)

For $r \ll 1$, this can be rewritten using the natural (i.e. base- $e$ =2.718...) exponential function as 

$V = V_0 \cdot \exp\left(r \frac{t}{\Delta t}\right)$

The natural exponential function is mathematically nice because of identities like the one used above, but an easier base for intuitive understanding is 2. 
We can convert the above to base-2 as follows:

$V = V_0 \cdot 2^{r \frac{t}{\ln(2)\Delta t}}$

which we can rewrite as 

$V = V_0 \cdot 2^{\frac{t}{\tau_2}} $

where we've introduced the **doubling time** $\tau_2$.

This implies that the following relationship between the doubling time $tau_2$ and the increase rate $r$:

$\tau_2 = \frac{\ln(2) \Delta t}{r}$

The value of the natural log of 2 is approximately 0.7, so this becomes the following easy-to-remember rule:

**The doubling time is 70 years divided by the annual growth rate in percent**

Something that grows 1% year-on-year will double every 70 years. Something that grows 2% year-on-year will double every 35 years. And so on.


Population, economy, energy and CO2 emissions
---------------------------------------------

The defining identity of the natural exponential function is:

$\frac{\mathrm{d} \exp(x)}{\mathrm{d} x} = \exp(x)$

In other words, you get an exponential function any time something grows at a rate proportional to itself.

Without physical or cultural limitations, this includes **population**: people make people, so the more people there are, the faster (in absolute numbers) the population will grow.

For a long period following the globalization of the industrial revolution, from approximately 1900 to 2000, population grew at about 1.7% per year. Using the rule-of-70 derived above, 
this means a doubling time of about 41 years. This is about right if you look at the time it took for world population to increase from 2 to 4 billion, or 3 to 6 billion.

Now, it's decreased significantly to about 1.1% per year, attributed to changing culture with wealth and/or women's rights and girls' education as the main drivers, 
depending on who you ask. World population growth rate is expected to keep decreasing, until it crosses 0 and world population peaks at around 10 billion people.

See here for details: https://ourworldindata.org/population-growth-over-time

**Economic output** also grows exponentially. Part of this can be explained by population growth, but economics also obey the fundamental definition of an exponential function
on its own: the more productive people are, the more surplus time and resources they have, and this surplus can be used to become more productive. This is at the core of
capitalism: wealth can grow at a rate proportional to the amount of wealth available to grow it with. The world economy is more sensitive to events like financial crises, wars
and pandemics than the world population, but usually bounces back, such that over the past many decades it hasn't strayed for long from an avaerage annual growth rate of about 3%.

**Global energy consumption** also grows exponentially, probably mainly due to its coupling to economic output, at an annual rate of about 2.2% in recent years. 

Since the industrial revolution, most of that energy comes from burning fossil fuels, and the chemistry of the planet changes as a result: 
**Global CO2 emissions** have grown with energy consumption. They are growing slower now, but are still growing, at an average annual rate of 0.8% per year over the past ten years.

The following table summarizes these four descriptors of our changing world (check that the doubling times obey the rule-of-70)!:

|               | Current value (world) | Annual growth rate* |  Doubling time |
|---------------|-----------------------|---------------------|----------------|
| Population    | 8.3 billion           | 1.1%                | 64 years       |
| Economy       | 117 trillion USD / yr | 3.0%                | 23 years       |
| Energy Use    | 20 Terawatts          | 1.6%                | 44 years       |
| CO2 emissions | 40 gigatons CO2 / yr  | 0.8%                | 87 years       |

*for the most recent ten-year period with available data (2015-2025 or 2014-2024). All data from ourworldindata.org. 

Units of energy and emissions
-----------------------------


Climate change
--------------


Global climate policy: A brief history of the UNFCCC
----------------------------------------------------




Energy and the technologies that convert it
===========================================

