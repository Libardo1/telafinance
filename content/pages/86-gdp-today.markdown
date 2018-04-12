title: GDPToday
category: page
slug: gdptoday
sortorder: 0502
toc: True
sidebartitle: &nbsp; 5.1 GDPToday
meta: Bankcasting's daily tracker for GDP

<script src="http://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
<script src="js/jquery.csv.min.js"></script>
<script type="text/javascript" src="http://www.google.com/jsapi"></script>

<script type="text/javascript"> // load the visualisation API
  google.load('visualization', '1', { packages: ['corechart', 'controls'] });
</script>
<script type="text/javascript">
function drawVisualization() {
   $.get("data/ifr.csv?q="+Math.random(), function(csvString) {
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
            title: 'Bankcasting 2018Q1 GDP Daily Estimate',
            legend: 'bottom',
            titleTextStyle : {color: 'black', fontSize: 20},
            vAxis: {viewWindow: {min: 0, max: 3.2}, format: '0.0', title: 'Annualized Growth Rate (%)'},
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

&#8729; GDPToday provides forecasted estimates for upcoming official GDP releases from the Bureau of Economic Analysis

&#8729; The forecast is updated every weekday that does not fall on a holiday

&#8729; The official first estimate for 2018Q1 GDP from the BEA will be released on April 27, 2018. <!--The current annualized estimate for 2018Q1 GDP as of March 29, 2018 is +2.63%. The current three-year forecast for GDP is +7.61%. The current three-year severe forecast for GDP is -4.98%. -->

---

<div id="crt_ertdlyYY" style="margin-top:-10px"></div>
<br>
<!--
<img src="/img/GDPToday/GDPToday3Year.PNG" width="100%" alt="Latest GDPToday Three-year Forecast" class="technical-diagram">
<img src="/img/GDPToday/GDPToday.PNG" width="100%" alt="Latest GDPToday Forecast" class="technical-diagram">
-->


For any questions, comments, or inquiries related to this topic or any other on this site please reach out to: contact@bankcasting.com

<!-- Begin MailChimp Signup Form -->
<link href="//cdn-images.mailchimp.com/embedcode/horizontal-slim-10_7.css" rel="stylesheet" type="text/css">
<style type="text/css">
	#mc_embed_signup{background:#fff; clear:left; font:14px Helvetica,Arial,sans-serif; width:100%;}
	/* Add your own MailChimp form style overrides in your site stylesheet or in this style block.
	   We recommend moving this block and the preceding CSS link to the HEAD of your HTML file. */
</style>
<div id="mc_embed_signup">
<form action="https://bankcasting.us17.list-manage.com/subscribe/post?u=b3b11f090db9e2871e474b005&amp;id=204a12fade" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank" novalidate>
    <div id="mc_embed_signup_scroll">
	<label for="mce-EMAIL">Want to learn more? Bankcasting Insights. Just one email each week.</label>
	<input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_b3b11f090db9e2871e474b005_204a12fade" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>

<!--End mc_embed_signup-->