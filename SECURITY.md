# Security Policy

Security fixes target current `main`. Historical research is a separately owned record and may not receive retroactive correction.

Report suspected vulnerabilities through GitHub private vulnerability reporting when available, otherwise through the repository owner’s private GitHub profile contact route. Include commit/path, prerequisites, minimal reproduction, impact, and mitigation. Remove credentials and unnecessary personal or database content. Do not open a public exploit issue.

Maintainers should acknowledge within 7 days and provide triage status within 14 days when capacity permits; these are targets, not guarantees.

This library is not an authentication, authorization, isolation, secret-management, or distributed-consensus system. Callers must restrict database paths and permissions, validate untrusted content, bound queries and resources, protect backups, and define retention. FTS5 is lexical search, not a semantic-safety filter. Error output exposes types and aggregate state, not payloads by default.

Actions use minimal job permissions and immutable full commit SHAs. Pull-request code receives no write credential. Security claims require a threat model and adversarial verification beyond ordinary unit tests.