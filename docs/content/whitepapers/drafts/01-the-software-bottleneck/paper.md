# The Software Bottleneck

*How implementation rigidity shapes the opportunities people can pursue*


**Conceptual source and direction: Valto Loikkanen.** Research and drafting: Codex (OpenAI), at his request. Research draft 1.0 · 26 November 2026.

## Abstract

Software can constrain activity when adapting it costs more than the value of a particular need. Valto Loikkanen identifies this rigidity as a structural bottleneck and argues that intelligence may make adaptation responsive to actual demand. This paper defines the bottleneck, identifies its economic mechanism and distinguishes coding speed from useful flexibility. It proposes measurements that include lost opportunities, workarounds, maintenance and human attention. The argument is conditional: reducing implementation friction can move constraints elsewhere without eliminating them. [S01]

## 1. Needs that never become features

A user wants a report that combines several sources for a decision this afternoon. The desired report is understandable, but no application provides it. A developer could build the feature, yet specification, integration and maintenance make the request too expensive. The user accepts an incomplete view, creates a manual workaround or abandons the question.

This is an illustrative case, not an empirical observation from a named organization. It exposes a demand that ordinary software metrics may miss. A feature backlog records some requests; it rarely records all questions people stopped asking because they expected the answer to be impractical.

Define the **software bottleneck** as the constraint arising when the availability, cost or adaptability of implementations limits an otherwise meaningful and authorized activity. It can appear in development queues, rigid information models, integration gaps and the cognitive effort of navigating tools.

## 2. The economic mechanism

An adaptation is pursued when its expected benefit exceeds development, coordination, operation and maintenance costs. Centralized products therefore prioritize needs shared by many users. Specialized requests may remain below the commercial threshold even when they are valuable to a particular person or group.

The result is not simply missing features. Users reshape their processes around the product: they enter data in the offered categories, perform extra steps, or omit useful distinctions. The tool influences which activities seem possible and which information survives. Loikkanen's broader thesis is that this influence can extend to organizational and market arrangements. That extension requires evidence beyond a coding demonstration. [S01]

Ink & Switch's malleable-software research offers related accounts of users adapting their workflows to inflexible tools. Its emphasis is user agency and modification at the point of use. The present paper frames the resulting adaptation gap as a constraint on pursuing opportunities. [S04]

## 3. Coding speed is one part of flexibility

Generating a working script more quickly can reduce a particular cost. It does not resolve ambiguous requirements, inaccessible information, integration authority, security obligations or long-term support. Brooks's distinction between difficulties intrinsic to a system's conceptual design and difficulties of representing it remains a useful counterweight to sweeping automation claims. [S19]

Useful flexibility has at least four dimensions:

- **Expression:** can someone communicate the actual need without learning the internal model of an application?
- **Fulfillment:** can the system assemble an appropriate capability from available information and tools?
- **Adaptation:** can the implementation change while preserving meaningful behavior and accepted work?
- **Continuity:** can the user retain information and commitments when a tool or provider changes?

A system may improve one dimension while worsening another. A custom interface might be easy to generate but impossible to maintain; a broad agent might understand requests but lack reliable access to the necessary records.

## 4. Where intelligence may change the threshold

Intelligence can help interpret an unfamiliar request, find relevant information, compose existing tools and produce a temporary interface. Repetition can then justify a specialized implementation. This sequence changes the threshold for serving an emerging need: usefulness can be established before committing to a permanent feature.

The claim is not that every need should begin with an agent. A proven deterministic capability may already be cheaper and more dependable. The proposed opportunity is to avoid requiring a new predefined implementation for every variation before any value can be delivered.

A recurring request for overdue commitments illustrates the mechanism. Initially, an agent might reconcile a few source documents. Later, consistent definitions and frequent demand may justify a structured projection and direct query. The capability becomes cheaper to serve while its original evidence remains available.

## 5. Measuring the bottleneck

| Measurement | Why it matters |
| --- | --- |
| Time from expressed need to useful result | Captures adaptation delay |
| Abandoned or deferred meaningful requests | Reveals demand omitted from shipped-feature metrics |
| Manual coordination and re-entry | Captures work displaced onto users |
| Total cost over a realistic period | Includes maintenance and validation |
| Decision quality and source coverage | Prevents speed from substituting for usefulness |
| Recovery and provider-switching effort | Measures continuity beyond first success |

A study should compare a stable baseline with a bounded adaptive alternative using similar tasks and participants. It should include negative results and failures. A demonstration that a tool can be generated is evidence of possibility; it does not establish sustained productivity or social impact.

Research on generative AI at work provides a useful reminder that benefits can vary by task and worker experience. The customer-support study by Brynjolfsson, Li and Raymond concerns a specific assistance setting, not liquid architectures across the economy. [S24]

## 6. Counterarguments

Standardization can be beneficial. It supports training, coordination, safety and comparability. A process that appears rigid may encode a deliberate agreement rather than a technical limitation. Before modifying it, distinguish unnecessary implementation constraints from legitimate shared rules.

Customization also has costs. People may struggle to learn continuously changing interfaces. Generated components can create dependency and support burdens. An adaptive system can become a more powerful monopoly if it owns the user's information, terminology and relationship history.

Finally, a bottleneck can move. Faster software production may expose unclear objectives, limited trust, fragmented authority or inadequate information. Solving implementation friction is valuable even when these remain, but it should not be reported as their solution.

## 7. Research and practical implications

Organizations can start by mapping where meaningful requests are blocked and why. A selected case should identify the information required, the actor authorized to act, the cost of the existing workaround and the smallest useful adaptation.

The central hypothesis is falsifiable: within an appropriately bounded domain, intelligence-assisted adaptation should make a wider range of useful needs serviceable at an acceptable total cost. The stronger societal thesis requires longitudinal evidence about agency, economic opportunity, concentration and outcomes.

The paper's contribution is to make the adaptation gap visible as an object of research. Liquid Software supplies one response to that gap; adaptive interfaces address expression; information preservation supports future fulfillment; and decision freedom addresses authority. None independently guarantees that the bottleneck disappears.


## Sources and attribution

**[S01]** Valto Loikkanen and ChatGPT. *Define liquid software — shared conversation*. Retrieved 26 November 2026. [Original source](https://chatgpt.com/share/6b077626-c894-83ed-aabf-d21a363c4313).

**[S04]** Geoffrey Litt, Josh Horowitz, Peter van Hardenberg and Todd Matthews. *Malleable Software: Restoring User Agency in a World of Locked-Down Apps*. June 2025. [Original source](https://www.inkandswitch.com/essay/malleable-software/).

**[S19]** Frederick P. Brooks, Jr.. *No Silver Bullet: Essence and Accidents of Software Engineering*. UNC technical report TR86-020, September 1986. [Original source](https://www.cs.unc.edu/techreports/86-020.pdf).

**[S24]** Erik Brynjolfsson, Danielle Li and Lindsey R. Raymond. *Generative AI at Work*. NBER Working Paper 31161, April 2023, revised November 2023; published QJE 140(2), 2025, pp. 889–942. [Original source](https://www.nber.org/papers/w31161).

Valto Loikkanen supplies the conceptual synthesis and directs this collection. Codex prepared the research and prose. Definitions and reference models are editorial developments of the cited discussion, not claimed verbatim statements or universal first inventions. See the companion source register for exact read scope, versions and remaining gaps. This draft has not undergone independent peer review.
