# Beyond Predefined APIs

*Interaction languages, emerging contracts and implementation-independent fulfillment*


**Conceptual source and direction: Valto Loikkanen.** Research and drafting: Codex (OpenAI), at his request. Research draft 1.0 · 26 November 2026.

## Abstract

Valto Loikkanen proposes that a requester should express its information need in a suitable language or format while an intelligent receiver resolves the need using shared documentation, terminology and authorized information. A dedicated implementation need not precede every supported request. This paper develops that proposal and the accompanying clarification that schemas can be inferred, generated or negotiated rather than fixed in advance. It distinguishes the meaning of an interaction from its language, representation and realization, and explains who contributes each part. Existing protocol conformance remains relevant when claimed, but it is an implementation choice within the broader architecture. [S01, S26]

## 1. Start with expression and understanding

A person asks for the accepted commitments due during a particular period. An application asks for the same concepts in a structured selection. An agent asks because it needs to prepare a briefing on behalf of an organization.

All three need a shared account of commitment, acceptance, due date, source and permission. They may use different languages and require different representations. The receiving system can use a direct query, intelligent retrieval or a combination without changing the underlying need.

The proposed shift is to support that need through an interpretable interaction, rather than require a dedicated endpoint and backend implementation for every useful variation. A receiving mechanism must still exist, and it must have a bounded ability to understand and fulfill the request.

## 2. Four concerns that should remain distinguishable

| Concern | Question |
| --- | --- |
| Meaning | Which information or capability is requested, and for what purpose? |
| Language | How does the requester express that need? |
| Representation | How should the result be organized and communicated? |
| Realization | How will the receiver produce an acceptable result? |

A schema can describe some of the representation and supported operations. A capability document can describe meaning and acceptable behavior. A protocol can define interaction mechanics. None alone supplies every part of the exchange.

Treating these mechanisms initially as languages and formats keeps the architectural question clear. Technical classifications can be applied when a concrete implementation needs interoperability or a specific guarantee.

## 3. What a schema requirement actually means

In the September 2025 GraphQL specification, a service's schema describes its types, directives and root operations. Field selections are validated against the type in scope, and execution uses that type system. The specification therefore requires enough defined structure for conventional validation and execution. [S11]

This does not require a human to handwrite a permanent schema before any need appears. An implementation can construct a schema from governing information, generate one for a session, or negotiate a compatible view. The schema may be an operational expression of already shared meaning rather than the source of that meaning.

A conventional GraphQL request cannot simply add a schema definition to its executable document and expect the normal executor to accept it. A system that generates schemas must arrange that process through its own receiving or preparation mechanism, then perform the applicable GraphQL validation and execution. This is a compatibility detail, not a prohibition on dynamic interaction.

A future language may use self-describing results, examples or other mechanisms instead. The broader proposal does not depend on preserving GraphQL's current rules. A system should accurately describe the guarantees it offers rather than assume that familiar syntax implies full conformance.

## 4. Who defines the interaction?

The answer is distributed across the participants and their existing decisions.

The **requester** contributes the need, intended recipient, relevant constraints and desired response representation. The **receiver** contributes the information it actually has, the meaning it can support and the actions it is authorized to perform. The **information principal** governs disclosure and use. Shared documentation supplies definitions, conventions and defaults.

Their agents can resolve ordinary gaps using those foundations. A new schema or explicit negotiation is needed only where it adds necessary precision. An unresolved material difference requires clarification or a structured failure, not creative invention.

The requester cannot unilaterally redefine an accepted fact, and the receiver cannot silently substitute a different concept because its database makes that easier. Both can agree to a transformation or narrower scope where their authority permits it.

## 5. A worked interaction

Consider this illustrative request:

> Return accepted commitments due before 3 December 2026, with stable identifiers, dates and attributable source references. Use the organization's documented meaning of accepted commitment.

The requester could communicate this in natural language or a supported structured selection. In a dynamically prepared GraphQL view, an executable request might look like:

```graphql
query {
  acceptedCommitments(dueBefore: "2026-12-03") {
    id
    dueDate
    sourceReference
  }
}
```

This example is not a published PIOS API. It becomes a valid GraphQL operation only if the prepared schema supports the fields and argument. That schema can emerge from existing capability meaning and the requested view rather than from a previously shipped endpoint.

Several matters still need resolution: which calendar and time boundary applies, whether undated commitments are excluded, what source reference means, whether partial results are acceptable, and whose commitments the actor may see. Existing conventions can answer these without a new human decision each time. Where they do not, the receiver must expose the gap.

The query shape communicates selected fields. It does not alone establish every type, nullability rule, completeness condition or business definition. Similarly, a REST-style interaction needs an agreed representation when exact consumption matters; the architectural style itself does not prescribe a universal response shape. [S12, S13]

## 6. Minimize custom negotiation through shared foundations

