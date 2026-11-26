# Intelligence First, Software Second

*Starting with a capability to serve needs, then specializing its execution*


**Conceptual source and direction: Valto Loikkanen.** Research and drafting: Codex (OpenAI), at his request. Research draft 1.0 · 26 November 2026.

## Abstract

Valto Loikkanen proposes that intelligence can fulfill emerging needs before a dedicated implementation exists, with software specialization following demonstrated demand. This paper interprets that principle as a choice of architectural starting point. It distinguishes a general capacity to interpret and assemble from reliable execution, and proposes a decision model for agentic, deterministic and hybrid fulfillment. The central claim concerns when specialization is warranted, not the replacement of all software by language models. [S01]

## 1. Begin with the need

Traditional feature development commonly starts by anticipating an activity, describing it, building an implementation and observing its use. An intelligence-first approach can begin with an actual request: understand it, locate authorized information, choose an available means of fulfillment and learn whether the need recurs.

For example, an organization asks why a supplier commitment changed. The system may need to reconcile correspondence and accepted decisions, rather than execute a known database query. A general interpretation capability can provide an initial answer with evidence and explicit uncertainty. Repeated demand may later support a specialized commitment-history projection.

This illustrative sequence differs from attempting to anticipate every useful combination of information. It makes exploratory fulfillment possible while retaining a path toward efficient repeated execution.

## 2. What intelligence means here

**Intelligence** denotes a capability to interpret a need, use relevant context, select or compose methods, and evaluate a result. A language model may participate, but the capability also depends on retrieval, tools, source quality and operational controls.

Calling it a default capability describes availability at the architectural level. It does not imply that the capability is universal, always accurate or entitled to act. A system may lack the evidence, access, resources or competence required for a request.

**Software specialization** denotes a dedicated implementation that makes an established task more economical or dependable. It may be a query, index, workflow, renderer or service. Intelligence itself runs on software; the distinction is between flexible fulfillment and task-specific realization, rather than between two mutually exclusive substances.

## 3. Three valid modes

| Mode | Suitable conditions | Main challenge |
| --- | --- | --- |
| Agentic | Emerging meaning, varied sources, exploratory tasks | Reliability, cost and ambiguity |
| Deterministic | Stable semantics, repeatable operations, strict constraints | Adaptation when assumptions change |
| Hybrid | Stable operations with uncertain interpretation or exceptions | Clear responsibility at the boundary |

The requester does not determine the serving mode. A conventional application can receive an agentically assembled response; an agent can invoke a deterministic calculation. One interaction may use all three modes.

The response still owes the recipient the agreed result. It should make material uncertainty visible and preserve evidence. A fluent answer is not a substitute for a successful capability.

## 4. A decision model

Choose a feasible implementation by expected value after accounting for serving cost, latency, quality, validation, maintenance, recovery and human attention. Exclude methods that violate the applicable authority or information boundaries before comparing performance.

For an optimization evaluated over a chosen horizon, a simple condition is:

`expected repeated-use savings > construction + validation + maintenance + retirement costs`

This condition applies only if the specialized implementation preserves acceptable quality and behavior. It is an illustrative accounting model, not an empirical threshold. A higher volume does not compensate for answering the wrong question or exposing unauthorized information.

For some critical tasks, the acceptable method may need to be determined before serving the first request. The principle therefore supports intelligent selection of specialization rather than imposing an agent-first sequence on every domain.

## 5. Specializing knowledge responsibly

A successful agent trace can suggest a reusable operation, but converting it into code requires separating stable steps from judgment. An observed answer may contain an assumption that happened to be correct for one case.

Suppose an agent summarizes open commitments by treating every unmarked date as a deadline. A compiler could make that rule efficient and consistently wrong. The specialization must instead use an accepted definition of commitment, supported state transitions and explicit handling of unknown dates.

Tests should include exceptions, stale inputs and denied requests, not only successful traces. Source interpretation that remains uncertain should stay labeled or remain in an agentic part of the workflow. Repeatability is evidence of consistency, not evidence of truth.

## 6. Related research and important distinctions

Litt's work on LLM-enabled personal software explores changes in who creates tools and when they are created. Ink & Switch develops the broader goal of user-modifiable software. These provide close conceptual neighbors to on-demand specialization. [S21, S04]

FrugalGPT studies selecting combinations of language models to manage cost and performance. That is relevant to adaptive execution choices, but it does not prove the conversion of arbitrary reasoning into deterministic services. Learned-index research similarly explores specialization within data access, not general intelligent understanding. [S22, S23]

The contribution here is to place these execution choices inside a durable capability and information model. The capability's meaning and the principal's authority should outlast the selected method.

## 7. An experiment

Select a read-only capability with varied but bounded requests. Record source coverage, result quality, latency, total serving cost and the human effort required to repair errors. Preserve a conventional baseline.

After observing actual demand, specialize a repeated subtask. Compare the specialized route against the original route on new cases, including edge cases. Examine whether the system can return to flexible fulfillment when demand or source structure changes.

A negative outcome is informative. Specialization may fail to amortize, or interpretation may remain too unstable. The system should then keep the simpler route rather than treating generated code as progress by itself.

## 8. The principle's practical value

Intelligence-first architecture changes a planning question from which features must be predicted to which capabilities can responsibly serve emerging needs. It reserves permanent implementation effort for cases where that effort is justified.

It also changes what must be maintained. Shared terminology, evidence, capability definitions and accepted human decisions become operational dependencies. If these are weak, intelligence amplifies ambiguity. If they are reliable, specialized software can become a replaceable means of delivering durable value.


## Sources and attribution

**[S01]** Valto Loikkanen and ChatGPT. *Define liquid software — shared conversation*. Retrieved 26 November 2026. [Original source](https://chatgpt.com/share/6b077626-c894-83ed-aabf-d21a363c4313).

**[S04]** Geoffrey Litt, Josh Horowitz, Peter van Hardenberg and Todd Matthews. *Malleable Software: Restoring User Agency in a World of Locked-Down Apps*. June 2025. [Original source](https://www.inkandswitch.com/essay/malleable-software/).

**[S21]** Geoffrey Litt. *Malleable software in the age of LLMs*. March 2023. [Original source](https://www.geoffreylitt.com/2023/03/25/llm-end-user-programming).

**[S22]** Lingjiao Chen, Matei Zaharia and James Zou. *FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance*. arXiv:2305.05176, 9 May 2023. [Original source](https://arxiv.org/abs/2305.05176).

**[S23]** Tim Kraska, Alex Beutel, Ed H. Chi, Jeffrey Dean and Neoklis Polyzotis. *The Case for Learned Index Structures*. arXiv:1712.01208v3, 30 April 2018. [Original source](https://arxiv.org/html/1712.01208v3).

Valto Loikkanen supplies the conceptual synthesis and directs this collection. Codex prepared the research and prose. Definitions and reference models are editorial developments of the cited discussion, not claimed verbatim statements or universal first inventions. See the companion source register for exact read scope, versions and remaining gaps. This draft has not undergone independent peer review.
