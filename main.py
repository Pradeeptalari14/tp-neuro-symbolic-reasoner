#!/usr/bin/env python3
"""
Canonical CLI Entrypoint for Neuro-Symbolic Logic Reasoner Studio
"""
import sys
import neuro_symbolic_prover as engine

def main():
    print("=" * 60)
    print("🚀 Neuro-Symbolic Logic Reasoner Studio")
    print("=" * 60)
    if hasattr(engine, '__main__'):
        pass
    print("Executing engine drill...")
    # Trigger standalone block
    with open("neuro_symbolic_prover.py", "r") as f:
        code = compile(f.read(), "neuro_symbolic_prover.py", "exec")
        exec(code, {"__name__": "__main__"})

if __name__ == "__main__":
    main()
