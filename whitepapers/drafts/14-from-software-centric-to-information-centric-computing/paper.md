# From Software-Centric to Information-Centric Computing

*A transition that preserves source authority while changing the working environment*


**Conceptual source and direction: Valto Loikkanen.** Research and drafting: Codex (OpenAI), at his request. Research draft 1.0 · 26 November 2026.

## Abstract

Information-centric computing makes information identity, provenance, capability meaning and human authority more durable than a particular application. Valto Loikkanen's synthesis suggests reversing several historical dependencies: capture should preserve useful evidence, presentation should follow context, and implementation should follow actual need. This paper examines how existing systems can move toward that model incrementally. It distinguishes source preservation from bulk accumulation, information continuity from a single database, and a successful export from a proven replacement. [S01]

## 1. The application as both tool and container

An application often bundles information, permissions, presentation and operational logic. This can provide a coherent product, but it can also make the user's information dependent on the product's lifecycle and choices.

The transition proposed here separates these concerns enough to preserve continuity while retaining useful applications. A particular interface may remain the best working surface. The information system should nevertheless know what the records mean, where they came from and how they can survive a change of surface.

Information-centric does not mean interface-free or code-free. It identifies what should retain authority and identity as tools evolve.

## 2. Three dependencies to reconsider

| Current dependency | Transition question |
| --- | --- |
| Capture is limited to anticipated fields | What original evidence should survive beyond current queries? |
| Presentation determines the accessible information | Can the same source support contextually different views? |
| A dedicated implementation precedes every useful activity | Can a bounded intelligent capability serve the emerging need? |

These are questions about priorities, not universal descriptions of every historical system. Many existing systems already separate logical information, storage and views. Codd's data-independence argument is an important antecedent. [S18]

The opportunity is to extend that separation across the user's information, interactions and evolving implementations, rather than treating it only as a database optimization.

## 3. Declare what is authoritative

Before changing a workflow, identify original records, accepted revisions, governing documents, derived assertions and pending work. Record which source is authoritative for each purpose.

A retrieved summary is not automatically an accepted revision. An export is not automatically the new source of truth. A cache may contain pending work that has never been accepted elsewhere. Losing that distinction can create competing masters or delete the only copy of an intended change.

PIOS's public framework separates canonical Core, native processing and retrieval, external applications and physical placement. EIOS distinguishes originals, knowledge and use. These illustrate how logical boundaries can remain explicit even within one deployment. [S07, S08]

## 4. A bounded adoption unit

Choose one capability and a defined information set. For example, let a user browse and revise a selected class of notes through an additional working surface while preserving original identity, revision history and conflict handling.

The required boundary includes full-content readback, meaningful updates, source attribution, acceptance, replay handling and recovery. A successful screen demonstration proves only part of this boundary.

This is a hypothetical adoption example. The paper does not authorize a migration, assert that a particular product supports it, or change an existing owner's source authority.

## 5. Preservation without indiscriminate accumulation

Source preservation should follow purpose and retention choices. Rich material can support new interpretation, but retaining every available file does not guarantee useful context.

Microsoft's MyLifeBits research offers a historical comparison: lifetime personal storage and richer annotation were pursued alongside SQL Server-based retrieval. It illustrates that rich preservation and relational access can coexist. It does not prove that preserving all possible information is desirable or that every future question becomes answerable. [S27]

The transition should retain appropriate originals, record their context and make derived interpretations attributable. It should also identify material deliberately excluded or no longer retained.

## 6. Portability needs more than bytes

An information package can contain files yet fail to preserve meaning. Relationships, accepted state, source versions, annotations and pending revisions may be needed to reconstruct the useful capability.

Likewise, a provider change may require re-establishing credentials and delegated authority. A content export should not imply that access grants or external commitments have automatically transferred.

Local-first research provides important principles for ownership, longevity and usable offline work. Its design emphasis differs from a server-packaged information system, but the continuity test is relevant: can useful work survive the loss or replacement of the current service? [S05]

## 7. Introduce adaptability where it serves a real need

Once the selected information and capability boundary are reliable, add one contextual presentation or retrieval route. Preserve the conventional route as a baseline where useful.

Observe whether the new route improves a meaningful outcome. Repeated needs may justify specialization. A novel question may remain best served through intelligent interpretation. The system should permit both without promoting a derived view into authority.

Documentation and capability requirements can maintain shared meaning through these changes. Their revisions should follow the relevant source authority rather than be inferred from whatever the latest implementation happens to do. [S09]

## 8. Acceptance, recovery and eventual replacement

Acceptance should cover the selected user's actual outcome: information is readable, intended changes are accepted correctly, conflicts remain safe, and the capability can be recovered. Source release or deletion is a later decision supported by the relevant verification and authority.

An isolated reconstruction is useful evidence. It should demonstrate recovery from the retained authoritative package, not depend silently on the original live application's cache.

End-to-end design reasoning explains why component-level success is insufficient. The meaningful outcome may cross source acceptance, network delivery and user acknowledgement. [S20]

## 9. Evaluation and contribution

Measure continuity across a change of working surface or implementation, including semantic fidelity, conflict behavior, recovery effort and user comprehension. Compare the transition cost with actual gains in use and flexibility.

The contribution is a gradual transition model that preserves source authority while reducing application dependence. It provides a path between an ambitious information-centric vision and a bounded useful capability, without requiring a whole-world migration before any benefit can be realized.


## Sources and attribution

**[S01]** Valto Loikkanen and ChatGPT. *Define liquid software — shared conversation*. Retrieved 26 November 2026. [Original source](https://chatgpt.com/share/6b077626-c894-83ed-aabf-d21a363c4313).

**[S05]** Martin Kleppmann, Adam Wiggins, Peter van Hardenberg and Mark McGranaghan. *Local-first software: You own your data, in spite of the cloud*. Web essay April 2019; Onward! October 2019, pp. 154–178; DOI 10.1145/3359591.3359737. [Original source](https://www.inkandswitch.com/essay/local-first/).

**[S07]** peecos / Valto Loikkanen. *PIOS 2.0 master and public README*. PIOS 2.0; retrieved 26 November 2026. [Original source](https://www.peecos.org/pios/master).

**[S08]** Entity Core / Valto Loikkanen. *EIOS 1.0, Keel, and Weave*. Working master v1.4, 21 November 2026. [Original source](https://github.com/entity-core/eios/blob/main/spec/eios-1.0-master-documentation.md).

**[S09]** Valto Loikkanen. *Capability Documentation / Capability Requirements Document framework*. Draft 0.4; package 0.8.0. [Original source](https://valto.github.io/crd/specification.html).

**[S18]** E. F. Codd. *A Relational Model of Data for Large Shared Data Banks*. Communications of the ACM 13(6), June 1970, pp. 377–387; DOI 10.1145/362384.362685. [Original source](https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf).

**[S20]** J. H. Saltzer, D. P. Reed and D. D. Clark. *End-to-End Arguments in System Design*. ACM Transactions on Computer Systems 2(4), November 1984, pp. 277–288. [Original source](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf).

**[S27]** Microsoft Research; Gordon Bell, Jim Gemmell and Roger Lueder. *MyLifeBits — project overview and publication list*. Project established 2 November 2001; overview retrieved 26 November 2026. [Original source](https://www.microsoft.com/en-us/research/project/mylifebits/).

Valto Loikkanen supplies the conceptual synthesis and directs this collection. Codex prepared the research and prose. Definitions and reference models are editorial developments of the cited discussion, not claimed verbatim statements or universal first inventions. See the companion source register for exact read scope, versions and remaining gaps. This draft has not undergone independent peer review.
