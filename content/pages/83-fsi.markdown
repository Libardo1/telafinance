title: Tela Financial Stress Index
category: page
slug: fsi
sortorder: 0203
toc: True
sidebartitle: &nbsp; Financial Stress Index
meta: Tela's Financial Stress Index

<script src="http://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
<script src="js/jquery.csv.min.js"></script>
<script type="text/javascript" src="http://www.google.com/jsapi"></script>

<script type="text/javascript"> // load the visualisation API
  google.load('visualization', '1', { packages: ['corechart', 'controls'] });
</script>
<script type="text/javascript">
function drawVisualization() {
   $.get("data/bfsi.csv?q="+Math.random(), function(csvString) {
      var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
      var data = new google.visualization.arrayToDataTable(arrayData);
      var chartwidth = $('#chartparent').width();
      var bfsi = new google.visualization.ChartWrapper({
         chartType: 'LineChart',
         containerId: 'bfsi',
         dataTable: data,
         options:{
            width: chartwidth, height: 450,
            chartArea: {'width': '80%','height': '70%'},
            title: 'Tela Financial Stress Index',
            legend: 'bottom',
            titleTextStyle : {color: 'black', fontSize: 20},
            vAxis: {viewWindow: {min: -2, max: 4}, format: '0.0', title: 'Financial Stress Index'},
            series: {
               0: { color: '#529ecc' }
            }
         }
      });
      bfsi.draw();
   });
}
google.setOnLoadCallback(drawVisualization)
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
            chartArea: {'width': '80%','height': '70%'},
            title: 'Tela Financial Stress Index (2018)',
            legend: 'bottom',
            titleTextStyle : {color: 'black', fontSize: 20},
            vAxis: {viewWindow: {min: 0, max: .75}, format: '0.0', title: 'Financial Stress Index'},
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

# Tela Financial Stress Index

<div id="fsi2018" style="margin-top:0px"></div>
<br>
<div id="bfsi" style="margin-top:0px"></div>