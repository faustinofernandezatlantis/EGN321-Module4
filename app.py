import streamlit as st
import pandas as pd
from src.iteration import run_iterative_solver, CalculationStatus

st.set_page_config(page_title="Iterative Sizing Tool", layout="wide")

st.title("⚙️ Iterative Sizing Tool with Interface")
st.markdown("Automated engineering calculation tool replacing manual Goal-Seek processes.")

st.sidebar.header("Calculation Parameters")
initial_val = st.sidebar.number_input("Starting Value (Radius)", value=1.0, step=0.1)
target_val = st.sidebar.number_input("Target Value (Volume)", value=100.0, step=10.0)
height = st.sidebar.number_input("Height (h)", value=5.0, step=0.5)
tolerance = st.sidebar.number_input("Convergence Tolerance", value=0.001, format="%.5f")
max_iters = st.sidebar.number_input("Maximum Iterations", value=50, step=1)

if st.sidebar.button("Run Solver", type="primary"):
    result = run_iterative_solver(
        initial_value=initial_val,
        target_value=target_val,
        height=height,
        tolerance=tolerance,
        max_iterations=int(max_iters)
    )

    status = result["status"]

    # Display clear Status Badge
    if status == CalculationStatus.CONVERGED:
        st.success(f"STATUS: {status}")
    elif status == CalculationStatus.NOT_CONVERGED:
        st.warning(f"STATUS: {status}")
    else:
        st.error(f"STATUS: {status} — {result.get('error_message')}")

    col1, col2, col3 = st.columns(3)
    col1.metric("Final Output (Radius)", f"{result['final_value']:.4f}" if result['final_value'] else "N/A")
    col2.metric("Final Error", f"{result['final_error']:.6f}" if result['final_error'] else "N/A")
    col3.metric("Iterations Performed", result["iterations_performed"])

    # Iteration History
    if result["history"]:
        st.subheader("Iteration History")
        df_history = pd.DataFrame(result["history"])
        st.dataframe(df_history, use_container_width=True)