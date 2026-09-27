# Iterative Sizing Tool with Interface (ENG 321)

## Project Overview
This application replaces a manual spreadsheet Goal-Seek process with an automated, Python-driven iterative sizing tool featuring a Streamlit web interface.

## Original Workbook / Process
Replaces the Module 4 tank sizing workbook where radius was manually adjusted until target volume was reached.

## Inputs and Units
- **Initial Radius**: meters (m)
- **Target Volume**: cubic meters (m³)
- **Height**: meters (m)
- **Tolerance**: dimensionless convergence threshold
- **Max Iterations**: count

## Iterative Calculation
The solver repeatedly calculates cylindrical volume $V = \pi \cdot r^2 \cdot h$ and adjusts radius $r$ until the error $\vert{}V_{actual} - V_{target}\vert{} \le \text{tolerance}$.

## Convergence Rule & Tolerance
Convergence occurs when the absolute difference between computed volume and target volume is within the user-defined tolerance.

## Non-Convergence Behavior
If `max_iterations` is reached without meeting tolerance, the system explicitly flags the run as `NOT CONVERGED`.

## Validation Rules
- All numeric dimensions must be strictly positive (> 0).
- `max_iterations` must be an integer $\ge 1$.

## AI-Generated Version Defect
The generated implementation in `generated_version/ai_generated_solver.py` attempted exact numeric equality (`!=`) instead of using tolerance, resulting in infinite iteration loops or max iteration cap hits on floating-point values. Verified by `test_exposes_ai_generated_version_defect`.

## How to Run Locally
```bash
pip install -r requirements.txt
pytest
streamlit run app.py