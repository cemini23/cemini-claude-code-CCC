---
title: "Enterprise MCP authentication gateway architecture"
type: source
tags: [source, arxiv, mcp, auth, gateway, enterprise, k271]
keywords: [2608.10760, MCP-gateway, BYOT, GYOT, OAuth, persona]
related:
  - concepts/enterprise-mcp-auth-gateway.md
  - entities/tools/enterprise-mcp-auth-gateway.md
  - concepts/schema-bound-mcp-tool-surface.md
  - concepts/mcp-claim-validation-and-parameter-grounding.md
  - sources/brief-k270-k273-mcp-acm-wave-2026-08-12.md
  - briefs/2026-08-12_ccc-handoff-k270-k273-ingest.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
---

## Relations

- `@concepts/enterprise-mcp-auth-gateway.md`
- `@entities/tools/enterprise-mcp-auth-gateway.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | A Gateway Architecture for Enterprise MCP Authentication |
| **arXiv** | 2608.10760 |
| **Authors** | Kumar, Wang, Manoharan (Enterprise AI Platform Engineering) |
| **Code** | No public artifact at Phase-0 |
| **Retrieved** | 2026-08-12 |

## Narrative

Industry deployment: centralized MCP gateway fronts heterogeneous servers. Two-axis auth (**persona** user vs non-user × **credential** no-auth/API-key/OAuth/client-credentials/…). Gateway SSO grants + BYOT/GYOT/RFC 8693 token exchange. Three identity flows: User→OAuth2, Non-user→Service-Account, User→Service-Account.

| Verdict | **ADOPT** gateway + persona/credential model. **NO-GO** code (none). |

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.10760-a-gateway-architecture-for-enterprise-mcp-authen.pdf`
