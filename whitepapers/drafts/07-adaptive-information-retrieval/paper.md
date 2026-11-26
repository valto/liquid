# Adaptive Information Retrieval

*Evolving access structures around preserved evidence and actual questions*


**Conceptual source and direction: Valto Loikkanen.** Research and drafting: Codex (OpenAI), at his request. Research draft 1.0 · 26 November 2026.

## Abstract

Adaptive Information Retrieval separates durable information from the structures that make selected questions efficient to answer. Valto Loikkanen proposes combining intelligent discovery with evolving SQL projections, indexes, graphs and other access mechanisms according to actual demand. This paper defines that separation, explains the lifecycle of derived representations, and identifies the semantic, freshness and authority obligations that must survive changes in retrieval. It treats hybrid retrieval as a method-selection problem rather than a guarantee that more retrieval techniques produce better answers. [S01]

## 1. One source, several useful access paths

A preserved meeting record can support full-text search, a timeline, a graph of referenced commitments and an extracted table of dates. Each representation makes some questions easier. None automatically replaces the meeting record or becomes the complete account of what happened.

The architecture should allow the access structures to evolve as questions change. A recurring request about commitments may justify a specialized projection; a later request about reasons for a decision may require returning to the original discussion.

The stable concern is evidence and accepted meaning. The variable concern is how to find and assemble it efficiently.

## 2. What adaptive retrieval includes

**Adaptive Information Retrieval** is the governed selection, construction and revision of retrieval methods and representations according to observed needs, while preserving information authority and an attributable path to the relevant sources.

Adaptation can occur when serving a request or when improving the system over time. A request-time planner may combine exact lookup with semantic discovery. A maintenance process may identify repeated patterns and build an index or structured projection.

These are distinct activities. Choosing an existing method is not the same as changing a persistent access structure. The latter may affect other requests, resources and information exposure, and should be evaluated at that boundary.

## 3. Different structures preserve different questions

| Method | Typical strength | Important limitation |
| --- | --- | --- |
| Exact lookup | Stable identifiers and known records | Requires a known key or relation |
| Full-text retrieval | Terms present in source material | Different wording can obscure relevant evidence |
| Semantic retrieval | Conceptual similarity and discovery | Similarity does not establish factual support |
| Structured projection | Repeated filters and aggregation | Extraction choices can omit or misclassify meaning |
| Graph traversal | Explicit relationships and dependencies | Missing or inferred links require qualification |
| Spatial or temporal access | Location and sequence questions | Depends on captured context and resolution |

This table describes roles in the proposed architecture, not comparative benchmark results. Hybrid retrieval should choose methods for the question and data, then evaluate whether their combined result is actually useful.

## 4. A derived representation needs a declared lineage

A useful representation records its source set, source revisions, transformation method, schema or vocabulary, freshness policy and known limitations. It should distinguish copied facts from inferred assertions.

For an extracted commitment table, record the original passage and the definition used to classify it as a commitment. If a date is inferred, preserve that status. A later correction must be able to invalidate the relevant row without erasing the source or silently rewriting unrelated history.

PROV-DM provides a general model for describing entities, activities and agents in such provenance relationships. The collection uses it as a lineage reference, not as proof of source accuracy. [S17]

## 5. Canonical state and derived state

A rebuildable index is different from an accepted record. A structured event or approved decision may be authoritative in its own right. The distinction concerns the record's declared authority and lifecycle, not whether it resides in SQL, a graph or an object store.

PIOS's public documentation explicitly separates its Core from native processing and retrieval services. Rebuildable state can belong inside the information system while remaining outside the narrower canonical contract. Physical location and authority are separate concerns. [S07]

An optimizer must not promote a projection into canonical authority merely because it has become the fastest route. If the source changes, the system should either update the projection, mark it stale or return to another valid route.

## 6. Demand-driven specialization

The walking example becomes an illustrative retrieval case. One question about birds may justify interpreting a source interval. Repeated questions may justify a table of supported observations with source links. A broader environmental question may later use a different representation of the same originals.

Specialization should be evaluated over expected future demand, construction cost, update cost, storage, serving latency and correctness. A quiet but critical capability may need an access structure even without high frequency; a popular but unstable question may remain unsuitable for automatic extraction.

Learned-index research demonstrates that data-access structures themselves can be reconsidered using models. Its results concern particular indexing tasks and datasets, not unrestricted interpretation of arbitrary personal information. Codd's earlier data-independence argument likewise supports keeping logical information distinct from internal access organization. [S23, S18]

## 7. Access control survives optimization

A search index can reveal information even when it returns only snippets, counts or relationships. A cache can preserve an answer after access changes. Therefore, moving a request from intelligent retrieval to a projection cannot bypass the current disclosure boundary.

Authorization must apply to the relevant source and result scope. Shared representations may need recipient-specific filtering, while cached results need an appropriate policy identity and source revision. A faster answer with broader access is a different capability, not an optimization of the same one.

## 8. Acceptance and recovery

Test retrieval against questions with known source support, unsupported questions, ambiguous concepts and denied access. Include newly updated sources and stale structures. Measure precision of evidence, coverage, answer quality, freshness and total cost.

Then remove a selected derived structure in an isolated environment and verify that it can be rebuilt or that the fallback route fulfills the retained capability. Rebuildability is established by recovery evidence, not by labeling a folder derived.

A regression should be able to disable the faulty route without losing accepted originals or pending work. The endpoint may continue through a slower valid route, provided the agreed latency and quality conditions permit it.

## 9. Contribution and open questions

The proposed contribution is a lifecycle for retrieval representations governed by actual use, source authority and capability meaning. It complements source preservation by making rich evidence practical to use without fixing every future question at capture.

Open questions include how to detect semantic drift, select useful representations across changing workloads, control accumulated maintenance costs and communicate incomplete evidence. The architecture succeeds when it improves access while retaining the ability to inspect, correct and reinterpret what the system believes.


## Sources and attribution

**[S01]** Valto Loikkanen and ChatGPT. *Define liquid software — shared conversation*. Retrieved 26 November 2026. [Original source](https://chatgpt.com/share/6b077626-c894-83ed-aabf-d21a363c4313).

**[S07]** peecos / Valto Loikkanen. *PIOS 2.0 master and public README*. PIOS 2.0; retrieved 26 November 2026. [Original source](https://www.peecos.org/pios/master).

**[S17]** W3C Provenance Working Group. *PROV-DM: The PROV Data Model*. W3C Recommendation, 30 April 2013. [Original source](https://www.w3.org/TR/prov-dm/).

**[S18]** E. F. Codd. *A Relational Model of Data for Large Shared Data Banks*. Communications of the ACM 13(6), June 1970, pp. 377–387; DOI 10.1145/362384.362685. [Original source](https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf).

**[S23]** Tim Kraska, Alex Beutel, Ed H. Chi, Jeffrey Dean and Neoklis Polyzotis. *The Case for Learned Index Structures*. arXiv:1712.01208v3, 30 April 2018. [Original source](https://arxiv.org/html/1712.01208v3).

Valto Loikkanen supplies the conceptual synthesis and directs this collection. Codex prepared the research and prose. Definitions and reference models are editorial developments of the cited discussion, not claimed verbatim statements or universal first inventions. See the companion source register for exact read scope, versions and remaining gaps. This draft has not undergone independent peer review.
