title: Introduction
category: page
slug: introduction
sortorder: 0101
toc: True
sidebartitle: Introduction
meta: Bankcasting provides plain language explanations for financial topics and provides forecasts.

<script src="http://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
<script src="js/jquery.csv.min.js"></script>
<script type="text/javascript" src="http://www.google.com/jsapi"></script>

<script type="text/javascript"> // load the visualisation API
  google.load('visualization', '1', { packages: ['corechart', 'controls'] });
</script>
<script type="text/javascript">
function drawVisualization() {
   $.get("data/gdp18q2.csv?q="+Math.random(), function(csvString) {
      var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
      var data = new google.visualization.arrayToDataTable(arrayData);
      var chartwidth = $('#chartparent').width();
      var gdp18q2 = new google.visualization.ChartWrapper({
         chartType: 'LineChart',
         containerId: 'gdp18q2',
         dataTable: data,
         options:{
            width: chartwidth, height: 450,
            chartArea: {'width': '80%','height': '70%'},
            title: 'Bankcasting 2018Q2 GDP Daily Estimate',
            legend: 'bottom',
            titleTextStyle : {color: 'black', fontSize: 20},
            vAxis: {viewWindow: {min: 2.5, max: 3.5}, format: '0.0', title: 'Annualized Growth Rate (%)'},
            series: {
               0: { color: '#529ecc' }
            }
         }
      });
      gdp18q2.draw();
   });
}
google.setOnLoadCallback(drawVisualization)
</script>

## Introduction

Bankcasting provides plain language explanations for banking topics and provides forecasts.

The forecasting and analysis framework drives the written content of this website. Articles feature commentary on both the future state of the banking sector and analysis on the past trends and relationships that have occured.

---
## Daily Commentary

###<a href="/daily-commentary.html">May 10, 2018</a>
The <a href="/gdptoday.html">GDPToday</a> forecast for 2018Q2 is down -0.01% from 2.91% to 2.90%.

---
## Latest Forecasts
	
<div id="gdp18q2" style="margin-top:-10px"></div>

---
## Recommended Articles

###<a href="/provision-analysis.html">Charge-offs, Provision, and ALLL
<img src="/img/provision-analysis/COversusProvisionversusALLL2017Q3.PNG" width="100%" alt="Net Charge-offs, Provision, and ALLL for the banking industry" class="technical-diagram"></a>
&#8729; Credit losses are a critical driver of a bank's income statement 

&#8729; During downturns and times of stress, credit losses increase dramatically from baseline behavior, adversely affecting earnings and deteriorating capital

&#8729; Understanding the interaction between charge-offs, provision, and ALLL in a bank's credit loss management process is essential to analyzing banking performance over time

---

###<a href="/frb-gdp-analysis.html">GDP Analysis for the CCAR Scenarios
<img src="/img/frb-gdp-analysis/FRB2018RealGDPForecastJan2018AllScenarios.PNG" width="100%" alt="FRB CCAR 2018 Real GDP Forecast" class="technical-diagram"></a>
&#8729; Each year, the Federal Reserve releases macroeconomic forecasts for the CCAR and DFAST regulatory exercises

&#8729; While each yearly scenario has been different, there are some noticeable patterns 

&#8729; Real GDP is analyzed for historical behavior and a forecasted estimate is made for the upcoming scenario release

---

###<a href="/do-banks-scale.html">Could too-big-to-fail be good for banks?
<img src="/img/do-banks-scale/EmployeesVsAssets2017Q2.PNG" width="100%" alt="Banking employees versus assets" class="technical-diagram"></a>
&#8729; Large banks are often chided for their status of being “too-big-to-fail”

&#8729; However, if economies of scale are at work there may be an economic efficiency with maintaining larger banks	

&#8729; Several visualizations presented here suggest that banks do not gain an advantage through scale

---


