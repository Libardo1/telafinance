title: Profit Distribution
category: page
slug: profit-distribution
sortorder: 0302
toc: True
sidebartitle: &nbsp; Profit Distribution
meta: The banking profitability distribution has some odd characteristics

# The banking profitability distribution has some odd characteristics
---
<p>
&#8729; An experienced analyst wouldn’t expect many normal distributions in the finance world—but a normal distribution does provide a useful starting assumption
<p>
&#8729; The banking profitability distribution looks normal at first glance around the mean
<p>
&#8729; However, the shape is positively skewed and leptokurtic, exhibiting noticeably fat tails
---
<img src="/img/profit-distribution/NetIncomeOverAverageAssetsHistogram2017Q2.PNG" width="100%" alt="Banking Profit Distribution" class="technical-diagram">
Most practitioners can recall a time they were given the advice to “not assume normality.” Nevertheless, not only is the normal distribution a basic statistical concept but it is also one of the most pervasive assumptions used in finance (like many other statistically approached fields). It is often the starting point for distribution analysis and, unfortunately, the ending point as well. A major reason for this is the non-intuitive nature of alternative frameworks…and, of course, laziness. Despite the challenges, one doesn’t need an advanced degree in statistics to apply some basic analysis to a given distribution to gain some insight into the behavior of a sample or population.
<p>
Profitability, measured here as net income, which is the bottom line on a bank’s income statement, is one of the most important metrics for performance analysis. For the balance sheet, total assets represent another key summarized aggregation measure. So, both metrics provide a great starting point for a top-down analysis. When these two metrics are combined by dividing a bank’s net income by total assets, the ratio analysis provides insight into the relative profitability of a given bank when controlling for asset size. In general, it’s an important question to ask for benchmarking purposes, “How profitable is a given bank and how profitable should it be based on its peer group?”
<p>
To help answer this question, net income through the second quarter of 2017 is annualized and divided by average assets for the same period for all available banks. In addition to the full data set, the top and bottom one percent of outliers are removed for further analysis. The summary statistics for these data sets can be seen in the following table.
<p>

| Summary Statistics &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;    | Full data set &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;    | +/-1% outliers   &nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;     |
|-------------------------|--------------------|-------------------------|
| Mean                    |              1.17  |                   0.99  |
| Standard Error          |              0.06  |                   0.01  |
| Median                  |              0.92  |                   0.92  |
| Mode                    |              0.91  |                   0.91  |
| Standard Deviation      |              4.38  |                   0.65  |
| Kurtosis                |      2,446.09      |                   9.46  |
| Skewness                |            42.23   |                   1.67  |
| Range                   |         298.45     |                   7.50  |
| Minimum                 |          (28.69)   |                 (1.24)  |
| Maximum                 |         269.76     |                   6.26  |
| Sum                     |      6,811.67      |           5,637.14      |
| Count                   |      5,839         |           5,721         |
| Largest                 |         269.76     |                   6.26  |
| Smallest                |          (28.69)   |                 (1.24)  |

<br>
The mean for the full data set is 1.17, while the industry ratio, which is measured by aggregating the individual ratio components of each bank before ratio calculation, is 1.10. The mean and mode, are .92 and .91, respectively. Using these measures of the distribution center, it is already apparent that the data is not symmetric like a normal distribution. The mean is much greater and the median slightly greater than the mode, which indicates positive skewness, as a normal distribution has a skewness of zero. This positive skewness is expected and logical. The distribution of banks should be expected to have a profit-to-asset ratio greater than zero, as that indicates banks are providing a return or, more simply, making money.
<p>
Looking at the direct results for skewness, the full data set shows 42.23 while the reduced set has a less extreme 1.67. The reduced skewness is much closer to zero but still greater than zero. So, the data suggests a fairly consistent story about positive skewness, which is, again, a good thing for banks (or any business for that matter)!
<p>
The full data set standard deviation is much larger than the data set with outliers removed, suggesting some extreme outliers. The range confirms this, with 298.45 for the full set and 7.50 for the reduced set.
<p>
When reviewing the chart, one would expect to see about 95% of observations within two standard deviations of the mean if the data were normally distributed. Instead, two standard deviations capture a much higher percentage. In fact, the major cluster of data sits within about a tenth of one standard deviation. Removing the top and bottom one percent brings the deviation to a smaller value of 0.65, versus the 4.38 for the full set.
<p>
In terms of the distribution shape, kurtosis for a normal distribution would be three. Instead of three, we have 2,446.09 for the full data set. Wow. That is definitely not normal. A value greater than three suggests a leptokurtic shape, which means fatter tails, meaning the distribution would be expected to produce more outliers than a normal distribution. The 89 banks below the smallest bucket value and 118 banks above the largest bucket value support this expectation. And, when outliers are removed, the shape is still leptokurtic at 9.46.
<p>
So, beyond just analyzing the raw numbers, which can sometimes be a bit boring, what would one expect to see if visualizing a distribution? By taking the histogram bucket value, mean, and standard deviation, we can plot the expected normal distribution shape. For the full data set, this is the black dotted line on the chart above. If analyzed closely, this line that at first glance seems flat, is actually slightly curved. This suggests that the bucket size, if this was indeed a normal distribution, is much too small. But, clearly it isn’t, as the data fits nicely and shows a full shape except for the fat tails.
<p>
Removing the outliers produces the aforementioned lower standard deviation. Using the same formula inputs but changing to the lower standard deviation produces the bell curve exhibited as the orange line. Finally, by just shaving off a percentage from the top and bottom of the data set, we can see something that looks decent enough to compare to the data set from a visual, not numerical, perspective. The visualization confirms what the numerical data implied. The shape of the profit distribution is indeed leptokurtic, as seen by the cluster of data that sits well above the center of the orange normal distribution. The large tails of the data set, though a summation of the data below the curve as opposed to an exact comparison to the height of the orange normal distribution, suggest that many more observations can be found further down the tail.
<p>
So, the expected behavior of the curve suggests that for a given bank, one would most likely see a profit-to-asset ratio close to the mean or industry average. Most banks are performing relatively similar to each other. However, if the bank happens to be an outlier, then that would be a poor and misleading assumption. The bank would likely be either a big winner or a huge loser, in a way much greater than the average and a normal distribution would lead one to expect.
<p>
There are a few ways to explain this behavior. For the most part, banks are bound by the same rules and regulations and given the homogenization of some business aspects of finance, performance should be clustered around a market average. For the outliers, banks may be quite small and have numbers skewed by size, which could be checked by eliminating banks below a certain threshold. Also, outliers could be controlled by extending the time period that is considered for the ratio. Some banks may have really good or bad quarters but if they are outliers over a long enough period of time they are either going out of business or making shareholders a lot of money.
<p>
Ultimately, this analysis supports the adage to “expect the unexpected.” One should not assume normal behavior for anything in the finance field. However, the normal assumption provides a powerful starting point and framework for the behavior that could be expected, if not normal. It is a powerful tool for any analysis and can be applied to a diverse group of datasets.

<p>
<p>
For any questions, comments, or inquiries related to this topic or any other on this site please reach out to: contact@bankcasting.com