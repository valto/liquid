# Capability Economics

**Definition.** Compare feasible ways of fulfilling a capability by the risk-adjusted cumulative net value they deliver over time, including their full lifecycle and the flexibility they retain or remove.

Conceptual source: **Valto Loikkanen**, *Liquid Software: The Economics of Execution*, versions 2.0 and 3.0, 27 November 2026. This proposed revision incorporates the expanded v3 source. The explanation, models and examples are AI-assisted elaborations, with supplied v3 scenarios identified separately. They are proposals for measurement, not empirical validation of the framework.

## Begin with the outcome

Specify the need, its beneficiary, accepted results, quality, latency, reliability, safety and authority. A path outside these boundaries is infeasible even if its runtime price is attractive. Some capabilities require a deterministic control or a validated process before first use. Others can be fulfilled using existing tools and intelligent execution while the need is still being understood.

Compare direct agents, existing software or SaaS, reusable skills, deterministic functions, modules, dedicated applications and hybrids. Include a feasible manual path or doing nothing when either is a real alternative. Intelligence itself has enabling costs: permissions, context, tools, evaluation, runtime setup and human supervision.

The useful unit is the capability or meaningful contract. Internal operations can use different realizations without becoming independent promises. CRD's capability/realization separation supplies a documentation approach; it does not prove the economics of any particular implementation.

## Compare value over the relevant horizon

A simple accounting model makes the comparison explicit:

```text
NetValue(r, scenario) =
    discounted value actually delivered over the horizon
  − enabling, building, operating, assuring and maintaining costs
  − adaptation, transition, restoration and retirement costs
  − attributable failure and rigidity losses not already counted
```

Here `r` is a candidate realization or sequence of realizations. Select among feasible candidates using plausible demand and failure scenarios, the principal's risk tolerance and required commitments. An expected value alone may conceal an unacceptable downside; explicit constraints remain part of selection.

Time matters because a benefit received later may be worth less, arrive after a market window, or never occur. A delayed benefit already absent from the value term must not be subtracted again as opportunity cost. Likewise, avoid counting failure losses both through an unsuccessful scenario and a second blanket risk deduction. Account consistently for scarce people, capital and existing resources; sunk expenditure is distinct from avoidable future cost.

Minimum cost is an adequate objective only when outcomes, timing and relevant risks are comparable. Where benefits differ, choose on net value. The v2 page 6 least-cost wording therefore needs the outcome comparability established on its page 3; v3 makes the net-value objective explicit throughout.

## Make scenarios and timing explicit

V3 page 25 proposes an expected discounted-value objective. Using different variable names to distinguish a strategy from a discount rate:

```text
V(j) = sum over scenarios s of p(s) ×
       sum over periods t of [B(j,s,t) − C(j,s,t) − L(j,s,t)] / (1 + d)^t
```

`j` is a feasible realization or staged strategy; `p(s)` is a scenario probability, with the probabilities summing to one. `B` is attributable benefit, `C` is full incremental lifecycle and transition cost, and `L` is failure or rigidity loss not already represented in the other terms. `d` is the discount rate for the chosen period. State the horizon, timing, units and any residual value consistently. This is an accounting proposal rather than an implemented optimizer.

Compare serving now and specializing later with building first, retaining existing tools and other feasible sequences. Demand observed at one stage can change a later decision. A staged strategy must have a safe initial path and an acceptable transition; it cannot assume those prerequisites away. Average expected value does not excuse unacceptable severe downside. Unknown probabilities and flexibility costs may need ranges, qualitative judgments or hard constraints rather than invented precision.

Serving a need before committing to construction can preserve options to defer, expand, alter or abandon the investment. Waiting can also forfeit value or violate a requirement. The benefit of this evidence-first sequence is conditional, and neither delay nor initial agentic fulfillment is always preferable.

## A hypothetical example: value during development

The following dollar example was developed for the v2-derived explanation. It is distinct from the supplied v3 euro example that follows.

