# The Self-Optimizing Information System

*Learning from demand to improve how a durable capability is served*


**Conceptual source and direction: Valto Loikkanen.** Research and drafting: Codex (OpenAI), at his request. Research draft 1.0 · 26 November 2026.

## Abstract

Valto Loikkanen proposes a monitoring and optimization loop that observes information requests, identifies repeated needs, and creates, revises or retires specialized implementations. A general intelligent route supplies flexibility; deterministic and hybrid routes supply efficiency where justified. This paper develops the loop as a reference design, including candidate selection, semantic checks, staged acceptance and recovery. A nightly run is one possible cadence, not a requirement. The proposed optimizer changes how a capability is fulfilled while preserving its meaning, source authority and human-defined boundaries. [S01]

## 1. Observe use before committing to specialization

A capable information system can serve a novel request by interpreting it and retrieving relevant evidence. Some requests remain occasional. Others recur with a consistent meaning and costly execution. Those recurring patterns are candidates for specialization.

The optimization loop turns these observations into improvements. It can create an index, a structured projection, a direct query, a reusable workflow or a presentation component. It can also consolidate overlapping implementations or retire ones whose value no longer justifies their cost.

The loop is a proposed architecture. This paper does not report a deployed implementation or measured savings from the complete system.

## 2. Define the objective before optimizing

Optimizing raw request count or latency alone can produce worse outcomes. The system should optimize useful fulfillment subject to quality, evidence, authority, freshness and recovery requirements.

For a candidate implementation, estimate its expected benefit over a declared horizon and subtract construction, validation, operation, maintenance and retirement costs. Include user effort and failures. Compare it with maintaining the current route.

An illustrative arithmetic case: if a specialized route saves nine abstract cost units per request and requires nine hundred units to build and maintain over the period, it needs more than one hundred equivalent requests to create positive net savings. This is a hypothetical accounting example; real quality and authority requirements remain independent constraints.

Frequency is evidence of demand, not a complete decision rule. A rare critical capability can warrant specialization; a frequent ambiguous question can remain a poor candidate.

## 3. Observe patterns without collecting everything

The monitor needs enough information to distinguish capability, request meaning, execution route, cost, latency, result quality and relevant dependency revisions. It need not retain every private prompt or response indefinitely.

| Observation | Use in optimization |
| --- | --- |
| Capability and semantic pattern | Groups requests that actually mean the same thing |
| Source and policy revisions | Identifies dependency and permission changes |
| Execution cost and latency | Estimates possible specialization benefit |
| Failures and human corrections | Exposes weaknesses hidden by successful responses |
| Unserved or abandoned requests | Reveals demand the current system cannot fulfill |
| Seasonal and declining use | Informs retention and retirement |

An optimizer that sees only successful requests may reinforce existing limitations. It should account for requests declined because of unsupported language, missing capabilities or poor evidence, while preserving appropriate privacy.

## 4. A bounded optimization loop

1. **Observe:** record selected operational evidence from actual fulfillment.
2. **Interpret:** group requests using accepted terminology and capability meaning.
3. **Propose:** identify a candidate realization and its expected benefit.
4. **Construct:** create or revise the smallest useful implementation in isolation.
5. **Validate:** test semantic behavior, authority, freshness, effects and recovery.
6. **Accept:** activate within the current delegation and any genuine reserved decision.
7. **Measure:** compare useful outcomes and costs with the previous route.
8. **Revise or retire:** respond to drift, failure and changing demand.

The loop can run nightly, periodically or when a material signal appears. Timing should follow workload and dependency conditions. An off-peak schedule does not itself establish safe capacity or authority.

## 5. Semantic equivalence is stronger than output similarity

Two results can look alike while answering different questions. A generated commitment query might treat an inferred intention as an accepted commitment. A cached result might include records whose access has since changed.

A candidate should therefore be tested against explicit meaningful outcomes and source-backed cases. CRDs offer a way to preserve capability purpose, interaction contracts, rules and unknowns independently of realization. Provenance helps connect derived results to their sources. [S09, S17]

An agent trace can supply examples, but it is not automatically a specification. Repeated assumptions should be identified and checked before being frozen into a specialized route.

