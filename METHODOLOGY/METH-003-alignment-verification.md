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

## Required distinctions

- `ACCEPTED` != source truth
- `REJECTED_FROM_INGESTION` != source falsification
- selfcheck pass != historical health
- lexical top-result stability != semantic equivalence
- repeated snapshot digest != durable memory
- source reachability != proposition support

## Evidence boundary

This method bounds evidence strength. It does not make the repository an alignment evaluator or prove a global safety property.