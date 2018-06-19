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
            chartArea: {'width': '77%','height': '80%',top:20},
            legend: 'bottom',
            vAxis: {viewWindow: {min: 2.5, max: 3.5}, format: '0.00', title: 'Annualized Growth Rate (%)'},
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

<script type="text/javascript">
function drawVisualization() {
   $.get("data/bfsi2018.csv?q="+Math.random(), function(csvString) {
      var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
      var data = new google.visualization.arrayToDataTable(arrayData);
      var chartwidth = $('#chartparent').width();
      var bfsi2018 = new google.visualization.ChartWrapper({
         chartType: 'LineChart',
         containerId: 'bfsi2018',
         dataTable: data,
         options:{
            width: chartwidth, height: 450,
            chartArea: {'width': '77%','height': '80%',top:20},
            legend: 'bottom',
            vAxis: {viewWindow: {min: 0, max: .75}, format: '0.00', title: 'Financial Stress Index'},
            series: {
               0: { color: '#529ecc' }
            }
         }
      });
      bfsi2018.draw();
   });
}
google.setOnLoadCallback(drawVisualization)
</script>

<script type="text/javascript">
function drawVisualization() {
   $.get("data/mv2018.csv?q="+Math.random(), function(csvString) {
      var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
      var data = new google.visualization.arrayToDataTable(arrayData);
      var chartwidth = $('#chartparent').width();
      var mv2018 = new google.visualization.ChartWrapper({
         chartType: 'LineChart',
         containerId: 'mv2018',
         dataTable: data,
         options:{
            width: chartwidth, height: 450,
            chartArea: {'width': '77%','height': '80%',top:20},
            legend: 'bottom',
            vAxis: {viewWindow: {min: 0, max: .45}, format: '0.00', title: 'Stock Market Valuation Index'},
            series: {
               0: { color: '#529ecc' }
            }
         }
      });
      mv2018.draw();
   });
}
google.setOnLoadCallback(drawVisualization)
</script>

## Daily market forecasts driven by the latest financial data

###<a href="/gdptoday.html">GDPToday (2018Q2)</a>
<div id="gdp18q2" style="margin-top:0px"></div>

###<a href="/market-valuation.html">Stock Market Valuation Index (2018 YTD)</a>
<div id="mv2018" style="margin-top:0px"></div>

###<a href="/bfsi.html">Bankcasting Financial Stress Index (2018 YTD)</a>
<div id="bfsi2018" style="margin-top:0px"></div>