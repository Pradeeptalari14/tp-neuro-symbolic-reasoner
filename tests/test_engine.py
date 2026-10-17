import pytest
from neuro_symbolic_prover import NeuroSymbolicVerifier, ClinicalAxiomKB

def test_kb_rules_loaded():
    rules = ClinicalAxiomKB.get_rules()
    assert len(rules) >= 3
    assert "Contraindicated" in rules[0]

def test_safe_treatment_verification():
    verifier = NeuroSymbolicVerifier()
    res = verifier.verify_treatment("Jane Roe", "Mild Hypertension", "Lisinopril", 20)
    assert res["allowed"] is True
    assert res["contraindicated"] is False
    assert res["proof_status"] == "SAT_PROOF_VALIDATED"
    assert res["toxicity_risk"] == "LOW"

def test_contraindicated_treatment_blocked():
    verifier = NeuroSymbolicVerifier()
    res = verifier.verify_treatment("John Doe", "Acute Renal Failure", "Metformin", 1000)
    assert res["allowed"] is False
    assert res["contraindicated"] is True
    assert res["proof_status"] == "UNSAT_COUNTEREXAMPLE_BLOCKED"
    assert res["toxicity_risk"] == "HIGH"
    assert len(res["active_rules_fired"]) >= 2
