# A1/A2 Git commit vs tree object identity — post-merge erratum (2026-10-28)

Record Type: POST_MERGE_EVIDENCE_IDENTIFIER_ERRATUM
Repository: lostlight530/reflective-continuum
Logical maintenance day: 2026-10-28 Asia/Shanghai
Original A1 record: `historical-audits/2026-10/2026-10-28-a1-source-custody.md`
Original A2 record: `historical-audits/2026-10/2026-10-28-a2-month-relation.md`
Status: CORRECTED_OBJECT_TYPE_LABEL / SOURCE_CUSTODY_UNCHANGED

## Exactly scoped factual correction

The earlier A1/A2 text uses the phrase **Git tree SHA** for an SHA that, in the connected `git/trees/main?recursive=1` result, tracked the resolved **branch HEAD commit**. These object types must not be conflated. The right revision pair was used to read files and the per-file Git blob SHAs remain independently checkable. The erroneous *object-type label* is corrected here without rewriting historical A1 or A2 documents.

| Source-time baseline | Commit SHA (recorded ref) | Actual Git tree object SHA (`commit.tree.sha`) |
|---|---|---|
| A1 before merge, Oct1..27 | `912ccf70617620471920cb73e515f614e9e5c715` | `ef18f06e9b3b1cd2db9c3c32ed670d887616cd40` |
| A2 after A1 merges, Oct1..28 | `4a1bb56a14b6069edd305cbe545283b261eef84f` | `02638f030954be16224c9c4e3737c75f974f0f2e` |

Evidence source: GitHub Commit REST API `GET /repos/lostlight530/reflective-continuum/commits/{sha}`, separately inspecting `sha` and `commit.tree.sha` for both exact base commits, compared to the earlier recursive file-tree ref response. GitHub evidence read, not a local Git command or an original scientific rerun.

## Unchanged outcomes and governance

- A1/N−1 and A2/N PRs remain separate completed maintenance events at their exact prior merge commits.
- The 28-day A2 path census and individual file/Blob identities are **not** converted into runtime or historical original-producer proof.
- No original Jules, Web GPT, Stage, native research, weekly or monthly record is replaced or re-attributed.
- Month OCTOBER_OPEN, no natural-month final or research credit added.
- CLI/host/independent semantic and external-effect verification still NOT_EXECUTED where originally recorded.
- This erratum corrects the type label only; the claimed A1-before-A2 chain and scientific outcomes are not upgraded.
- Future evidence records should name three independent identity classes explicitly: `COMMIT_OID`, `TREE_OID`, `BLOB_OID`.
- Verification gate for this erratum: two commit objects fetched, two distinct tree OIDs matched their own `commit.tree.sha` fields; original records left byte-for-byte unchanged.
- This is a post-merge evidence-class correction, not the original base-repair phase, and does not create a new A1 or A2.
