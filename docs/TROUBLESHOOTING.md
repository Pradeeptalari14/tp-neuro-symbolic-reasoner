# Incident Triage & Troubleshooting Runbook — Neuro-Symbolic Logic Reasoner Studio

> **Severity Tier:** P1 - P3 SRE Operational Runbook  
> **Maintainer:** Talari Pradeep (Platform Architecture)

---

## Common Incident Signatures

### Incident 1: `Z3 Solver UNKNOWN or Timeout (>5000ms)`
- **Symptom & Alert:** Pipeline telemetry breaches critical threshold or logs failure signature.
- **Root Cause Analysis:** Non-linear real arithmetic or unbounded quantifiers causing undecidability.
- **Standard Operating Remediation:**
  ```bash
  # Step 1: Diagnose current state
  python main.py --diagnose

  # Step 2: Remediate configuration
  Refactor FOL axioms into decidable fragments (e.g. Presburger arithmetic or quantifier-free Horn clauses).
  ```


### Incident 2: `Symbolic Grounding Type Mismatch`
- **Symptom & Alert:** Pipeline telemetry breaches critical threshold or logs failure signature.
- **Root Cause Analysis:** Neural extraction failed to normalize medication generic and brand aliases.
- **Standard Operating Remediation:**
  ```bash
  # Step 1: Diagnose current state
  python main.py --diagnose

  # Step 2: Remediate configuration
  Apply canonical RxNorm / MeSH ontology dictionary normalization before grounding.
  ```


---

## Emergency Escalation Protocol
1. **L1 Triage:** Verify pod status via `kubectl get pods -l app=neuro-symbolic-reasoner`.
2. **L2 Deep Dive:** Check container logs via `kubectl logs -l app=neuro-symbolic-reasoner --tail=100`.
3. **L3 Incident Lead:** Contact `pradeeptalari14@gmail.com` for critical containment breaches.
