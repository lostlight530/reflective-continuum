## 每个 Reference 的状态

- `REFERENCES/INDEX.md`: `UNRESOLVED_ORPHAN`
- `REFERENCES/PIONEERS/PIO-001-Google_DeepMind.md`: `GRAPH_INTEGRATED_REFERENCE`
- `REFERENCES/PIONEERS/PIO-002-Google_Paper_Interpretations.md`: `GRAPH_INTEGRATED_REFERENCE`
- `REFERENCES/PIONEERS/PIO-003-Other_Pioneers.md`: `GRAPH_INTEGRATED_REFERENCE`
- `REFERENCES/PIONEERS/PIO-004-Anthropic_OpenAI.md`: `GRAPH_INTEGRATED_REFERENCE`

*说明*：PIONEERS 文件已被 `REFERENCES/INDEX.md` 引用，因此它们在局部图谱内属于 `GRAPH_INTEGRATED_REFERENCE`。然而，由于没有任何外部文件（如 `SPECIFICATION.md` 或 `ADR/INDEX.md`）链接到 `REFERENCES/INDEX.md`，所以 `REFERENCES/INDEX.md` 自身处于 `UNRESOLVED_ORPHAN` 状态。

## ADR Chain

- 存在有效链接的 ADR 集合：`ADR-001` 到 `ADR-010` 均被 `ADR/INDEX.md` 引用。
- `README.md` 包含指向 `ADR/INDEX.md` 的有效链接。
- ADR 编号无错误（无断层或命名规范错误）。
- 无破损的 ADR 内部链接。

## SPEC ↔ ADR

- 映射缺失：`SPECIFICATION.md` 中完全没有包含指向 `ADR-xxx.md` 或 `ADR/INDEX.md` 的显式 Markdown 引用。
- 虽然 `ADR/INDEX.md` 反向链接到 `../SPECIFICATION.md`，但从 SPEC 到 ADR 的正向拓扑未能建立。

## Ghost Chains

- `REFERENCES/INDEX.md` 内存在如下断言的 Ghost Chains：
  1. 声明 `SPECIFICATION.md links to this reference map for non-normative context`
  2. 声明 `ADR/INDEX.md links to this reference map and keeps ADR decisions separate from background material`
  经过审查，`SPECIFICATION.md` 与 `ADR/INDEX.md` 均无指向 `REFERENCES/INDEX.md` 的实际链接，因此这些均为幽灵引用（Ghost Chains）。

## Orphans

- `REFERENCES/INDEX.md`：因未能被架构核心文档有效链接而成为 `UNRESOLVED_ORPHAN`。

## Recommended Additions

- 在 `SPECIFICATION.md` 中补充指向 `ADR/INDEX.md` 的引用链接。
- 在 `SPECIFICATION.md` 和 `ADR/INDEX.md` 中补充指向 `REFERENCES/INDEX.md` 的引用链接，以消除 Ghost Chains 和孤儿节点。

## 证据不足项

- 无。所有的拓扑链接情况均已由明确的提取所验证。
