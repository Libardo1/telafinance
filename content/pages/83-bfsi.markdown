title: Bankcasting Financial Stress Index
category: page
slug: bfsi
sortorder: 0203
toc: True
sidebartitle: &nbsp; Financial Stress Index
meta: Bankcasting's Financial Stress Index

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
            title: 'Bankcasting Financial Stress Index',
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

# Bankcasting Financial Stress Index

<div id="bfsi2018" style="margin-top:0px"></div>
<br>
<div id="bfsi" style="margin-top:0px"></div>
<br>

For any questions, comments, or inquiries related to this topic or any other on this site please reach out to: contact@bankcasting.com