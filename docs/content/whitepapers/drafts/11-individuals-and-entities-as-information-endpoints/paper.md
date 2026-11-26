# Individuals and Entities as Information Endpoints

*Separating the principal from the actor and the serving implementation*


**Conceptual source and direction: Valto Loikkanen.** Research and drafting: Codex (OpenAI), at his request. Research draft 1.0 · 26 November 2026.

## Abstract

Valto Loikkanen proposes individuals and entities as the persistent principals of an information architecture. Humans, agents and applications act directly or indirectly on their behalf, while implementations serve their needs through changing interfaces. This paper interprets the two-principal model as an architectural organizing choice, rather than a claim that every network endpoint fits a simple ownership ontology. It develops the separation of principal, requester, beneficiary, information authority and realization, including shared records and cross-principal interaction. [S01]

## 1. Who persists when the software changes?

A person may replace a notes application, an agent provider or a hosting service. An organization may replace employees, dashboards or communication tools. Its information, relationships and commitments should not disappear with each replacement.

The proposed architecture anchors continuity in the individual or entity served. PIOS describes a personal information foundation; EIOS describes an entity information foundation. These are public framework models with related principles and distinct scope. Their documentation does not establish universal adoption or production readiness. [S07, S08]

An endpoint in this paper means a logical point of information continuity and governed interaction. It need not be one server, address, physical machine or database.

## 2. Principal, actor and implementation are independent

| Dimension | Meaning | Examples |
| --- | --- | --- |
| Principal | The individual or entity whose authorized purpose is served | Person, company, association |
| Operational actor | Who initiates or performs an interaction | Human, agent, application |
| Beneficiary | Who ultimately benefits from the work | Principal, customer, member or another party |
| Information authority | Who can accept or govern the relevant record | Owner, designated entity role, shared decision process |
| Realization | How the receiver fulfills the need | Agentic, deterministic or hybrid execution |

No dimension automatically determines another. An application may request information for a person and receive agentic fulfillment. An agent may request information for an entity and receive a direct query result. A human may act under an entity role rather than in a personal capacity.

The immediate actor's identity therefore cannot substitute for the represented principal or the scope of delegated authority.

## 3. Two principal categories, many practical arrangements

The model distinguishes individuals from entities to preserve personal and organizational continuity. It does not imply that entities have one simple human decision-maker or that all information has a single owner.

An organization can contain roles, teams, jurisdictions and conflicting interests. A shared agreement may belong to several participants' records. A public dataset may be served by infrastructure whose operator and data authority differ.

These arrangements can be represented through relationships among principals, roles and records. If an autonomous agent participates without a clear represented principal, the system should preserve that uncertainty or identify the accountable operator; it should not invent a human owner to force the case into the model.

The distinction is useful if it clarifies authority and continuity. It should be extended or qualified where it conceals them.

## 4. Direct and indirect needs

A human may explicitly ask an agent to retrieve a document. An agent may also discover that it needs a supporting record to accomplish an already authorized objective. The second request serves an indirect need.

Indirect work does not require a new human instruction for every internal dependency. It does require the dependency to remain within the purpose and scope of the existing delegation. A task to prepare an internal briefing does not automatically authorize external contact or disclosure.

The interaction context should therefore identify the requesting actor, represented principal, purpose, applicable grant and intended result recipient. The exact representation can vary by language and format, provided the meaning remains clear enough for the consequences involved.

## 5. Cross-principal relationships

The proposed model supports individual-to-individual, individual-to-entity and entity-to-entity interactions. Their information exchanges may use ordinary human communication, applications, agents or combinations.

PAIX's public guidance explores addressable human and agent participation, disclosure and optional channel upgrades. It explicitly separates advertising a capability from granting access. A2A and other mechanisms can supply particular execution and task interactions. [S10, S15]

An exchange should preserve each participant's independent policy. Agreement on a language or format does not override either party's authority boundaries, and a receiving system's access does not entitle it to disclose the information elsewhere.

## 6. Shared information and accepted state

One record can have several legitimate views and custodians. A signed agreement, for example, may appear in both an individual's and an entity's information foundations. These are not automatically competing masters; they can preserve the same source identity with distinct governance context.

The important questions are which record is authoritative for which purpose, how accepted changes are represented, and what each participant is entitled to retain or modify. Copying a record does not transfer every right associated with it.

Provenance can relate originals, copies, derived assertions and actions across systems. An acceptance process must still determine which statements or revisions count as agreed. [S17]

## 7. Replacing an operational actor

A provider change should preserve the principal's information, accepted commitments, relevant grants and operational history. Credentials and permissions may require separate re-establishment; exporting content does not export authority automatically.

A new agent should be able to understand the current capability and decision context without inheriting unsupported claims from a former actor. The principal retains continuity even when the representation and execution change.

Local-first and Solid research provide relevant approaches to user control and separation of information from applications. Their technical approaches and governance scope differ from PIOS and EIOS; they are comparison points rather than interchangeable implementations. [S05, S29]

## 8. Evaluation and contribution

Test a workflow across a change of actor or implementation. Can the system preserve record identity, accepted state, source attribution and the correct represented principal? Can it distinguish personal work from entity work and refuse an out-of-scope request?

Include shared records, role changes and revoked delegation. Ask whether the human participants can explain who is represented and who is entitled to decide.

The contribution is a persistent principal model that separates purpose and information continuity from replaceable actors and software. Its value is practical clarity about who is served, what persists and how legitimate interaction continues when tools change.


## Sources and attribution

**[S01]** Valto Loikkanen and ChatGPT. *Define liquid software — shared conversation*. Retrieved 26 November 2026. [Original source](https://chatgpt.com/share/6b077626-c894-83ed-aabf-d21a363c4313).

**[S05]** Martin Kleppmann, Adam Wiggins, Peter van Hardenberg and Mark McGranaghan. *Local-first software: You own your data, in spite of the cloud*. Web essay April 2019; Onward! October 2019, pp. 154–178; DOI 10.1145/3359591.3359737. [Original source](https://www.inkandswitch.com/essay/local-first/).

**[S07]** peecos / Valto Loikkanen. *PIOS 2.0 master and public README*. PIOS 2.0; retrieved 26 November 2026. [Original source](https://www.peecos.org/pios/master).

**[S08]** Entity Core / Valto Loikkanen. *EIOS 1.0, Keel, and Weave*. Working master v1.4, 21 November 2026. [Original source](https://github.com/entity-core/eios/blob/main/spec/eios-1.0-master-documentation.md).

**[S10]** Private AI Exchange / PAIX. *Human & Agent Interoperability*. Non-normative design guidance for PAIX v0.1. [Original source](https://github.com/privateaiexchange/paix-spec/blob/main/docs/Human_Agent_Interoperability.md).

**[S15]** A2A Project. *Agent2Agent Protocol Specification*. Retrieved latest page identifies released version 1.0.0. [Original source](https://a2a-protocol.org/latest/specification/).

**[S17]** W3C Provenance Working Group. *PROV-DM: The PROV Data Model*. W3C Recommendation, 30 April 2013. [Original source](https://www.w3.org/TR/prov-dm/).

**[S29]** Solid Community Group. *Solid Protocol*. Draft Community Group Report, 12 May 2024. [Original source](https://solidproject.org/TR/protocol).

Valto Loikkanen supplies the conceptual synthesis and directs this collection. Codex prepared the research and prose. Definitions and reference models are editorial developments of the cited discussion, not claimed verbatim statements or universal first inventions. See the companion source register for exact read scope, versions and remaining gaps. This draft has not undergone independent peer review.
