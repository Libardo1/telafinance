title: Test
category: page
slug: test
sortorder: 0604
toc: False
sidebartitle: Test
meta: Test

# Test

<script src="http://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
<script src="js/jquery.csv.min.js"></script>
<script type="text/javascript" src="http://www.google.com/jsapi"></script>

<script type="text/javascript"> // load the visualisation API
  google.load('visualization', '1', { packages: ['corechart', 'controls'] });
</script>

<script type="text/javascript">
function drawVisualization() {
   $.get("data/ifr.csv", function(csvString) {
      // transform the CSV string into a 2-dimensional array
      var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
      // this new DataTable object holds all the data
      var data = new google.visualization.arrayToDataTable(arrayData);
      // CAPACITY - En-route ATFM delay - YY - CHART
      var chartwidth = $('#chartparent').width();
      var crt_ertdlyYY = new google.visualization.ChartWrapper({
         chartType: 'LineChart',
         containerId: 'crt_ertdlyYY',
         dataTable: data,
         options:{
            width: chartwidth, height: 450,
            title: 'Dow Jones',
            titleTextStyle : {color: 'grey', fontSize: 11},
         }
      });
      crt_ertdlyYY.draw();
   });
}

google.setOnLoadCallback(drawVisualization)
</script>

<div id="crt_ertdlyYY"></div>

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