Assume a service produces $100 of value per active day. An agent path needs $100 of setup and costs $20 per active day, starting on day 1. A dedicated implementation costs $3,000 to build, becomes available after 40 days and costs $2 per active day. Both deliver equal accepted quality. Demand lasts 90 days.

For this illustration only, ignore discounting and uncertainty. Treat the stated costs as complete for the horizon, with no separate retirement expenditure or residual value. In the hybrid, development can run in parallel with the agent service without extra shared-resource costs. These assumptions are deliberately simple and are not measured performance or market prices.

| Path | Value delivered | Total cost | Net value over 90 days |
| --- | ---: | ---: | ---: |
| Agent throughout | $9,000 | $100 + 90 × $20 = $1,900 | $7,100 |
| Wait for software, then operate for 50 days | $5,000 | $3,000 + 50 × $2 = $3,100 | $1,900 |
| Agent for 40 days, then software for 50 | $9,000 | $100 + 40 × $20 + $3,000 + 50 × $2 = $4,000 | $5,000 |

In these assumptions, the agent path has the greatest net value. The hybrid delivers the same benefit sooner than waiting for software, but its 50 days of runtime savings do not recover the build cost. For a longer unchanged horizon `H`, the hybrid gains `$18 × (H − 40) − $3,000` relative to the agent path. It becomes preferable after roughly 207 days if all other assumptions remain true. Different demand, quality, build costs or delivery dates can reverse the result.

This example shows why lower per-execution cost does not settle the decision. It also shows that early intelligent execution does not automatically justify subsequent materialization.

## The supplied v3 example: identical software, different timing

V3 page 15 assumes both paths build the same €12,000 module over three months, paying the investment at the start. From month four, each generates €5,000 monthly contribution at €500 monthly operating cost. In the alternative path, an existing agent environment also serves the first three months, generating €4,000 monthly contribution at €1,500 operating and assurance cost.

| First six months | Software-first | Agent-first, then the same module |
| --- | ---: | ---: |
| Initial construction | −€12,000 | −€12,000 |
| Net operations in months 1–3 | €0 | €7,500 |
| Net operations in months 4–6 | €13,500 | €13,500 |
| Cumulative net value | **€1,500** | **€9,000** |

The €7,500 difference persists after both use the same software under these assumptions. The example excludes discounting and other costs, and assumes parallel fulfillment and development are feasible. It illustrates timing rather than measured agent performance or a universally optimal sequence. Early execution can be too expensive or unreliable, and observed demand might instead eliminate the later build.

Record actual attributable contribution. Hours released are not cash until converted into avoided expenditure, profitable throughput or another defined benefit. Positive discounting lowers the present value of fixed future benefits; receiving them earlier can improve value relative to receiving them later. It does not increase their value above the same undiscounted amount. Opportunity cost concerns the best feasible alternative forgone, not the sum of every imagined opportunity.

## Use break-even as a limited check

If incremental fixed software cost is `F`, the agent cost per successful execution is `a`, and software cost is `s`, the elementary cost threshold is:

```text
N = F / (a − s), when a > s
```

If `a ≤ s` and `F` is positive, this particular runtime-saving argument gives no finite break-even point. Other benefits can still justify the software.

The formula assumes comparable outcomes and ignores timing, variable demand, changing prices, failures, maintenance, transition and residual value. Count successful accepted executions and their actual retries and supervision, rather than treating token price as the whole cost. Replace the elementary threshold with a fuller scenario comparison when those omitted factors matter.

V3 pages 10 and 17 illustrate `F = €1,200` and `s = €0.10`. Agent costs of €2.50, €1.30 and €0.50 imply thresholds of 500, 1,000 and 3,000 respectively. Reducing software-production cost moves the comparison as well. These are hypothetical inputs, not predictions. A history of 500 executions is not a build trigger: decide using remaining demand and incremental future investment. Construction already paid for is sunk and must not be charged again when comparing future operation.

## Keep the continuum reversible

