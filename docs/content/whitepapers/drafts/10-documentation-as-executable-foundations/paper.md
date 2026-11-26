# Documentation as Executable Foundations

*Durable meaning from which implementations and behavior can be derived*


**Conceptual source and direction: Valto Loikkanen.** Research and drafting: Codex (OpenAI), at his request. Research draft 1.0 · 26 November 2026.

## Abstract

Valto Loikkanen places documentation, terminology, capability requirements and governing decisions among the relatively durable foundations of adaptive software. This paper explains how documentation can shape execution without being mistaken for executable code or a grant of authority. It develops a source-to-realization model, identifies semantic categories that prevent accidental policy changes, and describes how shared guidance can bound intelligent interpretation when a case is not predefined. The contribution is operational reliance on attributable meaning rather than on a particular implementation. [S01]

## 1. Documentation can precede the implementation

Documentation often describes a system after it has been built. In an adaptive architecture, it also defines what should remain true when the system is generated or changed.

A capability's purpose, information semantics, acceptable result and boundaries can persist through a UI redesign, a backend rewrite or a shift between agentic and deterministic execution. These documents give different actors a common basis for understanding and realization.

The phrase executable foundations refers to this operational role. It does not imply that ordinary prose is automatically executable or that every instruction-like sentence should be obeyed by an agent.

## 2. Identify what kind of statement is being read

| Statement class | Function | Consequence of confusion |
| --- | --- | --- |
| Fact | Reports something established by a source | May be mistaken for a requirement |
| Purpose | Explains the capability's meaningful outcome | May be replaced by an implementation detail |
| Rule | States a binding invariant within its authority | May be weakened into a preference |
| Default | Supplies normal behavior when no choice overrides it | May become an unnecessary veto |
| Example | Illustrates a case | May become a universal requirement |
| Inference | Proposes an interpretation | May be promoted into accepted truth |
| Unknown | Preserves unresolved meaning | May be silently filled with invention |

CRD's public documentation explicitly distinguishes such categories and separates a capability from its realizations. That separation supports consistent intelligent use of documents while retaining uncertainty. [S09]

## 3. Capability meaning and operational realization

For a commitment-history capability, the durable description might define what qualifies as an accepted commitment, what constitutes a meaningful result and how disputed evidence is handled. A realization might use a graph, a query or an agent that reads source records.

A capability document should not be enlarged to include every internal helper. It should identify a complete, meaningful ability. Operational documentation then records the selected implementation, dependencies, exposure and acceptance evidence.

This preserves a common semantic middle between product rationale, user interaction, API descriptions, tools and code. Domain-specific documents remain useful. The capability reference connects them rather than replacing them.

## 4. A derivation chain

`attributable sources → controlled terminology → capability meaning → interaction → realization → acceptance evidence`

Each transition needs traceability appropriate to its consequence. A realization should identify the source revision it implements. An acceptance case should test a meaningful requirement, rather than merely mirror the generated code.

The chain is not one-way. Actual use can reveal a missing definition or a conflict. The system can propose a revision, but the revision should pass through the relevant source authority rather than quietly become a rule because one implementation used it.

PROV-DM provides a vocabulary for relating source entities, transformation activities and responsible agents. It supports traceability; it does not replace the authority process that accepts a change. [S17]

## 5. Shared principles can govern unspecified cases

No useful documentation predicts every situation. Loikkanen proposes that strong foundations can also define where to look for relevant guidance and how to apply it when a case is not predefined. [S01]

A bounded agent can use an accepted glossary, documented defaults, domain references and capability boundaries to resolve ordinary gaps. This can keep custom behavior limited even when interactions emerge dynamically.

The scope of inference matters. An agent may choose a readable layout under design guidance or select an existing retrieval method. It should not invent an accepted business definition, erase an explicit unknown or infer a new permission from an example.

The foundation is therefore both information and a disciplined method of interpretation. An unset detail need not stop every action, but a material unresolved question must remain visible.

## 6. Schemas as projections of meaning

