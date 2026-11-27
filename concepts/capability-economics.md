# Capability Economics

**Definition.** Compare feasible ways of fulfilling a capability by the risk-adjusted cumulative net value they deliver over time, including their full lifecycle and the flexibility they retain or remove.

Conceptual source: **Valto Loikkanen**, *Liquid Software: The Economics of Execution*, version 2.0, 27 November 2026. This independently readable explanation, model and example are AI-assisted elaborations. They are proposals for measurement, not empirical validation of the framework.

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

Minimum cost is an adequate objective only when outcomes, timing and relevant risks are comparable. Where benefits differ, choose on net value. The page 6 least-cost wording in the source therefore needs the outcome comparability established on page 3.

## A hypothetical example: value during development

Assume a service produces $100 of value per active day. An agent path needs $100 of setup and costs $20 per active day, starting on day 1. A dedicated implementation costs $3,000 to build, becomes available after 40 days and costs $2 per active day. Both deliver equal accepted quality. Demand lasts 90 days.

For this illustration only, ignore discounting and uncertainty. Treat the stated costs as complete for the horizon, with no separate retirement expenditure or residual value. In the hybrid, development can run in parallel with the agent service without extra shared-resource costs. These assumptions are deliberately simple and are not measured performance or market prices.

| Path | Value delivered | Total cost | Net value over 90 days |
| --- | ---: | ---: | ---: |
| Agent throughout | $9,000 | $100 + 90 × $20 = $1,900 | $7,100 |
| Wait for software, then operate for 50 days | $5,000 | $3,000 + 50 × $2 = $3,100 | $1,900 |
| Agent for 40 days, then software for 50 | $9,000 | $100 + 40 × $20 + $3,000 + 50 × $2 = $4,000 | $5,000 |

In these assumptions, the agent path has the greatest net value. The hybrid delivers the same benefit sooner than waiting for software, but its 50 days of runtime savings do not recover the build cost. For a longer unchanged horizon `H`, the hybrid gains `$18 × (H − 40) − $3,000` relative to the agent path. It becomes preferable after roughly 207 days if all other assumptions remain true. Different demand, quality, build costs or delivery dates can reverse the result.

This example shows why lower per-execution cost does not settle the decision. It also shows that early intelligent execution does not automatically justify subsequent materialization.

## Use break-even as a limited check

If incremental fixed software cost is `F`, the agent cost per successful execution is `a`, and software cost is `s`, the elementary cost threshold is:

```text
N = F / (a − s), when a > s
```

If `a ≤ s` and `F` is positive, this particular runtime-saving argument gives no finite break-even point. Other benefits can still justify the software.

The formula assumes comparable outcomes and ignores timing, variable demand, changing prices, failures, maintenance, transition and residual value. Count successful accepted executions and their actual retries and supervision, rather than treating token price as the whole cost. Replace the elementary threshold with a fuller scenario comparison when those omitted factors matter.

## Keep the continuum reversible

Direct execution, skills, deterministic functions, modules and applications can coexist in one capability. Movement toward dedicated software is not a required maturity progression. A small validated function may be the best long-term realization; a changing activity may remain agentic; a high-utilization service may justify a dedicated application from the outset.

Materialization fixes assumptions about workflow, information, interaction and rules. It can improve speed and assurance while closing alternatives. Compare that flexibility loss with the benefit gained. Expose functions where useful, retain a permitted fallback when a commitment requires one, and preserve accepted meaning when implementations change.

**Maturity bias** here means treating the implementation level as evidence of decision quality. Informed selection instead depends on understanding feasible alternatives and their limitations. It does not imply that every imaginable alternative is known or that a published maturity taxonomy has been validated.

## Include adoption and reversal

An implementation can consume resources without delivering its promised value. Introducing it can require training, migration, testing and process changes. Returning to the earlier system can require a second transition, reconciliation and restoration. This is **double transition cost**, a possible exposure to examine rather than a standard multiplier to add to every budget.

The source's Pendo, GAO and UK examples concern distinct measures and populations. Underused features are not necessarily unnecessary: infrequent critical or seasonal functions may be valuable. Projects missing a cash-savings target may still provide security or other benefits. Qualitative reversal reports establish possible mechanisms, not their prevalence. None establishes a universal failure rate or proves that an agentic replacement would have succeeded.

## Apply the same reasoning to information processing

Preserving a source and preprocessing every possible interpretation are separate investments. Appropriate capture can retain future options without immediately generating every summary, index, graph or embedding.

Select among processing on retrieval, caching a useful result, preprocessing a recurring category and broader preprocessing. Include the cost of discovery, permissions, minimum metadata, freshness checks, invalidation and rebuilding. Some of this work is necessary before retrieval can be safe or practical. Demand-driven processing requires enough source discoverability to learn what is being requested.

A disposable derived structure does not change canonical source authority. Retiring it does not authorize deleting the original or pending work. Storage, privacy, retention and access commitments remain part of the feasible boundary.

Modularity can extend the comparison to models, processing and infrastructure. Count interface, integration, coordination, testing and observability overhead. Owned hardware can reduce one marginal price while adding utilization and lifecycle costs. A vendor's architectural claim needs a comparable measured workload before it supports a cost advantage.

## A measurable operating loop

1. Define the capability, commitments, beneficiaries and relevant horizon.
2. Identify existing resources and feasible agentic, software, manual and hybrid paths.
3. Execute where feasible and record accepted outcomes, time, actual cost and exceptions.
4. Compare full net value and plausible demand, failure and transition scenarios.
5. Materialize selectively when the evidence justifies the investment.
6. Reassess changed needs, prices and constraints; retain, evolve or retire the realization within authority.

Evaluation should test the claim that one sequence improves fulfillment. Measure elapsed time to first accepted value, quality, successful-execution cost, cumulative benefit, implementation and restoration expenditure, and meaningful exceptions. Compare with existing tools as well as new agent paths. Keep measurement periods and demand assumptions explicit.

A useful experiment can fail: no feasible direct path may exist, demand may not repay specialization, or coordination overhead may exceed savings. Reporting such results improves selection rather than invalidating stable software as a legitimate choice.

## Read further

Read the [complete economics paper and reference audit](https://valto.github.io/liquid/whitepapers/economics-of-execution/). Related research drafts develop [intelligence-first sequencing](https://valto.github.io/liquid/whitepapers/drafts/02-intelligence-first-software-second/), [Liquid Software](https://valto.github.io/liquid/whitepapers/drafts/04-liquid-software/), [self-optimization](https://valto.github.io/liquid/whitepapers/drafts/08-the-self-optimizing-information-system/) and [implementation lifecycles](https://valto.github.io/liquid/whitepapers/drafts/12-the-lifecycle-of-liquid-software/).

The supplied economics v2 paper is this concept's conceptual source. The earlier economics version and named AI-maturity companion were not read.
