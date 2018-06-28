title: GDP
category: page
slug: gdp
sortorder: 0202
toc: True
sidebartitle: &nbsp; GDP
meta: Tela's daily tracker for GDP

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
            title: 'Tela 2018Q2 GDP Daily Estimate',
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

<script type="text/javascript">
function drawVisualization() {
   $.get("data/gdp18q1.csv?q="+Math.random(), function(csvString) {
      var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
      var data = new google.visualization.arrayToDataTable(arrayData);
      var chartwidth = $('#chartparent').width();
      var crt_ertdlyYY = new google.visualization.ChartWrapper({
         chartType: 'LineChart',
         containerId: 'crt_ertdlyYY',
         dataTable: data,
         options:{
            width: chartwidth, height: 450,
            chartArea: {'width': '80%','height': '70%'},
            title: 'Tela 2018Q1 GDP Daily Estimate',
            legend: 'bottom',
            titleTextStyle : {color: 'black', fontSize: 20},
            vAxis: {viewWindow: {min: 2, max: 3}, format: '0.0', title: 'Annualized Growth Rate (%)'},
            series: {
               0: { color: '#529ecc' }
            }
         }
      });
      crt_ertdlyYY.draw();
   });
}
google.setOnLoadCallback(drawVisualization)
</script>

# GDPToday
---

&#8729; Tela provides forecasted estimates for upcoming official GDP releases from the Bureau of Economic Analysis

&#8729; The forecast is updated every weekday that does not fall on a holiday

&#8729; The official first estimate for 2018Q2 GDP from the BEA will be released on July 27, 2018.

---

<div id="gdp18q2" style="margin-top:-10px"></div>
<br>
<div id="crt_ertdlyYY" style="margin-top:-10px"></div>
<br>