## 6. Staged acceptance and runtime selection

A candidate can first be evaluated on retained cases, then run in shadow alongside the existing route, and then become active for a bounded request class. The old route remains available where its behavior and cost are acceptable.

The dispatcher should know which capability versions, source types and conditions a realization supports. A language or representation chosen by the requester does not determine the serving method. An agent request may take the direct route; an application request may require interpretation.

Fallback is conditional. A slower agent route is useful only if it still meets the capability's acceptable behavior. It should not be used to hide a deterministic failure when the fallback cannot preserve the required result.

## 7. Dependencies and drift

Candidate validity depends on more than code. Terminology, source revisions, permissions, model versions and capability definitions may all matter. A change can make a previously accepted route unsuitable.

The system should identify these dependencies at an appropriate level and invalidate or reevaluate affected routes. Avoid treating every unrelated change as a reason to rebuild the whole system. Scope the work to the assumption that actually changed.

Drift may also be gradual. A request pattern once consistent can split into several meanings. The optimizer should be able to distinguish new variants rather than forcing them through the old implementation.

## 8. Recovery and retirement

Withdrawal should preserve accepted information, originals, pending work and relevant evidence. Retiring a specialized route is different from deleting the records that made it useful.

A registry can retain the capability identity, realization version, acceptance evidence and reason for withdrawal. Actual executable artifacts may have their own retention policy. Reinstating a seasonal implementation should verify current dependencies rather than assume historical acceptance remains sufficient.

End-to-end acceptance matters: successful deployment of a query does not prove the user's result survives a failed response, stale projection or lost state transition. [S20]

## 9. Related work and limits

Learned-index research revisits data-access structures through models, while FrugalGPT studies adaptive selection of language-model combinations. Both support investigating specialized execution choices; neither validates the complete governed optimization loop proposed here. [S23, S22]

The distinctive synthesis is to place optimization around a persistent capability, information foundation and human decision space. The optimizer is an operational actor with delegated freedom, not an independent authority over its owner's data or goals.

## 10. Evaluation and open questions

Compare the adaptive system with a fixed baseline over a changing workload. Measure useful quality, total cost, latency, maintenance effort, failed transitions, boundary violations and recoverability. Include unfamiliar requests, declining demand and a source or policy change.

The research questions are concrete: can semantic grouping remain reliable; can validation costs amortize; can drift be detected before it harms users; and can retirement preserve capability continuity? Answering them would establish the conditions under which self-optimization creates useful liquid behavior.


## Sources and attribution

**[S01]** Valto Loikkanen and ChatGPT. *Define liquid software — shared conversation*. Retrieved 26 November 2026. [Original source](https://chatgpt.com/share/6b077626-c894-83ed-aabf-d21a363c4313).

**[S09]** Valto Loikkanen. *Capability Documentation / Capability Requirements Document framework*. Draft 0.4; package 0.8.0. [Original source](https://valto.github.io/crd/specification.html).

**[S17]** W3C Provenance Working Group. *PROV-DM: The PROV Data Model*. W3C Recommendation, 30 April 2013. [Original source](https://www.w3.org/TR/prov-dm/).

**[S20]** J. H. Saltzer, D. P. Reed and D. D. Clark. *End-to-End Arguments in System Design*. ACM Transactions on Computer Systems 2(4), November 1984, pp. 277–288. [Original source](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf).

**[S22]** Lingjiao Chen, Matei Zaharia and James Zou. *FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance*. arXiv:2305.05176, 9 May 2023. [Original source](https://arxiv.org/abs/2305.05176).

**[S23]** Tim Kraska, Alex Beutel, Ed H. Chi, Jeffrey Dean and Neoklis Polyzotis. *The Case for Learned Index Structures*. arXiv:1712.01208v3, 30 April 2018. [Original source](https://arxiv.org/html/1712.01208v3).

Valto Loikkanen supplies the conceptual synthesis and directs this collection. Codex prepared the research and prose. Definitions and reference models are editorial developments of the cited discussion, not claimed verbatim statements or universal first inventions. See the companion source register for exact read scope, versions and remaining gaps. This draft has not undergone independent peer review.
