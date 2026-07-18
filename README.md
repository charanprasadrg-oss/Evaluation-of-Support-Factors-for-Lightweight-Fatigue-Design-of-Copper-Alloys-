# Evaluation-of-Support-Factors-for-Lightweight-Fatigue-Design-of-Copper-Alloys
This project focuses on predicting the fatigue support factor n for notched copper alloy components so that designers can account for notch effects without performing new fatigue tests for every geometry.

Experimentally, four copper alloy specimen pairs (G6‑A to G6‑D) were tested in both unnotched and notched conditions under axial loading using the staircase method according to DIN 50100. For each series, the endurance limit SaE (unnotched) and SaEn (notched) were evaluated from the staircase data, providing a fatigue notch factor Kf = SaE / SaEn. The experimental support factor was then obtained as n = Kt / Kf, where the theoretical stress concentration factor Kt was computed from specimen geometry.

Two notch types were considered: circumferential grooves and shoulder steps. For each notched specimen, the geometric parameters (D, d, r, t) were measured and used in analytical formulae to compute Kt and the relative stress gradient G. Groove and shoulder geometries use different Kt and G expressions, with a correction factor φ to account for notch depth. This yields a range of G values from shallow to very sharp notches, expanding beyond the literature data.

To build a general model, the four new experimental data points (n, G, Rm) were combined with six literature points from Siebel and Stieler for copper alloys. A two‑parameter Siebel–Stieler model of the form

n = 1 + a·√G·Rmᵇ

was fitted to the 10‑point dataset using nonlinear least‑squares (SciPy in the original work, or a fixed‑parameter version in the shared code). The resulting parameters a ≈ 3.7010 and b ≈ −0.4659 achieved an average prediction error of about 6.3%. The negative exponent on tensile strength Rm reflects increased notch sensitivity at higher strength levels, consistent with known behavior for metals.

Using the fitted model, design charts were generated: n vs G for several Rm values, and n vs Rm for several G values. These charts, and the corresponding Python implementation, allow engineers to estimate the support factor directly from notch geometry (through G) and material tensile strength Rm, then compute Kf = Kt / n and the notched endurance limit. This provides a practical tool for fatigue‑safe, lightweight design of copper alloy components without requiring new component‑level fatigue tests for every geometry.
