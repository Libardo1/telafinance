title: Tela Indicators
category: page
slug: indicators
sortorder: 0104
toc: True
sidebartitle: Indicator Index
meta: Index for all indicators developed and tracked by Tela

# Indicators

<script src="http://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
<script src="js/jquery.csv.min.js"></script>
<script type="text/javascript" src="http://www.google.com/jsapi"></script>

<script type="text/javascript"> // load the visualisation API
  google.load('visualization', '1', { packages: ['corechart', 'controls'] });
</script>

<script type="text/javascript">
function drawVisualization() {
   $.get("data/fsi2018.csv?q="+Math.random(), function(csvString) {
      var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
      var data = new google.visualization.arrayToDataTable(arrayData);
      var chartwidth = $('#chartparent').width();
      var fsi2018 = new google.visualization.ChartWrapper({
         chartType: 'LineChart',
         containerId: 'fsi2018',
         dataTable: data,
         options:{
            width: chartwidth, height: 450,
            chartArea: {'width': '75%','height': '80%',top:20},
            legend: 'bottom',
            vAxis: {viewWindow: {min: 0, max: .75}, format: '0.00', title: 'Financial Stress Index'},
            series: {
               0: { color: '#529ecc' }
            }
         }
      });
      fsi2018.draw();
   });
}
google.setOnLoadCallback(drawVisualization)
</script>

###<a href="/fsi.html">Tela Financial Stress Index (2018 YTD)</a>
<div id="fsi2018" style="margin-top:0px"></div>