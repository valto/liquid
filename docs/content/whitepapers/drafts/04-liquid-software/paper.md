# Liquid Software

*Governed implementations that take shape around actual needs*


**Conceptual source and direction: Valto Loikkanen.** Research and drafting: Codex (OpenAI), at his request. Research draft 1.0 · 26 November 2026.

## Abstract

Liquid Software, in Valto Loikkanen's proposed sense, describes implementations that emerge, adapt, specialize and retire according to actual needs while preserving information, capability meaning and human-defined boundaries. It joins his earlier ideas of UI on the fly and backend on the fly into a lifecycle spanning human presentation, machine interaction and execution. This paper defines the paradigm, distinguishes it from continuous delivery and unrestricted code generation, and identifies the conditions under which implementation fluidity creates durable value. [S01]

## 1. From on-demand creation to an ongoing property

A temporary dashboard can be generated for a meeting. A backend function can be assembled for a new analysis. These examples describe creation on demand. Liquid Software extends the idea: implementations continue to change in response to demand, constraints and evidence of usefulness.

An implementation might be generated once and remain stable. Another might serve a seasonal need and later retire. Several might consolidate after their common behavior becomes clear. The defining property is the ability to change realization while preserving the relevant capability and information continuity.

**Liquid Software is a governed mode of software realization in which implementations are selected and evolved around actual needs, under durable semantic, information and authority foundations.** This is a proposed definition, not an established industry standard.

## 2. The term and its prior lineage

JFrog's earlier Liquid Software vision concerns continuous, trusted delivery of software updates. Its published material links the concept to a 2018 book. The term therefore has established prior use; this collection does not claim its coinage. [S03]

Malleable-software research emphasizes the user's ability to reshape tools at the point of use. Litt's writing also explores LLM-enabled temporary scripts and interfaces. Loikkanen's synthesis adds a governed population of realizations around persistent information, capability documents and usage-driven specialization. These are related framings with different emphases, rather than exclusive territories. [S04, S21]

## 3. Three concerns with different lifetimes

| Concern | Role | Appropriate change |
| --- | --- | --- |
| Persistent foundation | Identity, original information, history and accepted work | Attributable revision and controlled lifecycle |
| Meaning and governance | Capability definitions, terminology, decisions and boundaries | Deliberate, versioned evolution |
| Realization | Interfaces, queries, workflows and backend components | Adaptation according to actual needs |

A durable foundation can contain continuously changing information. Its durability concerns identity, provenance and the ability to recover, not a frozen snapshot. Governing documentation may also change, but a generated component must not silently redefine the governing rule that justifies it.

This separation makes custom experiences possible without making every experience a custom world. A renderer can adapt to a recipient while using the same accepted meaning of a commitment, date, permission or result.

## 4. UI, machine interaction and backend as one lifecycle

UI on the fly adapts presentation and interaction to the person, situation, purpose and information. Machine interaction expresses comparable needs in a suitable language or format. Backend on the fly supplies the operations needed to fulfill the exchange.

These can be coordinated through shared semantics without becoming identical. A spoken explanation and a structured result differ in their usability requirements; an agent may need progress messages while a person needs an understandable choice. The common foundation is the capability and interaction meaning, rather than a universal screen or message type.

The serving implementation can remain hidden when it makes no material difference to the recipient. Material limitations, uncertainty, commitments and consequential changes must remain visible.

## 5. An illustrative lifecycle

A team asks for a comparison of project commitments. An agent initially locates relevant originals, reconciles dates and prepares a view. The team repeats the request, revealing a stable definition and a recurring combination of sources.

A monitored optimization process then proposes a specialized projection and query. The proposal is tested against new cases and exceptions. Once accepted within the applicable authority, it becomes the preferred route for that pattern. Requests with unresolved meaning continue through interpretation.

Months later, the project's structure changes. The specialized route may be revised, bypassed or retired. The team should retain its source records, accepted decisions and outstanding work. Retiring the implementation must not be mistaken for retiring these assets.

This example is a proposed workflow, not a claim about an existing deployed optimizer.

## 6. What must remain true during adaptation