A schema can be generated from shared capability and information semantics. It can represent the fields, types and operations needed for a particular interaction without becoming the ultimate authority over their meaning.

The same capability may have a natural-language description, a GraphQL view, an HTTP exposure or an event representation. Their technical contracts must be appropriate to their consumers. The durable documentation records which meanings and rules these views must preserve. [S11, S13, S16]

This supports the language-and-format framing: documentation supplies the context that lets participants interpret different expressions coherently. It reduces the need to create a custom semantic world for every format.

## 7. Authority and source order

Accessible documentation is not necessarily governing documentation. A retrieved webpage can describe a technique without authorizing its use. A copied policy may be outdated. A worker's note may be a proposal rather than an accepted owner decision.

The system needs to identify the declared source, applicable version and authority of material statements. It should distinguish permission to edit a document from permission to activate its proposed policy.

PIOS's public account separates source authority, information-system membership and implementation placement. EIOS similarly records entity governance and decision roles. These supply relevant context for deriving behavior from documents without confusing a local copy with canonical authority. [S07, S08]

## 8. Failure modes and evaluation

Documentation can be incomplete, contradictory, hard to retrieve or too costly to maintain. Agents can confidently reconcile conflicts incorrectly. Generated implementations can pass superficial tests while implementing the wrong category of statement.

Evaluate whether independent realizations preserve the same capability meaning. Give them normal cases, exceptions, explicit unknowns and conflicting defaults. Ask whether each conclusion is traceable to a source and whether a material new decision is clearly identified.

A useful change test revises one governing rule, then checks which realizations and interactions must change. This examines actual dependency management rather than merely counting document coverage.

## 9. Contribution and practical adoption

Start with a capability whose meaning is repeatedly lost between documents, interfaces and code. Preserve its existing source context, identify material semantic categories and derive one additional realization. Keep the document small enough to use and explicit enough to prevent known ambiguity.

The contribution is durable, attributable meaning that can guide several implementations. Documentation becomes an operational asset when actors can find it, interpret it correctly and demonstrate that the resulting behavior preserves its intended boundaries.


## Sources and attribution

**[S01]** Valto Loikkanen and ChatGPT. *Define liquid software — shared conversation*. Retrieved 26 November 2026. [Original source](https://chatgpt.com/share/6b077626-c894-83ed-aabf-d21a363c4313).

**[S07]** peecos / Valto Loikkanen. *PIOS 2.0 master and public README*. PIOS 2.0; retrieved 26 November 2026. [Original source](https://www.peecos.org/pios/master).

**[S08]** Entity Core / Valto Loikkanen. *EIOS 1.0, Keel, and Weave*. Working master v1.4, 21 November 2026. [Original source](https://github.com/entity-core/eios/blob/main/spec/eios-1.0-master-documentation.md).

**[S09]** Valto Loikkanen. *Capability Documentation / Capability Requirements Document framework*. Draft 0.4; package 0.8.0. [Original source](https://valto.github.io/crd/specification.html).

**[S11]** GraphQL Foundation / specification contributors. *GraphQL Specification*. September 2025 edition, selected explicitly. [Original source](https://spec.graphql.org/September2025/).

**[S13]** OpenAPI Initiative. *OpenAPI Specification*. Version 3.1.1, 24 October 2024; selected explicitly. [Original source](https://spec.openapis.org/oas/v3.1.1.html).

**[S16]** AsyncAPI Initiative. *AsyncAPI Specification*. Version 3.0.0, selected explicitly. [Original source](https://www.asyncapi.com/docs/reference/specification/v3.0.0).

**[S17]** W3C Provenance Working Group. *PROV-DM: The PROV Data Model*. W3C Recommendation, 30 April 2013. [Original source](https://www.w3.org/TR/prov-dm/).

Valto Loikkanen supplies the conceptual synthesis and directs this collection. Codex prepared the research and prose. Definitions and reference models are editorial developments of the cited discussion, not claimed verbatim statements or universal first inventions. See the companion source register for exact read scope, versions and remaining gaps. This draft has not undergone independent peer review.
