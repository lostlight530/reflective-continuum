# Security Policy


Security fixes target current `main`. Historical research is a separately owned record and may not receive retroactive correction.

Report suspected vulnerabilities through GitHub private vulnerability reporting when available, otherwise through the repository owner’s private GitHub profile contact route. Include commit/path, prerequisites, minimal reproduction, impact, and mitigation. Remove credentials and unnecessary personal or database content. Do not open a public exploit issue.

Maintainers should acknowledge within 7 days and provide triage status within 14 days when capacity permits; these are targets, not guarantees.

This library is not an authentication, authorization, isolation, secret-management, or distributed-consensus system. Callers must restrict database paths and permissions, validate untrusted content, bound queries and resources, protect backups, and define retention. FTS5 is lexical search, not a semantic-safety filter. Error output exposes types and aggregate state, not payloads by default.

Actions use minimal job permissions and immutable full commit SHAs. Pull-request code receives no write credential. Security claims require a threat model and adversarial verification beyond ordinary unit tests.

## 私密漏洞报告与数据保护 / Private disclosure and data boundaries

中文：不得在公开 Issue、PR、运行日志或科研档案中公布凭据、私人图谱内容或未修复漏洞详情；使用本仓既有的私密通报渠道；事务回滚、哈希、路径检查和样例成功只覆盖特定范围，不证明外部数据可信、持久自治或全面安全

English: Do not publish credentials, private graph content or unpatched exploit details in public issues, PRs, logs or research archives; use the existing private reporting route. Transaction rollback, hashes, path checks and fixed-fixture success are scope-bounded, not proof of external data trust, durable autonomy or universal safety

