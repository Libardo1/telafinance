title: Considerations for model validation
slug: model-validation-considerations
category: post
date: 2018-08-17
modified: 2018-08-17
newsletter: False
meta:  An introduction to model validation, a critical aspect of the risk management framework.
headerimage: /img/model-validation/Validation.png
headeralt: Model Validation

Model validation is as critical to the <a href="/blog/understanding-the-model-lifecycle.html">model lifecycle</a> as development and maintenance. This article covers some considerations a model validator should consider when assessing a model's performance and risk including development process, overall soundness, and limitations.

<img src="/img/model-validation/Validation.png" width="100%" alt="Validation Icons" class="technical-diagram">

## 1. Introduction

Models are used for business decision-making, financial forecasting, and accounting purposes. The use of models introduces model risk. Model risk is mitigated through a model risk management framework, in which validation plays a critical role.

<p>

The goal of validation, in the broadest sense, is to legitimize bank processes and, in particular, the models that are part of those processes.

<p>

Model validation is a disciplined approach to assessing a model's development, soundness, and limitations. Validation provides an independent review and effective challenge to the methodologies used by a modeling team. It is a  powerful tool in the management of model risk and an essential function of any risk department.

<p>

To give a general overview of the validation process, we will consider three review focuses of a typical validation: development, soundness, limitations.

</p>

## 2. Development

The first effort of a model validation exercise is the reconstruction of a model. This should be done using only development data and documentation. It is essential to a model's continuity that it can be fully understood and developed without the input of the modeling team. This step can be ensured by creating a firewall between validation and modeling teams whereby compliance would deliver the modeling materials to validation. 
<p>
Nearly every model has documentation failures and it is important for validation to assess a model's ability to stand on its own. Any step of the modeling process that cannot be readily understood, recreated, or rationalized can be documented as a validation finding.

</p>

### 2.1. Data
Reviewing the data component of a model involves reproducing the original data set and confirming its proper application. No matter how good a model is, bad input will never produce good output. Confirming a data source, whether it is internal or external, is the first step to verifying a model's results.
<p>
Other components of a data review include error detection, variable reconstruction, and calculation consistency.
</p>
### 2.2. Process Verification
A validator should follow documentation and verify that the actual processing of the model operates as prescribed. Any gaps in a model's operation or steps that involved some degree of judgement that are not documented should be identified. Documentation should capture a modeler's thought process and decision making and allow a reader to not only understand but also to challenge. A model is not created in the absence of judgement but because of it. An inquiry into these judgements is key to a validation.

## 3. Soundness

In this phase of model review, a validator, after reconstructing and understanding the model as prescribed by the modeler, will review the overall conceptual soundness of the process. This includes an assessment of key assumptions or presuppositions made by  the modeler and their reasonableness. It is critical to identify the key components of a model on which the development relies. By identifying the critical elements, a validator can determine their performance tolerance and the model's implied functionality constraints.

### 3.1. Assumptions
Assumptions should be well documented so a validator can determine their reasonableness and impact. Some assumptions are explicit such as management assuming interest rates will stay flat and are part of the framework a model was intended to operate in. These assumptions should be examined but may also be part of a conscious strategy required by stakeholders. Other assumptions may be implicit, such as using a formula for call-put parity. Using a formula implies the formula is correct and will hold, when the reality is financial markets do not obey scientific laws. In addition, these formulas may be built on assumptions of their own. It is important to identify and assess as many layers of these assumptions as possible.

### 3.2. Design
The methodology used by a developer may be subjective and open to challenge. Assessing the design is not asking whether the model is right but whether it is the right model. There are often multiple approaches to a problem and each may have its own merits and weaknesses. Considering alternatives and benchmarking them to a champion model can legitimize subjective modeling decisions.

## 4. Limitations

Given a validation team's acceptance of a model's reasonability and intended use, the final phase of a validation involves the review of a model's breaking points. This can be done through tools such as sensitivity analysis, benchmarking, assumption testing, and the development of additional and comparable challenger models.

<p>

It is important for a validator to define boundaries in which a model may no longer function as intended to provide guidance to senior management on scenarios in which a reconsideration of model outputs would be prudent. This kind of assessment is common practice in many fields in which a prescribed solution (in this case a model) comes with an extensive list of use-cases, caveats, and warnings.

</p>

### 4.1. Stress Testing
Key assumptions and model inputs should be tested for performance when subject to abnormal behavior such as values outside of historical record, volatility greater and less than usual, and several standard deviations of change. Understanding a model's performance record when input conditions show extreme or otherwise unusual activity gives both insight into the model's mechanics but also boundaries of environment use. With reverse stress testing, a stress condition is pushed to the point of either a model breaking, an impossible result, or a business-defined unacceptable output.

### 4.2. Scenario Analysis
Some models may not work in adverse market conditions, which is often when they are needed most. Determining environmental behaviors that may limit or falsify model results is imperative for a model user and management. Models may work for long periods of time and may have a proven track record but encounter a condition that was unforeseen by a developer, such as negative interest rates or a spike in the TED spread. Identifying scenarios and developing warning indicators can mitigate unexpected or misleading output.

## 5. Conclusion

Model validation is a value-added exercise when implemented properly. Merely the existence of an independent challenge can improve the development standards for models. Validation, through a discovery process, can generate key findings that will improve the robustness of a model and provide management with a deeper understanding of the model's effectiveness, legitimizing the modeling process and results. Given the sharp costs associated with model risk management failures, model validation can provide an effective hedge to these types of losses in the overall risk governance framework.

<p>

The aforementioned guidance is merely an introduction and each model should be treated on an individualized basis. A validator, just like a modeler, should approach the problem at hand and consider both the analysis tools at their disposal and prior experience when scrutinizing a process. The financial world is not bound by scientific laws but rather social dynamics that may behave in unexpected and illogical ways. Thus, a purely automated one-size-fits-all approach to validation can miss the most important fat-tail risks that it ideally should be trying to mitigate in the first place.

<p>

As with most things in life, the quality of a validation depends on the quality of the work put into it. Model risk can be managed to a finer degree when the right resources and right people are allocated to a job. Management can expect stronger, more robust, and better understood models with more credible results when validation is undertaken properly.

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