Direct execution, skills, deterministic functions, modules and applications can coexist in one capability. Movement toward dedicated software is not a required maturity progression. A small validated function may be the best long-term realization; a changing activity may remain agentic; a high-utilization service may justify a dedicated application from the outset.

Materialization fixes assumptions about workflow, information, interaction and rules. It can improve speed and assurance while closing alternatives. Compare that flexibility loss with the benefit gained. Expose functions where useful, retain a permitted fallback when a commitment requires one, and preserve accepted meaning when implementations change.

The earlier v2-derived explanation used **maturity bias** for treating implementation level as evidence of decision quality. V3 page 26 gives a broader formulation: current understanding and experience can limit the alternatives a decision-maker perceives. The revision below uses that source-attributed formulation while retaining the earlier warning. Neither concern makes agent use a proxy for decision quality.

## Recognize alternatives before choosing among them

V3 page 26 separates three dimensions of maturity:

| Dimension | Question |
| --- | --- |
| Understanding | Which operating paradigms and possible realizations does the decision-maker recognize? |
| Experience | Which alternatives have been tried enough to reveal their practical capabilities and limits? |
| Implementation | Which realization is actually selected for this capability? |

Its spectrum describes traditional software, AI-enabled software, agentic software, agent-first operations and AI-native operations, with unknown further paradigms explicitly left open. It is a conceptual classification rather than a validated assessment scale.

Broader understanding can lead to deliberate conventional software use. The same visible implementation can reflect informed selection or lack of awareness of alternatives. Seek practical evidence where useful and revisit assumptions; do not infer decision quality from how many agents are present. Retain durable knowledge and records when workers are instantiated or discarded. The separate named maturity paper remains unavailable to this review.

## Include adoption and reversal

An implementation can consume resources without delivering its promised value. Introducing it can require training, migration, testing and process changes. Returning to the earlier system can require a second transition, reconciliation and restoration. This is **double transition cost**, a possible exposure to examine rather than a standard multiplier to add to every budget.

The source's Pendo, GAO and UK examples concern distinct measures and populations. Underused features are not necessarily unnecessary: infrequent critical or seasonal functions may be valuable. Projects missing a cash-savings target may still provide security or other benefits. Qualitative reversal reports establish possible mechanisms, not their prevalence. None establishes a universal failure rate or proves that an agentic replacement would have succeeded.

## Apply the same reasoning to information processing

Preserving a source and preprocessing every possible interpretation are separate investments. Appropriate capture can retain future options without immediately generating every summary, index, graph or embedding.

Select among processing on retrieval, caching a useful result, preprocessing a recurring category and broader preprocessing. Include the cost of discovery, permissions, minimum metadata, freshness checks, invalidation and rebuilding. Some of this work is necessary before retrieval can be safe or practical. Demand-driven processing requires enough source discoverability to learn what is being requested.

A disposable derived structure does not change canonical source authority. Retiring it does not authorize deleting the original or pending work. Storage, privacy, retention and access commitments remain part of the feasible boundary.

Modularity can extend the comparison to models, processing and infrastructure. Count interface, integration, coordination, testing and observability overhead. Owned hardware can reduce one marginal price while adding utilization and lifecycle costs. A vendor's architectural claim needs a comparable measured workload before it supports a cost advantage.

V3 page 23 assumes €1,300 for full extraction and horizon upkeep, €0.01 per preprocessed retrieval and €0.20 per on-demand extraction. Both paths already have equivalent basic indexing and access controls. On-demand costs €200 at 1,000 retrievals, against €1,310 for preprocessing. At 10,000, the totals are €2,000 and €1,400. The continuous crossover is `1,300 / 0.19 = 6,842.105…`; preprocessing first costs less at **6,843 whole retrievals**. The source's approximately 6,842 is rounded, and its original text remains intact.

Count retrieval events separately from distinct documents. Repeated access may justify selective caching instead of full extraction. Include freshness, discovery, validation and access obligations consistently; the example does not establish that scanning raw archives on each request is efficient. Accessibility, searchability, compliance or response-time commitments can justify preparation before observed demand.

