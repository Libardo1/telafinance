title: Model Lifecycle
category: page
slug: model-lifecycle
sortorder: 0402
toc: True
sidebartitle: &nbsp; Model Lifecycle
meta: The phases of a model lifecycle including development, documentation, validation, monitoring, maintenance, and audit.

# Understanding the model lifecycle is critical for developers

---
<p>
&#8729; Analysts typically focus on model development and use
<p>
&#8729; These phases are important but represent just a small portion of a broader lifecycle
<p>
&#8729; Practitioners who understand their roles and interconnected responsibilities within the greater model lifecycle can facilitate the overall mitigation of model risk 
---
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

Development is often the longest and most risk-prone step of the model process. It covers the inception of the model from business need to output results. It is here that a developer will take an idea and build a framework that takes input and produces one or more outputs – for example, a valuation model for a bond, where the inputs are face value, yield, coupon, and maturity and the output is present value. Development is the step on which all subsequent phases depend to assess the risks of known unknowns and, the much trickier, unknown unknowns.

## Documentation
Documentation provides the bridge between the first and second lines of risk defense. A model developer (first line) creates documentation for a model and provides it to a validator (second line) for an independent assessment. Documentation should provide the validator with all the information necessary to use, decompose, examine, and test a model. Therefore, it should be complete enough to minimize or remove all interaction between the two parties to ensure objectivity and independence. A governance framework may establish a firewall between the groups to assess a model’s ability to stand independent of its owner.

## Validation
As stated in the previous phase, validation comprises the independent assessment of a model. Here a model is reviewed for technique, conceptual soundness, and robustness. Common tests used by a validator to arrive at an informed opinion of a model’s fitness include benchmarking, stress testing, and back testing. For more thoughts on validation, please see <a href="model-validation.html">“Three things every validator should consider."</a>

## Monitoring
This phase depends on the frequency of new model outputs. With a daily VaR model, monitoring results is likely part of the process of communicating the results each day to management. For example, today our value at risk was X and we breached our limit by Y and this is the Nth time the limit has been breached in M periods. That example gives management three monitored values in addition to the model output in which to contextualize the result.

In another example, a yearly regulatory capital stress test will only produce output once a year. Therefore, the models may be updated on a quarterly or monthly basis to assess the interim results to create a more continuous process that will alleviate the model adjustment work and ongoing development required by the yearly live stress test.

## Maintenance

Maintenance is often lumped together with monitoring but it should be considered a separate phase as it defines the model change process which may or may not be initiated due to monitored results. Model limits should be determined prior to production with clearly defined scenarios for model maintenance. Using the VaR example, the model may define a maintenance limit in the case where a 95% confidence limit is breached more than 20 times per year. In this case, the model is expected to produce results outside of a confidence interval 5 out of every 100 runs. If we assume 252 trading days each year, we would expect 12.6 breaches in a given year. Therefore, 20 breaches indicate a statistical likelihood threshold that the model is performing outside of its pre-defined expected behavior and may require maintenance. This maintenance, if materially beneficial to the model performance, may lead to a model change. It is important to note that any model changes made during this phase require some level of re-validation, either on the whole or specifically for the changes depending on change materiality as defined by the policy.

## Audit

An internal audit function is considered the third line of defense. Audit provides a second layer of independent review to the model lifecycle process. It is the function of an audit team to assess the actual reality of the steps taken in the lifecycle compared to the overall governance, guidance in policies and procedures, and controls. Audit findings can include lack of control evidence, inadequate documentation, or process failures. For example, a model control log may define a model output review by a superior to ensure quality. This control may lack proper documentation, in the case where a review did take place but the action was not formally noted. It may also lack sufficient evidence, in the case where a review took place, the action was formally documented, but the work provided by the reviewer does not provide rationale detailed enough for an independent assessment of that review. In another example, a process failure would take the form of a review that is documented to have taken place but when cross-checked by the reviewer is determined to have not taken place. Obviously, the last case represents the most serious of the three examples, which would demand a more detailed investigation into the cause and failure of the process.

## A Continuous Process

Modeling is an on-going process subject to continuous change. Models can and must be improved over time to ensure a lifetime of proper functionality. The risks of model failure are well documented and proper resources should be allocated to support their lifecycle needs to mitigate these risks. All aspects of the lifecycle are subject to regulatory scrutiny, which provides an additional layer of independent review outside of the model’s organization. The guidance here represents merely a simple starting framework that can be expanded to meet the unique needs and challenges of an institution. Managing model risk should not be thought of as a one-time review or fix but rather an ongoing process critical to standard business functions.


For any questions, comments, or inquiries related to this topic or any other on this site please reach out to: contact@bankcasting.com