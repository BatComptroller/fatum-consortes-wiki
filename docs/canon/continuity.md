---
canon_mode: CANON-LOCK
continuity_flag: OK
version: 2026.1
updated: 2026-02-07
tags:
  - canon
  - continuity
  - governance
related:
  - /canon/canon-rules/
  - /index/
---

# Continuity System

This page defines how canon is validated, updated, and repaired under **MYTHRAEL INFINITA v7**.

## Continuity Flags (Required)
### OK
Aligned with CANON-LOCK canon. No action required.

### Minor Tension
A variance exists but is explainable without rewriting canon.
**Required:** Add a short “Continuity Note” explaining the variance.

### Contradiction
Direct conflict with CANON-LOCK canon.
**Required:** Resolve using one of the options below.

## Resolving Contradictions (Canon-Safe Paths)
When a Contradiction is detected, apply one of:

1) **Text Fix**
Update the conflicting page(s) so facts match CANON-LOCK.

2) **Canon Patch Page**
Create a dedicated patch entry that explains:
- what changed
- why it changed
- what remains invariant
and update affected pages to reference it.

3) **Reclassification**
If the page is intentionally divergent, reclassify it:
- CANON-LOCK → BRIDGE-TEST or ELSEWORLDS
and label deviations.

## BRIDGE-TEST → CANON-LOCK Promotion
A BRIDGE-TEST proposal may be promoted to CANON-LOCK only when it includes:
- **Ripple Warnings**
- **Rollback Plan**
- **Change Ledger (Cause → Effect → Echo)**
and is accepted as the new authoritative resolution.

## Canon Update Discipline
- Major revisions must increment `version` and update the `updated:` date.
- Every significant change should include a Change Ledger section.

## Change Ledger Standard
**Cause → Effect → Echo**
- **Cause:** Why the change was needed
- **Effect:** What changed in canon
- **Echo:** Downstream implications (pages impacted, motifs altered, future hooks)

## Retrieval Audit (Mythrael v7)
In CANON-LOCK and BRIDGE-TEST, Mythrael must:
1) retrieve canon via wiki actions,
2) cite the slug(s) used,
3) emit Continuity Flags when conflicts exist.