## Compose at the meaningful capability boundary

The procurement example on v3 page 21 combines a reasoning model to clarify need, a validated local model for field extraction, declared rules for policy, an exact calculation function, an authorized existing API for commitment and an authoritative evidence record. A human with the required authority handles exceptions or approves a commitment where necessary. Each replacement must satisfy its contract and governing permissions; a capability description alone grants neither spending rights nor deployment authority.

Reuse can justify specialization across different activities. V3 page 28 assumes a shared calculation used 6,000 times, costing €0.40 per agent execution or €900 fixed plus €0.02 per function execution. The totals are €2,400 and €1,020, a €1,380 saving. At 1,000 uses, €400 versus €920 does not justify a new function on this cost comparison. Its custom-request and reconciliation examples illustrate different compositions; they do not supply enough comparative data to establish an entire portfolio optimum.

Choose a meaningful unit of purpose and contract, rather than the smallest possible code fragment. Interface, versioning, discovery and dependency overhead can outweigh reuse. Compare attributable owned-model capacity with hosted execution over actual utilization, assurance and maintenance. Idle capacity is not universally free, and local placement alone does not establish privacy or reliability.

## A measurable operating loop

1. Define the capability, commitments, beneficiaries and relevant horizon.
2. Identify existing resources and feasible agentic, software, manual and hybrid paths.
3. Execute where feasible and record accepted outcomes, time, actual cost and exceptions.
4. Compare full net value and plausible demand, failure and transition scenarios.
5. Materialize selectively when the evidence justifies the investment.
6. Reassess changed needs, prices and constraints; retain, evolve or retire the realization within authority.

Evaluation should test the claim that one sequence improves fulfillment. Measure elapsed time to first accepted value, quality, successful-execution cost, cumulative benefit, implementation and restoration expenditure, and meaningful exceptions. Compare with existing tools as well as new agent paths. Keep measurement periods and demand assumptions explicit.

A useful experiment can fail: no feasible direct path may exist, demand may not repay specialization, or coordination overhead may exceed savings. Reporting such results improves selection rather than invalidating stable software as a legitimate choice.

## Keep a practical decision record

V3 page 27 proposes a lightweight record. Capture the capability identity and version, accountable owner, required outcome and acceptance criteria, existing baseline, feasible alternatives, observed and forecast demand, quality and full cost evidence, selected strategy, governing authority, review triggers and recovery path. Separate observations from estimates, and explain important unknowns rather than supplying arbitrary probabilities.

A compact [decision-record template](https://valto.github.io/liquid/concepts/capability-economics/decision-record/) with [editable Markdown](https://valto.github.io/liquid/content/concepts/capability-decision-record.md) turns this into a reviewable business case. It is optional documentation, not a new CRD schema or authority grant.

The optimizer itself has lifecycle costs. Revisit a decision when demand, quality, prices, exceptions, commitments or source evidence change materially. Retain a stable realization when new generation and assessment would cost more than the likely improvement. Permission to propose a change is distinct from permission to deploy, transfer data, purchase or withdraw a service. Measure accepted value and avoided waste rather than rewarding application or agent production.

## Read further

Read the [complete economics paper and reference audit](https://valto.github.io/liquid/whitepapers/economics-of-execution/). Related research drafts develop [intelligence-first sequencing](https://valto.github.io/liquid/whitepapers/drafts/02-intelligence-first-software-second/), [Liquid Software](https://valto.github.io/liquid/whitepapers/drafts/04-liquid-software/), [self-optimization](https://valto.github.io/liquid/whitepapers/drafts/08-the-self-optimizing-information-system/) and [implementation lifecycles](https://valto.github.io/liquid/whitepapers/drafts/12-the-lifecycle-of-liquid-software/).

The supplied economics v2 and [complete v3 paper](https://valto.github.io/liquid/whitepapers/economics-of-execution/v3/) are this revision's conceptual sources. The earlier economics v1 and separate named AI-maturity companion were not supplied or read; the substantive maturity chapter within v3 was read in full.
