title: Understanding the Model Lifecycle
slug: understanding-the-model-lifecycle
category: post
date: 2018-07-27
modified: 2018-07-27
newsletter: False
meta: The phases of a model lifecycle including development, documentation, validation, monitoring, maintenance, and audit.
headerimage: /img/model-lifecycle/ModelLifecycle.PNG
headeralt: Model Lifecycle

Analysts typically focus on model development and use. These phases are important but represent just a small portion of a broader lifecycle. Practitioners who understand their roles and interconnected responsibilities within the greater model lifecycle can facilitate the overall mitigation of model risk.

<img src="/img/model-lifecycle/ModelLifecycle.PNG" width="100%" alt="Model Lifecycle" class="technical-diagram">

## Introduction

Models are used in almost every area of finance. In simple terms, if a process can't be reproduced with a four-function calculator - it's probably using a model.

Technically (and in boring regulatory speak), a model is defined by SR 11-7 as <q>a quantitative method, system, or approach that applies statistical, economic, financial, or mathematical theories, techniques, and assumptions to process input data into quantitative estimates ... and quantitative approaches whose inputs are partially or wholly quantitative or based on expert judgement, provided that the output is quantitative in nature.</q>

Models are essential tools for almost all financial functions but their use introduces model risk. To mitigate this risk, a model should go through several stages of independent review and analysis. These stages are not one-time incidents but rather parts of a continuous lifecycle as a model changes through time in its application or sophistication.

A detailed and defined understanding of the model lifecycle is a critical first step in the model risk management process. In general, this lifecycle will cover the following six phases&colon;

1. Development&semi;
2. Documentation&semi;
3. Validation&semi;
4. Monitoring&semi;
5. Maintenance&semi; and
6. Audit.

Each phase should have its own processes and procedures to ensure developers have both guidance and an ability to benchmark their actions to approved policy governance. A brief description of each phase is presented below.

## Development

Development is often the longest and most risk-prone step of the model process. It covers the inception of the model from business need to output results. It is here that a developer will take an idea and build a framework that takes input and produces on or more outputs - for example, a valuation model for a bond, where the inputs are face value, yield, coupon, and maturity and the output is present value. Development is the step on which all subsequent phases depend to assess the risks of the known unknowns and, the much tricker, unknown unknowns.

## Documentation

Documentation provides the bridge between the first and second lines of risk defense. A model developer (first line) creates documentation for a model and provides it to a validator (second line) for an independent assessment. Documentation should provide the validator with all the information necessary to use, decompose, examine, and test a model. Therefore, it should be complete enough to minimize or remove all interaction between the two parties to ensure objectivity and independence. A governance framework may establish a firewall between the groups to assess a model's ability to stand independent of its owner.

## Validation

As stated in the previous phase, validation comprises the independent assessment of a model. Here a model is reviewed for technique, conceptual soundness, and robustness. Common tests used by a validator to arrive at an informed opinion of a model's fitness include benchmarking, stress testing, and back testing. <!-- For more thoughts on validation, please see <a href="model-validation.html">"Three things every validator should consider."</a> -->

## Monitoring

This phase depends on the frequency of new model outputs. With a daily VaR model, monitoring results is likely part of the process of communicating the results each day to management. For example, today our value at risk was X and we breached our limit by Y and this is the Nth time the limit has been breached in M periods. That example gives management three monitored values in addition to the model output in which to contextualize the result.

In another example, a yearly regulatory capital stess tests will only produce output once a year. Therefore, the models may be updated on a quarterly or monthly basis to assess the interim results to create a more continuous process that will alleviate the model adjustment work and ongoign development required by the yearly live stress test.

## Maintenance

Maintenance is often lumped together with monitoring but it should be considered a separate phase as it defines the model change process which may or may not be initiated due to monitored results. Model limits should be determined prior to production with clearly defined scenarios for model maintenance. Using the VaR example, the model may define a maintenance limit in the case where a 95% confidence limit is breached more than 20 times per year. In this case, the model is expected to produce results outside of a confidence interval 5 out of every 100 runs. If we assume 252 trading days each year, we would expect 12.6 breaches in a given year. Therefore, 20 breaches indicate a statistical likelihood threshold that the model is performing outside of its pre-defined expected behavior and may require maintenance. This maintenance, if materially beneficial to the model performance, may lead to a model change. It is important to note that any model changes made during this phase require some level of re-validation, either on the whole or specifically for the changes depending on change materiality as defined by the policy.

## Audit

