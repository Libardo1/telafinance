title: How to gather economic data with Python
slug: python-fred-excel
category: post
date: 2018-08-31
modified: 2018-08-31
newsletter: False
meta:  A guide to gathering economic data from FRED using a Python-based API.
headerimage: /img/python-fred-excel/python-fred-excel.png
headeralt: Python, FRED, and Excel Logos

This guide provides a simple Python solution to gather <a href="https://fred.stlouisfed.org/">Federal Reserve Economic Data ("FRED")</a> and export information to an organized excel spreadsheet. Implementing the script is an easy way to improve data gathering efficiency for financial and economic analysis.

<img src="/img/python-fred-excel/python-fred-excel.png" width="100%" alt="Python, FRED, and Excel Logos" class="technical-diagram">

## Using FRED

As of writing, FRED warehouses 509,000 economic time series from 87 sources. Manually downloading information through the website, or even running the excel add-in, can be cumbersome. Luckily, time-saving API pulls are possible with the use of the third-party Python package <a href="https://github.com/mortada/fredapi">fredapi</a>.

The first step is to obtain an API key. Register for a free FRED account and click on "API Keys" under "My Account." Once there, click on "request API Key," fill out the form and a new key will be generated.

## Setting up Python

If you are an excel addict who doesn't have Python, it can be easily downloaded <a href="https://www.python.org/downloads/">here</a>. Once installed, the following lines in the command console can install the two packages required for the API requests: pandas and fredapi.

```python
pip install pandas
pip install fredapi
```

## Writing code

Once these packages are installed, a script with code is needed. On windows, one can simply open notepad and save the file as something such as "fred.py" to create a script. Open the script with either notepad itself or a more advanced editor to begin coding.

To start the script, we import the packages:

```python
import pandas as pd
from pandas import DataFrame
from fredapi import Fred
```

A line of code is needed to input the API key generated earlier:

```python
fred = Fred(api_key='insert key string between apostrophes here')
```

For this example, the code will pull three economic time series of varying frequency: <a href="https://fred.stlouisfed.org/series/gdpc1">Real Gross Domestic Product</a>, the <a href="https://fred.stlouisfed.org/series/T10Y2Y">10-Year Treasury Constant Maturity Minus 2-Year Treasury Constant Maturity</a>, and <a href="https://fred.stlouisfed.org/series/CPIAUCSL">Consumer Price Index for All Urban Consumers: All Items</a>.

We can do this with the following block of code that calls both the time series and the dates of the time series for easy excel exporting:

```python
df1 = {}
df1['GDPC1'] = fred.get_series('GDPC1')
df1['GDPC1 Dates'] = fred.get_series('GDPC1').index
df1 = pd.DataFrame(df1)

df2 = {}
df2['T10Y2Y'] = fred.get_series('T10Y2Y')
df2['T10Y2Y Dates'] = fred.get_series('T10Y2Y').index
df2 = pd.DataFrame(df2)

df3 = {}
df3['CPIAUCSL'] = fred.get_series('CPIAUCSL')
df3['CPIAUCSL Dates'] = fred.get_series('CPIAUCSL').index
df3 = pd.DataFrame(df3)
```

To combine the three dataframes into one dataframe, we can use the concatenate function:

```python
df = pd.concat([df1, df2, df3], ignore_index=False, axis=1)
```

Finally, we export the data to an excel sheet:

```python
df.to_csv('data.csv', index=False)
```

## Analyzing the Excel output

In this example, the data output is organized by observation date. So, the data in the .csv output file should look like the image below.

<img src="/img/python-fred-excel/exceldata.png" width="100%" alt="Excel Data Output Python API" class="technical-diagram">

While this format is different than the excel add-in, from experience it is more useful as each row is linked to a specific date, which becomes more important as the dataset grows with additional pulls beyond three time series. This format is also advantageous in that a quick index match formula based on static columns can automatically update as refreshed runs of the script bring in new data.

## Conclusion

That's it! Now, instead of manually pulling information from FRED or using the slow and clunky excel add-in, data can be automatically pulled and updated by just running the script. To get other times series, just change the series codes or add new lines of code for additional data pulls.

For those who are most comfortable in excel, this simple pull might be all that is needed. For those who want more, a guide to the additional functions that can be run using the fredapi package can be found <a href="http://mortada.net/python-api-for-fred.html">here</a>.

Overall, the new script should result in less time spent doing manual data pulls and organization and more time spent performing insightful analysis.

<hr>

For any questions, comments, or inquiries related to this article or any other on this site please reach out to: contact@telafinance.com

<hr>

<!--<h3>Related To</h3>-->
<div class="row">
    <div class="col-md-4">
        <div class="well select-next">
<a href="/blog/chinas-rise-in-gdp.html" class="btn btn-success btn-full"><svg width="28" height="30" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg"><path d="M640 896v512h-256v-512h256zm384-512v1024h-256v-1024h256zm1024 1152v128h-2048v-1536h128v1408h1920zm-640-896v768h-256v-768h256zm384-384v1152h-256v-1152h256z" fill="#fff"/></svg></a>
<p class="under-btn">Analyzing China's rise in GDP.</p>       </div>
    </div>
       
    <div class="col-md-4">
        <div class="well select-next">
<a href="/blog/can-you-hold-for-forty-years.html" class="btn btn-success btn-full"><svg width="28" height="30" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg"><path d="M1760 896q0 176-68.5 336t-184 275.5-275.5 184-336 68.5-336-68.5-275.5-184-184-275.5-68.5-336q0-213 97-398.5t265-305.5 374-151v228q-221 45-366.5 221t-145.5 406q0 130 51 248.5t136.5 204 204 136.5 248.5 51 248.5-51 204-136.5 136.5-204 51-248.5q0-230-145.5-406t-366.5-221v-228q206 31 374 151t265 305.5 97 398.5z" fill="#fff"/></svg></a>
<p class="under-btn">A historical view of the Dow Jones Industrial Average.</p>        </div>
    </div>
    <div class="col-md-4">
        <div class="well select-next">
<a href="/blog.html" class="btn btn-success btn-full"><svg width="28" height="30" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg"><path d="M1591 1448q56 89 21.5 152.5t-140.5 63.5h-1152q-106 0-140.5-63.5t21.5-152.5l503-793v-399h-64q-26 0-45-19t-19-45 19-45 45-19h512q26 0 45 19t19 45-19 45-45 19h-64v399zm-779-725l-272 429h712l-272-429-20-31v-436h-128v436z" fill="#fff"/></svg></a>
<p class="under-btn">The latest articles on Tela.</p>         </div>
    </div>
</div>

<hr>

<!-- Begin MailChimp Signup Form -->
<link href="//cdn-images.mailchimp.com/embedcode/horizontal-slim-10_7.css" rel="stylesheet" type="text/css">
<style type="text/css">
	#mc_embed_signup{background:#fff; clear:left; font:14px Helvetica,Arial,sans-serif; width:100%;}
	/* Add your own MailChimp form style overrides in your site stylesheet or in this style block.
	   We recommend moving this block and the preceding CSS link to the HEAD of your HTML file. */
</style>
<div id="mc_embed_signup">
<form action="https://telafinance.us17.list-manage.com/subscribe/post?u=b3b11f090db9e2871e474b005&amp;id=204a12fade" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank" novalidate>
    <div id="mc_embed_signup_scroll" align="center">
	<label for="mce-EMAIL">Join the Tela Insights Newsletter. Just one email each week.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
	<input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_b3b11f090db9e2871e474b005_204a12fade" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>

<!--End mc_embed_signup-->