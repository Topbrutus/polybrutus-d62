# Polybrutus D62 — proof-first validation and controlled publication

1. Direct scientific parent D61 frozen v0.1.0 peeled Git commit 71d35c075a5cd5dd83b08a619da6a7d051f85b2d, DOI 10.5281/zenodo.24432096, entire original source ZIP SHA256 10f1bd016a0f8737d5f2b7e4e6587b9bb71bd7a8c6657e09c70f713848e7d721, certificate SHA256 34213ec5e18c06a698cd752c55d2259c7d528f85bf1f211f82c11d1cd7727725. Both exact programs validate original ZIP SHA/CRC, original certificate bytes and inherited labels.
2. Exhaust all 67 norm-one points and 2211 labelled exact squared distances; 2145 unchanged old D61 pairs and 66 new squared distances 2R²; Euclidean Gram and centered Gram PSD rank 62.
3. Two independent implementations (SymPy exact Gram vs fractions.Fraction separate pair rules), four adversarial negative controls, exact deterministic certificate. Chosen dimensionless ideal graph eigenvalue 67/2 mult 56 and 33 mult 4.
4. Scientific GitHub initial main CI must pass, then freeze source tag v0.1.0 and require tag CI green; after public Zenodo DOI document on main and require third green CI.
5. Public Zenodo originals: full frozen Git scientific source ZIP, two-page mathematical PDF and exact deterministic certificate JSON; all 3 filenames, sizes and MD5 from public API match SHA256-verified originals. Nine current D62 sixty-two/fifty-sixfold keywords, structured isDerivedFrom direct D61 DOI, separate D61/D7 textual bibliography.
6. Preserve entire historic original source ZIP nesting unchanged, disclose D47/D46 historical parent text SHA mistake, never claim physical spacetime, measured hertz or new universal theorem.

    python -m pip install sympy==1.14.0
    python src/verify_d62.py
    python tests/independent_d62.py
    python src/check_zenodo_metadata.py
