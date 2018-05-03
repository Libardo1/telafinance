title: Bank Scalability
category: page
slug: do-banks-scale
sortorder: 0303
toc: True
sidebartitle: &nbsp; Bank Scalability
meta: Could too-big-to-fail be good for banks?

# Could too-big-to-fail be good for banks?
---

&#8729; Large banks are often chided for their status of being “too-big-to-fail”

&#8729; However, if economies of scale are at work there may be an economic efficiency with maintaining larger banks	

&#8729; Several visualizations presented here suggest that banks do not gain an advantage through scale

---

<img src="/img/do-banks-scale/EmployeesVsAssets2017Q2.PNG" width="100%" alt="Banking employees versus assets" class="technical-diagram">

The concept of “economies of scale” is often brought up in economics and business. Specifically, are the returns on a business or investment going to be linear, or will there be some enhanced return that can only be achieved on a larger scale? In a simple example, one person would be hard pressed to dig up much coal with an excavator in their backyard but a business that invests in a fixed-cost deep mining operation could increase the return a single excavator could have achieved otherwise. Once the fixed investment is made, the additional return on each excavator can eventually cover the cost of the fixed investment through the additional output generated per unit. While bankers don’t “get their hands dirty” like coal miners (or, maybe they do depending on who you ask…), the same principle of fixed investments decreasing as a per-unit cost as the scale of an operation expands can still be investigated.

There are a few ways to go about this but to start this analysis we will consider assets and employees. Every bank holds some amount of assets, whether those assets are cash, or loans, or their trading book, etc. Also, every bank, assuming it’s not some sort of pass through or shell entity, has employees. For a small bank, certain investments into I.T. infrastructure or expensive vendor services may be cost prohibitive in the same way a single guy with a pickaxe can’t invest in a coal mine to maximize the coal-to-digging ratio. To use a banking example, spreadsheet based approaches to banking activities can quickly spiral into chaos depending on the scale of an activity. In another example, a bank with a large loan and deposit book may not have the ALM tools to properly manage risk. The list of cost-prohibitive but ultimately worthy investments at scale is long.

So, if we treat asset-size as a proxy for complexity, which, as a caveat, some in the too-big-to-fail field of study say may be a poor indicator, we can imagine that more assets will mean more scale and likely more investment into infrastructure. It seems at least a safe assumption that Wells Fargo and Goldman are using some tools Mom-and-Pop bank, can’t afford. Perhaps, a bank willing to make an investment into certain systems could keep a large and complicated-to-manage asset book but need half the people to manage it than if they had used a cheap spreadsheet solution. So, a larger scale may enable a bank to have more assets per employee than a smaller bank.

If this were true, we would expect to see a non-linear curve when plotting assets against employees. If banks can invest in projects that would enable their employees to manage more assets per person, then the curve slope would be increasing at a pace faster than a linear increase in assets.

And what do we see in actuality, using 2017Q2 data in the chart at the beginning of this article? A linear fit. With a linear model (on this data set for this quarter in time), 94.3% of asset size is explained by the number of employees. A strong linear fit holds even when adjusting for outliers.

So, does this answer our economies of scale question? Not entirely, as we have other aspects to measure such as income per employee or per asset. But, what we have found here is evidence to suggest that scale is not factor in determining employee needs. On average, given the 17.1 trillion in banking assets and 2.09 million employees as of 2017Q2, a bank will have just about 8.2 million in assets for each employee.

While a bank may not see benefit from scale in terms of assets-to-employees, it could well be the case for the bottom line of net income. If scale were to exist, we might see a non-linear relationship between net income and assets, which would suggest that a bank could produce more income per asset if it were larger (or less in the case of diseconomies of scale).

<img src="/img/do-banks-scale/NetIncometoAssets2017Q2.PNG" width="100%" alt="Net income versus assets" class="technical-diagram">

The chart above looks awfully similar to the previous chart. The linear fit remains even when adjusting for outliers.

Now, this isn’t to say that there are no benefits to being a large bank. While there is increased regulatory scrutiny and other challenges to being large, there aren’t many marches in the street in favor of big banks and their support. What the numbers suggest is that there is no economic advantage or disadvantage in favor of scale. A large bank may be able to take on bigger deals or trade more complex instruments but those services don’t offer some extreme return that would warrant banks to consolidate further in order to capture a greater economic efficiency.

There are a lot of ways to interpret data and numerous transformations that could be made—we will only consider two other charts here. The first being a simple log transformation of the previous chart, seen below.

<img src="/img/do-banks-scale/NetIncometoAssets2017Q2LOG.PNG" width="100%" alt="Net income versus assets natural log" class="technical-diagram">

This transformation provides an even stronger argument than the previous visualization as it controls for the extreme asset outliers. JP Morgan, Wells Fargo, Bank of America, and Citibank aren’t impacting the linear fit nearly as much here. The largest banks sit above the linear trend, further indicating that they are not at some scaling advantage and arguably suggesting the opposite.

One last visualization is considered for this investigation, though it is left for last as it is the most challenging to interpret of the lot. Instead of considering net income, the ratio of net income to equity (return on equity, “ROE”) is used in comparison to assets. This gives a two-dimensional representation of three separate factors as seen in the chart below.

<img src="/img/do-banks-scale/ROEtoAssets2017Q2.PNG" width="100%" alt="ROE versus assets" class="technical-diagram">

If banks were at some advantage for simply being larger, all else equal, we would expect to see some suggestion of a generally positive linear fit. The idea being, as banks have more assets and move upwards on the y-axis, they would tend to move to the right on the x-axis. We don’t see much evidence for that. ROE is all over the place. In fact, good luck being a bank of any reasonable size and generating a high ROE. As banks get larger they tend to cluster closer to the 5-15% ROE range, indicating the difficulty with which excess return can be generated. This isn’t surprising considering the general investing world – as trades become crowded or funds become large, abnormal returns are harder to come by.

And so the evidence here suggests that banks don’t gain an economic scaling advantage. All else equal, a large bank split into two smaller banks should be able to generate a similar return as one whole bank. That isn’t reason to split any bank up but we can argue that it isn’t reason not to. Too-big-to-fail doesn’t get any brownie points on this one.

For any questions, comments, or inquiries related to this topic or any other on this site please reach out to: contact@bankcasting.com