# Reflective Continuum Governance Map

Calibration: 2026-09-17

`GOVERNANCE/` is the repository-native maintenance/control-plane entry point. It routes public maintenance, independent review, retained governance design material, and memoryless Independent GPT recovery without replacing implementation, evidence contracts, research content, or private Jules task controls.

## Current control-plane surfaces

- `MAINTENANCE.md` — canonical public maintenance contract.
- `INDEPENDENT_REVIEW.md` — reviewer-side interpretation state machine; non-operative and distinct from maintenance delivery.
- `independent-gpt/README.md` — cold-start recovery and bounded-repair kernel for a memoryless Independent GPT reviewer.
- `plans/` and `specs/` — retained governance design/specification material in their declared status; not routine maintenance edit targets.

## Evidence inputs, not maintenance edit targets

The following surfaces may be read when needed to verify a maintenance claim, but this governance router does not authorize changing them merely because a maintenance review is running:

- current implementation / tests;
- `../EVIDENCE_BASELINE.md`, `../ADR/`, `../METHODOLOGY/`;
- `../RESEARCH/` Daily / Weekly / Monthly research and execution records;
- `../historical-audits/INDEX.md` and retained point-in-time records.

A repository-native owning contract may explicitly require synchronization with one of those surfaces. Otherwise, keep the maintenance repair inside the maintenance/control plane.

## Authority rule

For maintenance work, recover repository truth first and use the most specific current owner:

```text
current merged main / current implementation facts
> current subject-specific repository contract
> canonical repository maintenance contract
> verified revision-matched execution / runner evidence
> current governance interpretation
> historical point-in-time evidence / prior handoff / model recollection
```

`INDEPENDENT_REVIEW.md` can calibrate interpretation, but it does not outrank the current owning contract or become runtime authority.

A private Jules task definition may instruct a producer, but it is not automatically a public repository authority and must not be copied into public files unless the maintainer explicitly chooses to publish it.

## Runner terminology

GitHub Actions and other repository automation are runner/deployment/lifecycle evidence only when their execution is actually observed for the relevant revision. A workflow definition is not an executed result; an unrun checker is `NOT_EXECUTED`; no workflow result is a universal correctness certificate.

## Separation

```text
native Jules production != Independent GPT
Independent review != Independent GPT maintenance delivery
Independent GPT != GitHub Actions
GitHub Actions != semantic or scientific truth
maintenance control plane != research content plane
historical record != current state
current path presence != earlier execution
correction != history rewrite
public governance != private task controls
```

## Delivery rule

No confirmed maintenance defect means `NO_CHANGE_REQUIRED` and no activity-only PR. A justified maintenance repair changes the owning control-plane file(s), verifies only what can actually be executed, refreshes current `main`/overlap state, opens one Draft PR, and stops for maintainer review.

Final doctrine and merge authority remains with the maintainer.