An internal audit function is considered the third line of defense. Audit provides a second layer of independent review to the model lifecycle process. It is the function of an audit team to assess the actual reality of the steps taken in the lifecycle compared to the overall governance, guidance in policies and procedures, and controls. Audit findings can include lack of control evidence, inadequate documentation, or process failures. For example, a model control log may define a model output review by a superior to ensure quality. This control may lack proper documentation, in the case where a review did take place but the action was not formally noted. It may also lack sufficient evidence, in the case where a review took place, the action was formally documented, but the work provided by the reviewer does not provide rationale detailed enough for an independent assessment of that review. In another example, a process failure would tale the form of a review that is documented to have taken place but when cross-checked by the reviewer is determined to have not taken place. Obviously, the last case represents the most serious of the three examples, which would demand a more detailed investigation into the cause and failure of the process.

## A Continuous Process

Modeling is an on-going process subject to continuous change. Models can and must be improved over time to ensure a lifetime of proper functionality. The risks of model failure are well documented and proper resources should be allocated to support their lifecycle needs to mitigate these risks. All aspects of the lifecycle are subject to regulatory scrutiny, which provides an additional layer of independent review outside of the model's organization. The guidance here represents merely a simple starting framework that can be expanded to meet the unique needs and challenges of an institution. Managing model risk should not be thought of as a one-time review or fix but rather an ongoing process critical to standard business functions.

<hr>

For any questions, comments, or inquiries related to this article or any other on this site please reach out to: contact@telafinance.com

<hr>

<!--<h3>Related To</h3>-->
<div class="row">
    <div class="col-md-4">
        <div class="well select-next">
<a href="/blog/chinas-rise-in-gdp.html" class="btn btn-success btn-full"><svg width="28" height="30" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg"><path d="M640 896v512h-256v-512h256zm384-512v1024h-256v-1024h256zm1024 1152v128h-2048v-1536h128v1408h1920zm-640-896v768h-256v-768h256zm384-384v1152h-256v-1152h256z" fill="#fff"/></svg></a>
<p class="under-btn">Analyzing China's rise in GDP.</p>       </div>
    </div>
       
    <div class="col-md-4">
        <div class="well select-next">
<a href="/blog/can-you-hold-for-forty-years.html" class="btn btn-success btn-full"><svg width="28" height="30" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg"><path d="M1760 896q0 176-68.5 336t-184 275.5-275.5 184-336 68.5-336-68.5-275.5-184-184-275.5-68.5-336q0-213 97-398.5t265-305.5 374-151v228q-221 45-366.5 221t-145.5 406q0 130 51 248.5t136.5 204 204 136.5 248.5 51 248.5-51 204-136.5 136.5-204 51-248.5q0-230-145.5-406t-366.5-221v-228q206 31 374 151t265 305.5 97 398.5z" fill="#fff"/></svg></a>
<p class="under-btn">A historical view of the Dow Jones Industrial Average.</p>        </div>
    </div>
    <div class="col-md-4">
        <div class="well select-next">
<a href="/blog.html" class="btn btn-success btn-full"><svg width="28" height="30" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg"><path d="M1591 1448q56 89 21.5 152.5t-140.5 63.5h-1152q-106 0-140.5-63.5t21.5-152.5l503-793v-399h-64q-26 0-45-19t-19-45 19-45 45-19h512q26 0 45 19t19 45-19 45-45 19h-64v399zm-779-725l-272 429h712l-272-429-20-31v-436h-128v436z" fill="#fff"/></svg></a>
<p class="under-btn">The latest articles on Tela.</p>         </div>
    </div>
</div>

<hr>

<!-- Begin MailChimp Signup Form -->
<link href="//cdn-images.mailchimp.com/embedcode/horizontal-slim-10_7.css" rel="stylesheet" type="text/css">
<style type="text/css">
	#mc_embed_signup{background:#fff; clear:left; font:14px Helvetica,Arial,sans-serif; width:100%;}
	/* Add your own MailChimp form style overrides in your site stylesheet or in this style block.
	   We recommend moving this block and the preceding CSS link to the HEAD of your HTML file. */
</style>
<div id="mc_embed_signup">
<form action="https://telafinance.us17.list-manage.com/subscribe/post?u=b3b11f090db9e2871e474b005&amp;id=204a12fade" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank" novalidate>
    <div id="mc_embed_signup_scroll" align="center">
	<label for="mce-EMAIL">Join the Tela Insights Newsletter. Just one email each week.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
	<input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_b3b11f090db9e2871e474b005_204a12fade" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>

<!--End mc_embed_signup-->