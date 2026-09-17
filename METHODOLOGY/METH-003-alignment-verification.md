> [!NOTE]
> **Current architecture interpretation — 2026-09-18**
> - **Subject class:** `METHOD`
> - **Role:** Current methodology for **alignment verification**
> - **Authority:** Repository-native method authority for the procedure, measurement, reconciliation rule, assumptions, and failure semantics explicitly defined here
> - **Current meaning:** Treat the procedure as a method contract, not evidence that it ran at the current revision. Historical R2/failure ranges remain historical ranges rather than present-state guarantees
> - **Evidence / implementation boundary:** Detection, drift, alignment, rollback, or reconciliation vocabulary is bounded by implemented mechanics: lexical search is not semantic proof, savepoints are not external rollback, and repeated digests are not convergence evidence
> - **Cross-document relation:** Specification/runtime code bound mechanics; ADRs explain decisions; Evidence Baseline and periodic artifacts provide dated observations without redefining the method
> - **Update trigger:** Update when mechanics, thresholds, evidence ranges, or reconciliation semantics materially change
> - **Preservation rule:** Existing subject history and dated examples retain their original time boundary. This pass clarifies current interpretation and corrects only confirmed current-authority drift

# Claim and source support review

- Method version: 2026-08-24
- Scope: repository behavior, research records, and external-source propositions

## Objective

Determine what an exact evidence surface supports without collapsing ingestion, local execution, persistence, source authority, and factual support into one “alignment” result.

## Inputs

- exact claim/proposition
- repository artifact or implementation surface relevant to the claim
- source identity/version when external evidence is used
- observation/revision/time boundary
- known counterevidence or unresolved fields

## Procedure

1. Classify the claim as local implementation, local observation, external proposition, inference, or continuity claim.
2. Select the evidence surface that actually bears on that claim.
3. For external material, separate source identity/authority from whether the source supports the exact proposition.
4. For local behavior, keep store/query/version/fixture scope explicit.
5. Preserve rejected signals, errors, missing fields, and conflicting evidence.
6. Narrow the wording when the evidence supports only a weaker proposition.
7. Use `SOURCE_CLAIM_MISMATCH` when the cited source does not support the stored proposition.
8. Use an unresolved state rather than inferring persistence when object identity is not linked.

## Outputs

- bounded claim text
- evidence surface
- claim-support state
- local implementation/observation state where relevant
- unresolved/untested dimensions

## Failure conditions

The procedure fails closed when the compared versions, query, PageRank configuration, threshold, or retained output is missing, or when a structural/lexical/rank result is promoted into semantic truth, safety, or general alignment.

## Required distinctions

- `ACCEPTED` != source truth
- `REJECTED_FROM_INGESTION` != source falsification
- selfcheck pass != historical health
- lexical top-result stability != semantic equivalence
- repeated snapshot digest != durable memory
- source reachability != proposition support

## Evidence boundary

This method bounds evidence strength. It does not make the repository an alignment evaluator or prove a global safety property.
