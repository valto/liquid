# Degrees of Decision Freedom

*Human sovereignty through contextual, reusable delegation*


**Conceptual source and direction: Valto Loikkanen.** Research and drafting: Codex (OpenAI), at his request. Research draft 1.0 · 26 November 2026.

## Abstract

Human control can be preserved through decisions that establish the freedom available to later actors. Valto Loikkanen emphasizes that decisions occur within existing context, commitments and boundaries; they are not isolated transactions. This paper defines decision freedom as a multidimensional, conditional space, distinguishes guidance from enforceable authority, and explains when an agent should act, clarify or escalate. It offers a model for reducing unnecessary repeated approval while preserving reserved human decisions and the ability to revise delegation. [S01]

## 1. A decision can govern many actions

An owner authorizes an assistant to organize a defined set of information, use existing tools and prepare a result. Asking for permission before every harmless formatting or retrieval step can consume more attention than the work itself. Yet the same authorization may not permit contacting an external party, making a financial commitment or deleting an original.

The useful distinction is the scope of freedom already granted. A human decision can authorize a class of actions; later actors choose within that class. This is familiar in organizations, but intelligent systems make its explicit representation increasingly important.

The aim is effective sovereignty: the relevant humans can understand, set, revise and enforce the decisions under which delegated work occurs. Merely inserting an approval button somewhere in a process does not establish that sovereignty.

## 2. Decision freedom is multidimensional

A delegation may permit broad choice of methods, moderate choice of timing, bounded expenditure and no external disclosure. Describing autonomy as a single level hides these distinctions.

| Dimension | Example of granted freedom | Example of a boundary |
| --- | --- | --- |
| Purpose | Pursue the agreed research question | Do not substitute a different objective |
| Information | Read the selected sources | Additional sensitive sources need authority |
| Method | Choose suitable analysis and presentation | Preserve required evidence and identity |
| Resources | Use a defined budget or existing capacity | Do not create a new ongoing commitment |
| Effects | Prepare reversible working artifacts | Reserved publication or deletion decisions |
| Time | Choose an efficient sequence | Observe deadlines and expiry |

The effective action space is the intersection of applicable grants, obligations, system permissions and current conditions. A grant from one participant cannot dispose of another participant's rights. The model is a design framework, not a jurisdiction-specific legal interpretation.

## 3. Separate context, intent, boundaries and guidance

**Context** describes what is known. **Intent** describes the desired result. **Boundaries** define conditions that must hold. **Guidance** expresses preferred ways of working where alternatives remain acceptable. **Freedom** is the remaining choice. **Escalation** identifies decisions outside that choice.

Confusing these categories causes two opposite failures. A preference becomes an unnecessary veto, or a descriptive document is treated as permission to act. Intelligence must interpret the categories, and the runtime must enforce the material boundaries.

EIOS's public framework distinguishes entity governance, actor roles and hard and soft boundaries. PIOS likewise separates information access and operating authority. These are relevant framework accounts, not proof that every implementation enforces the proposed decision model. [S07, S08]

## 4. Human decisions as durable operational information

A reusable decision should record its source, scope, conditions, effective period and reserved effects. It should also state how it can be superseded and what happens to work already underway.

An illustrative decision record might authorize generating internal read-only reports from selected records, permit changes to presentation, require evidence for material claims and reserve external disclosure. The same record can govern many requests without the human reviewing every renderer choice.

The system should preserve the distinction between the original decision and a derived interpretation of it. A summary that omits an exception must not quietly expand authority. Provenance models are useful for recording the relation between source decisions, interpretations and resulting actions. [S17]

## 5. Action, clarification and escalation

An actor should proceed when the requested effect is within a current grant and the necessary interpretation is adequately supported. It should clarify when a material ambiguity affects the expected result. It should escalate when a new decision is required, a reserved effect is reached or applicable boundaries conflict.

Low-impact ambiguity may be resolved through a documented default. A system need not seek a human decision for every unset presentation preference. However, inferring how to display a report is different from inferring consent to share its contents.

Repeated approval is often avoidable when the higher-level decision already covers the action. Repeated approval is appropriate when the facts or effects have materially changed. The record of the decision should help distinguish these cases.

## 6. Technical enforcement and meaningful human control

Natural-language instructions can express scope richly. Enforcement may require resource-specific permissions, bounded credentials, effect checks and records of completion. OAuth rich authorization requests illustrate structured expression of authorization details; they do not themselves decide whether a principal ought to grant the requested scope. [S25]

Controls should follow actual consequences. A system that permits arbitrary disclosure but blocks every formatting change has allocated friction poorly. Conversely, a technically broad credential should not be interpreted as broad human authorization.

Revocation also has limits. It can prevent future access without retracting information already disclosed. Recovery can undo some state changes without undoing all commitments. The human should be able to understand these practical limits before granting consequential freedom.

## 7. Failure modes

Delegation can become stale, contradictory or broader through a sequence of interpretations. Multiple agents may each believe another actor owns a reserved decision. An organization may have several legitimate authorities rather than one simple hierarchy.

The model therefore requires source attribution and conflict handling, not only nested scopes. A disputed decision should remain visibly disputed. A worker's interpretation should not automatically become a governing rule for other workers.

There is also a human cost to defining everything in advance. Excessively detailed delegation can recreate the same bottleneck it aims to solve. Start with the outcomes, material boundaries and understandable defaults needed for the current capability.

## 8. How to evaluate the model

Measure useful completed work per unit of human attention, together with boundary violations, unnecessary escalations, unresolved ambiguity and recovery effort. A reduction in approval count is beneficial only if control remains effective.

Test ordinary work, conflicting instructions, expired grants, changed context and a revoked delegation during execution. Ask the human to explain what the system was allowed to do and why. Agreement between the human account and the system's behavior is more meaningful than a nominal autonomy label.

The proposed contribution is reusable, contextual decision freedom. It complements Liquid Software by defining where implementation and operational choices may evolve, while leaving genuine human decisions visible and authoritative.


## Sources and attribution

**[S01]** Valto Loikkanen and ChatGPT. *Define liquid software — shared conversation*. Retrieved 26 November 2026. [Original source](https://chatgpt.com/share/6b077626-c894-83ed-aabf-d21a363c4313).

**[S07]** peecos / Valto Loikkanen. *PIOS 2.0 master and public README*. PIOS 2.0; retrieved 26 November 2026. [Original source](https://www.peecos.org/pios/master).

**[S08]** Entity Core / Valto Loikkanen. *EIOS 1.0, Keel, and Weave*. Working master v1.4, 21 November 2026. [Original source](https://github.com/entity-core/eios/blob/main/spec/eios-1.0-master-documentation.md).

**[S17]** W3C Provenance Working Group. *PROV-DM: The PROV Data Model*. W3C Recommendation, 30 April 2013. [Original source](https://www.w3.org/TR/prov-dm/).

**[S25]** Torsten Lodderstedt, Justin Richer and Brian Campbell. *OAuth 2.0 Rich Authorization Requests*. RFC 9396, May 2023. [Original source](https://www.rfc-editor.org/rfc/rfc9396.html).

Valto Loikkanen supplies the conceptual synthesis and directs this collection. Codex prepared the research and prose. Definitions and reference models are editorial developments of the cited discussion, not claimed verbatim statements or universal first inventions. See the companion source register for exact read scope, versions and remaining gaps. This draft has not undergone independent peer review.