Open terminology and capability documentation can make an emerging interaction highly constrained even when no dedicated implementation exists. Participants can consult the same definitions and rules, apply the same defaults and identify the same acceptable result.

This is central to Loikkanen's proposal. The goal is not arbitrary custom interfaces for every request. It is broad expression within a coherent space of meaning, with a small amount of justified adaptation at the boundary.

A system might preserve several degrees of precision: a shared definition, a request-specific selection, an agreed result example, and a machine-checkable schema where required. The additional form should resolve a real need rather than become an automatic prerequisite for all interaction.

## 7. Existing mechanisms can remain complementary

MCP provides machinery for interaction with exposed tools, resources and prompts. A2A provides agent-facing interaction concepts including messages, tasks, artifacts and discovery. PAIX's public guidance proposes email as an entry and fallback channel, with optional negotiated upgrades. [S14, S15, S10]

These roles do not determine whether the serving logic is intelligent or deterministic. A tool service may contain intelligence; an agent endpoint may call a conventional query. Nor does advertising a capability confer permission to use it.

CRD supplies a capability-centered semantic reference, while OpenAPI and AsyncAPI can describe particular HTTP or event-driven exposures. The broader interaction architecture can use these when suitable without reducing all meaning to an endpoint catalog. [S09, S13, S16]

## 8. Failure, uncertainty and effects

A machine-readable response should distinguish unsupported language, unresolved meaning, unavailable evidence, denied scope and execution failure. These are different situations with different next steps.

Read operations may tolerate explicit incomplete evidence. State-changing operations need precise effect semantics, identity, replay handling and a way to determine whether a result was accepted when the response is lost. A dynamically generated format does not remove these obligations.

Contract evolution is likewise distinct from implementation optimization. Changing the backend while preserving a promised result can be transparent. Changing the meaning, completeness or effects may require an explicit interaction-level revision.

## 9. Evaluation and contribution

Test equivalent needs expressed through several supported languages and formats. Measure whether recipients obtain semantically equivalent results, whether denied scope remains denied, and how much bespoke interpretation or negotiation is required.

Then change the serving method without changing the agreed need. Test source updates, missing fields, ambiguity and failures. The strongest result would show that new useful interactions can be served within shared boundaries before dedicated software exists, while exact consumers retain the guarantees they require.

The paper's contribution is an emerging interaction contract grounded in shared meaning. A schema may be one resulting artifact. The underlying architectural assets are the need, the information, the capability and the decisions that make their exchange legitimate.


## Sources and attribution

**[S01]** Valto Loikkanen and ChatGPT. *Define liquid software — shared conversation*. Retrieved 26 November 2026. [Original source](https://chatgpt.com/share/6b077626-c894-83ed-aabf-d21a363c4313).

**[S09]** Valto Loikkanen. *Capability Documentation / Capability Requirements Document framework*. Draft 0.4; package 0.8.0. [Original source](https://valto.github.io/crd/specification.html).

**[S10]** Private AI Exchange / PAIX. *Human & Agent Interoperability*. Non-normative design guidance for PAIX v0.1. [Original source](https://github.com/privateaiexchange/paix-spec/blob/main/docs/Human_Agent_Interoperability.md).

**[S11]** GraphQL Foundation / specification contributors. *GraphQL Specification*. September 2025 edition, selected explicitly. [Original source](https://spec.graphql.org/September2025/).

**[S12]** Roy Thomas Fielding. *Architectural Styles and the Design of Network-based Software Architectures, Chapter 5: Representational State Transfer*. Doctoral dissertation, 2000. [Original source](https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm).

**[S13]** OpenAPI Initiative. *OpenAPI Specification*. Version 3.1.1, 24 October 2024; selected explicitly. [Original source](https://spec.openapis.org/oas/v3.1.1.html).

**[S14]** Model Context Protocol contributors. *Architecture — Model Context Protocol*. Retrieved latest alias resolved to 2026-07-28. [Original source](https://modelcontextprotocol.io/specification/2026-07-28/architecture).

**[S15]** A2A Project. *Agent2Agent Protocol Specification*. Retrieved latest page identifies released version 1.0.0. [Original source](https://a2a-protocol.org/latest/specification/).

**[S16]** AsyncAPI Initiative. *AsyncAPI Specification*. Version 3.0.0, selected explicitly. [Original source](https://www.asyncapi.com/docs/reference/specification/v3.0.0).

**[S26]** Valto Loikkanen. *Commission clarifications on schemas, languages and formats*. 26 November 2026.

Valto Loikkanen supplies the conceptual synthesis and directs this collection. Codex prepared the research and prose. Definitions and reference models are editorial developments of the cited discussion, not claimed verbatim statements or universal first inventions. See the companion source register for exact read scope, versions and remaining gaps. This draft has not undergone independent peer review.
