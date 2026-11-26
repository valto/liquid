# The Adaptive Interface

*Languages and formats serving contextual needs*


**Conceptual source and direction: Valto Loikkanen.** Research and drafting: Codex (OpenAI), at his request. Research draft 1.0 · 26 November 2026.

## Abstract

The Adaptive Interface is Valto Loikkanen's proposal for treating human and machine interaction as contextual exchanges of information, intent and capabilities. Who needs the information, where they need it, why they need it and what it contains should guide how it is presented or requested. The concept applies to documents, slides, diagrams, voice, applications and machine messages. This paper makes languages and formats the starting frame and explains how precise interaction contracts can emerge through shared meaning, defaults and bounded interpretation. [S01, S26]

## 1. Information before its presentation

The same evidence may support a detailed document, a spoken briefing, a comparison table or an interactive exploration. Traditionally, these are prepared as separate artifacts. They can diverge from one another and from their sources.

An adaptive interface treats them as contextual presentations of attributable information. A person's needs and environment guide the form; the chosen form does not silently become the entire information model.

For example, a project leader walking to a meeting may need a short spoken account of changed commitments. At a desk, the same person may need a timeline with exact source links. An application may request structured changes for a notification. The information identity can persist across all three.

## 2. Four dimensions guide the interaction

| Dimension | Human context | Machine context |
| --- | --- | --- |
| Who | Recipient, role, familiarity and accessibility | Requester, represented principal and intended recipient |
| Where | Device, attention, environment and social situation | Runtime, trust boundary and consuming environment |
| Why | Understanding, learning, decision or action | Retrieval, transformation, execution or delegation |
| What | Information, relationships, complexity and uncertainty | Requested concepts, values, events or capabilities |

These dimensions guide **how**: language, format, level of detail and available interactions. They need not determine a single optimal format. A user should be able to prefer, change or stabilize a presentation, and a machine recipient may impose explicit consumption requirements.

Context affects presentation without changing permission. A relevant answer may still contain information the requester is not entitled to receive.

## 3. Languages and formats as the conceptual starting point

Natural language communicates intent flexibly. A structured query communicates selected concepts and relationships precisely. A table emphasizes comparison; a diagram emphasizes structure; a message format supports machine consumption.

At this level, familiar mechanisms are ways to express and carry interactions. Their technical categories remain distinct: GraphQL is a query language with a type system; REST is an architectural style; MCP and A2A define protocol behavior. These distinctions matter when implementing compatibility, but they need not fragment the conceptual account of the interaction. [S11, S12, S14, S15]

The useful initial question is whether the participants understand the need, representation and constraints. A known language may communicate much of this without a new bespoke interface. Open documentation and terminology can supply the remaining context.

## 4. Meaning can precede an explicit schema

The requester can describe a desired result using familiar terms, a structured selection, an example or a reference to a shared capability. The receiver can resolve that request against its information, governing documentation and supported behavior.

Some interactions require no separately designed schema beyond existing conventions. Others benefit from a generated or negotiated type description. The appropriate precision depends on consequences and ambiguity. Selecting a display layout may rely on a default; agreeing which amount is being reported may require explicit units and scope.

A schema is one way to express a resolved structure. Its creation can be a runtime activity, and its persistence can be limited to the interaction. The more durable elements may be the meaning of the information and the decisions governing its use.

## 5. Human and machine interfaces share a foundation

Both kinds of participant express needs, consume information and invoke capabilities. Both require identity and authority appropriate to their role. Both can receive agentic, deterministic or hybrid fulfillment.

Their experiences still differ. A human may need explanation, direct manipulation and an opportunity to reconsider. A machine may need exact types, correlation identifiers, structured failure and progress. A common semantic foundation can produce distinct presentations suitable to each recipient.

Dynamicland's work on humane dynamic media offers a related perspective on computational representation and shared understanding. Litt's work highlights why a conversational interface is not adequate for every task. The proposed adaptive interface therefore includes graphical and exploratory forms rather than treating conversation as the universal destination. [S06, S21]

## 6. Preserve provenance through transformation

