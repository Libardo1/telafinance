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
   $.get("data/gdp18q1.csv?q="+Math.random(), function(csvString) {
      var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
      var data = new google.visualization.arrayToDataTable(arrayData);
      var chartwidth = $('#chartparent').width();
      var gdp18q1 = new google.visualization.ChartWrapper({
         chartType: 'LineChart',
         containerId: 'gdp18q1',
         dataTable: data,
         options:{
            width: chartwidth, height: 450,
            chartArea: {'width': '80%','height': '70%'},
            title: 'Bankcasting 2018Q1 GDP Daily Estimate',
            legend: 'bottom',
            titleTextStyle : {color: 'black', fontSize: 20},
            vAxis: {viewWindow: {min: 2, max: 3}, format: '0.0', title: 'Annualized Growth Rate (%)'},
            series: {
               0: { color: '#529ecc' }
            }
         }
      });
      gdp18q1.draw();
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
            chartArea: {'width': '80%','height': '70%'},
            title: 'Bankcasting Financial Stress Index (2018)',
            legend: 'bottom',
            titleTextStyle : {color: 'black', fontSize: 20},
            vAxis: {viewWindow: {min: 0, max: .75}, format: '0.0', title: 'Financial Stress Index'},
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

## Daily market forecasts driven by the latest financial data

###<a href="/gdptoday.html">GDPToday</a>
<div id="gdp18q1" style="margin-top:0px"></div>

###<a href="/bfsi.html">Bankcasting Financial Stress Index</a>
<div id="bfsi2018" style="margin-top:0px"></div>