An adaptive implementation must preserve the relevant result semantics, access boundaries, source attribution, freshness obligations and side-effect rules. The exact controls depend on the capability. A read-only visualization and a payment operation require different execution assurance.

CRDs provide a public proposal for documenting capability purpose, meaningful outcomes, interaction contracts, rules and unknowns independently of realization. Their role is to preserve meaning through implementation changes; a CRD is not itself a runtime authorization or a guarantee that generated code is correct. [S09]

End-to-end reasoning adds a useful constraint: an internal component's success does not necessarily prove the user's complete outcome. A renderer may work while using stale information; a service may respond while losing an accepted state change. Acceptance should therefore follow the actual capability boundary. [S20]

## 7. Why fluidity is selective

Some components should remain stable because they are reliable, economical or externally depended upon. Familiar interfaces can reduce cognitive load. Long-lived services may provide better continuity than repeated regeneration.

The paradigm seeks appropriate adaptability rather than maximum change. A useful policy might allow contextual presentation freely, propose backend changes after demonstrated repetition, and reserve changes to accepted authority or external commitments for the designated decision-maker.

Constant generation without retirement creates accumulation. Aggressive retirement without a capability fallback creates breakage. The lifecycle must account for both costs.

## 8. Evaluating a liquid implementation

Evaluate how quickly a meaningful need becomes serviceable, what adaptation costs over time, and whether capability behavior survives implementation replacement. Include provenance, authority, recovery, human learning and support burden.

A meaningful experiment replaces one implementation while preserving the contract. Test representative normal cases, unfamiliar variations, denied requests and recovery after a failed change. Compare the result with maintaining a conventional implementation.

The concept would be weakened if realization changes repeatedly require rewriting the capability meaning, lose original information, or create greater maintenance costs than they remove. Those outcomes identify conditions where a stable implementation remains preferable.

## 9. Contribution and relationship to the collection

Liquid Software describes the evolving realization. The Adaptive Interface describes the exchange of needs and information. Capture for Unknown Future Value describes preservation. Degrees of Decision Freedom describes the space in which adaptation may occur. The self-optimizing system supplies one concrete mechanism for selecting changes.

Each can be adopted independently. Their combination is useful when information and capability meaning provide continuity while implementations remain replaceable. That combination is the central contribution attributed to Loikkanen in this collection.


## Sources and attribution

**[S01]** Valto Loikkanen and ChatGPT. *Define liquid software — shared conversation*. Retrieved 26 November 2026. [Original source](https://chatgpt.com/share/6b077626-c894-83ed-aabf-d21a363c4313).

**[S03]** JFrog; related book by Fred Simon, Yoav Landman and Baruch Sadogursky. *A Vision of Liquid Software; associated book Liquid Software: How to Achieve Trusted Continuous Updates in the DevOps World*. Associated book copyright 2018. [Original source](https://jfrog.com/whitepaper/a-vision-of-liquid-software/).

**[S04]** Geoffrey Litt, Josh Horowitz, Peter van Hardenberg and Todd Matthews. *Malleable Software: Restoring User Agency in a World of Locked-Down Apps*. June 2025. [Original source](https://www.inkandswitch.com/essay/malleable-software/).

**[S09]** Valto Loikkanen. *Capability Documentation / Capability Requirements Document framework*. Draft 0.4; package 0.8.0. [Original source](https://valto.github.io/crd/specification.html).

**[S20]** J. H. Saltzer, D. P. Reed and D. D. Clark. *End-to-End Arguments in System Design*. ACM Transactions on Computer Systems 2(4), November 1984, pp. 277–288. [Original source](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf).

**[S21]** Geoffrey Litt. *Malleable software in the age of LLMs*. March 2023. [Original source](https://www.geoffreylitt.com/2023/03/25/llm-end-user-programming).

Valto Loikkanen supplies the conceptual synthesis and directs this collection. Codex prepared the research and prose. Definitions and reference models are editorial developments of the cited discussion, not claimed verbatim statements or universal first inventions. See the companion source register for exact read scope, versions and remaining gaps. This draft has not undergone independent peer review.