A presentation should distinguish source information from an interpretation. If a diagram summarizes a dispute, it should retain access to the competing accounts. If a briefing omits detail for brevity, the omission should not become a canonical deletion.

Originals, accepted revisions and derived presentations should retain their identities and relationships. Provenance standards provide ways of describing entities, activities and agents involved in such transformations. They do not independently establish the truth of the resulting interpretation. [S17]

Documents can themselves be originals: a signed agreement or an authored essay has meaning in its particular form. An adaptive presentation should not erase that form or assume every narrative is merely a disposable rendering of a database.

## 7. Interaction includes action

An interface may help a person understand information or change state. The distinction must be clear. Exploring an option is not the same as committing to it; preparing an edit is not the same as accepting it.

Generated interfaces should therefore preserve the capability's action boundaries. The user should understand the consequence of a control even if its visual form is new. A machine request should distinguish retrieval from mutation and identify the expected effects.

A pleasant adaptive experience cannot compensate for a hidden consequential action. Meaningful control requires the interaction to make the decision legible at the point where it matters.

## 8. Failure modes and evaluation

Adaptation can create instability, inaccessible formats, inconsistent terminology or excessive simplification. A system may incorrectly infer what someone knows or prefers. Machine consumers may fail when a representation changes unexpectedly.

Evaluate whether recipients correctly understand and use the information, how much effort they expend, and whether material uncertainty and provenance survive transformation. Compare different presentations of the same source and ask recipients to explain the same central relationship.

For machine interactions, test equivalent requests in different supported languages or formats. Examine whether meaning, permission and result agree. A formatting match alone is insufficient if the content differs semantically.

## 9. An independent architectural contribution

Adaptive interfaces are useful even when the backend remains entirely conventional. They can improve publishing, reporting, education and information access without requiring a full liquid architecture.

Their distinctive contribution is to place the interaction's contextual purpose ahead of its format. Shared meaning provides coherence; languages and formats make that meaning usable; intelligence helps choose and interpret them; and human-defined boundaries govern the exchange.


## Sources and attribution

**[S01]** Valto Loikkanen and ChatGPT. *Define liquid software — shared conversation*. Retrieved 26 November 2026. [Original source](https://chatgpt.com/share/6b077626-c894-83ed-aabf-d21a363c4313).

**[S06]** Dynamicland Foundation. *Dynamicland FAQ*. Living page in /2024/; accessed 26 November 2026. [Original source](https://dynamicland.org/2024/FAQ/).

**[S11]** GraphQL Foundation / specification contributors. *GraphQL Specification*. September 2025 edition, selected explicitly. [Original source](https://spec.graphql.org/September2025/).

**[S12]** Roy Thomas Fielding. *Architectural Styles and the Design of Network-based Software Architectures, Chapter 5: Representational State Transfer*. Doctoral dissertation, 2000. [Original source](https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm).

**[S14]** Model Context Protocol contributors. *Architecture — Model Context Protocol*. Retrieved latest alias resolved to 2026-07-28. [Original source](https://modelcontextprotocol.io/specification/2026-07-28/architecture).

**[S15]** A2A Project. *Agent2Agent Protocol Specification*. Retrieved latest page identifies released version 1.0.0. [Original source](https://a2a-protocol.org/latest/specification/).

**[S17]** W3C Provenance Working Group. *PROV-DM: The PROV Data Model*. W3C Recommendation, 30 April 2013. [Original source](https://www.w3.org/TR/prov-dm/).

**[S21]** Geoffrey Litt. *Malleable software in the age of LLMs*. March 2023. [Original source](https://www.geoffreylitt.com/2023/03/25/llm-end-user-programming).

**[S26]** Valto Loikkanen. *Commission clarifications on schemas, languages and formats*. 26 November 2026.

Valto Loikkanen supplies the conceptual synthesis and directs this collection. Codex prepared the research and prose. Definitions and reference models are editorial developments of the cited discussion, not claimed verbatim statements or universal first inventions. See the companion source register for exact read scope, versions and remaining gaps. This draft has not undergone independent peer review.
