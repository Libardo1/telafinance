title: Bankcasting Stock Market Valuation Index
category: page
slug: market-valuation
sortorder: 0203
toc: True
sidebartitle: &nbsp; Stock Market Valuation Index
meta: Bankcasting Stock Market Valuation Index

<script src="http://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
<script src="js/jquery.csv.min.js"></script>
<script type="text/javascript" src="http://www.google.com/jsapi"></script>

<script type="text/javascript"> // load the visualisation API
  google.load('visualization', '1', { packages: ['corechart', 'controls'] });
</script>
<script type="text/javascript">
function drawVisualization() {
   $.get("data/mv.csv?q="+Math.random(), function(csvString) {
      var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
      var data = new google.visualization.arrayToDataTable(arrayData);
      var chartwidth = $('#chartparent').width();
      var mv = new google.visualization.ChartWrapper({
         chartType: 'LineChart',
         containerId: 'mv',
         dataTable: data,
         options:{
            width: chartwidth, height: 450,
            chartArea: {'width': '80%','height': '70%'},
            title: 'Bankcasting Stock Market Valuation Index',
            legend: 'bottom',
            titleTextStyle : {color: 'black', fontSize: 20},
            vAxis: {viewWindow: {min: -1, max: 1}, format: '0.0', title: 'Stock Market Valuation Index'},
            series: {
               0: { color: '#529ecc' }
            }
         }
      });
      mv.draw();
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
            chartArea: {'width': '80%','height': '70%'},
            title: 'Bankcasting Stock Market Valuation Index (2018)',
            legend: 'bottom',
            titleTextStyle : {color: 'black', fontSize: 20},
            vAxis: {viewWindow: {min: 0, max: .5}, format: '0.0', title: 'Stock Market Valuation Index'},
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

# Stock Market Valuation Index

<div id="mv2018" style="margin-top:0px"></div>
<br>
<div id="mv" style="margin-top:0px"></div>