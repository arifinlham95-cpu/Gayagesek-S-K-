import streamlit as st
import numpy as np
import pandas as pd

# =========================
# PHYSICS FUNCTION
# =========================
def calculate_force(m, mu_s, mu_k, F):
    g = 9.8
    fs_max = mu_s * m * g
    fk = mu_k * m * g

    if F < fs_max:
        status = "The object does not move (static friction)"
        friction_force = F
    else:
        status = "The object moves (kinetic friction)"
        friction_force = fk

    return fs_max, fk, friction_force, status


# =========================
# STREAMLIT UI
# =========================
st.title("Online Practicum: Static and Kinetic Friction Forces")

st.markdown("""
This application simulates **static and kinetic friction forces**
acting on an object being pulled across a flat surface,
complete with **force direction visualization and block simulation**.
""")

# Input parameters
m = st.number_input("Object Mass (kg)", min_value=0.1, value=2.0)
mu_s = st.number_input("Static Friction Coefficient (μs)", min_value=0.0, value=0.5)
mu_k = st.number_input("Kinetic Friction Coefficient (μk)", min_value=0.0, value=0.3)
F = st.number_input("Applied Force (N)", min_value=0.0, value=10.0)

# Calculation
fs_max, fk, friction_force, status = calculate_force(m, mu_s, mu_k, F)

# =========================
# OUTPUT TEXT
# =========================
st.subheader("Calculation Results")
st.write(f"Maximum Static Friction (Fs max): **{fs_max:.2f} N**")
st.write(f"Kinetic Friction (Fk): **{fk:.2f} N**")
st.write(f"Friction Force Acting: **{friction_force:.2f} N**")
st.info(status)

# =========================
# NUMERICAL GRAPH
# =========================
st.subheader("Graph of Applied Force vs Friction Force")

F_range = np.linspace(0, fs_max * 1.5, 100)
friction_range = []

for F_i in F_range:
    if F_i < fs_max:
        friction_range.append(F_i)
    else:
        friction_range.append(fk)

st.line_chart({
    "Applied Force (N)": F_range,
    "Friction Force (N)": friction_range
})

# =========================
# BLOCK & FORCE VISUALIZATION
# =========================
st.subheader("Force Simulation Visualization")

# Visual scale (prevent arrows from becoming too long)
scale = max(F, friction_force, 1)
Ft_visual = F / scale
Ff_visual = friction_force / scale

data = pd.DataFrame({
    "x": [0, 0],
    "y": [0, 0],
    "dx": [Ft_visual, -Ff_visual],
    "dy": [0, 0],
    "type": ["Applied Force", "Friction Force"]
})

st.vega_lite_chart(
    data,
    {
        "width": 500,
        "height": 200,
        "layer": [
            # Block
            {
                "mark": {"type": "rect", "width": 60, "height": 40},
                "encoding": {
                    "x": {"value": 250},
                    "y": {"value": 100},
                    "color": {"value": "steelblue"}
                }
            },
            # Force arrows
            {
                "mark": {"type": "rule", "strokeWidth": 4},
                "encoding": {
                    "x": {"value": 250},
                    "y": {"value": 100},
                    "x2": {
                        "field": "dx",
                        "type": "quantitative",
                        "scale": {"domain": [-1, 1], "range": [100, 400]}
                    },
                    "y2": {"value": 100},
                    "color": {
                        "field": "type",
                        "type": "nominal",
                        "scale": {
                            "domain": ["Applied Force", "Friction Force"],
                            "range": ["green", "red"]
                        }
                    }
                }
            }
        ]
    }
)

st.caption("Green arrow: applied force | Red arrow: friction force")

# =========================
# CONCLUSION
# =========================
st.subheader("Conclusion")

if F < fs_max:
    st.write(
        "The applied force is not enough to overcome the maximum static friction, "
        "so the object remains stationary."
    )
else:
    st.write(
        "The applied force exceeds the maximum static friction, "
        "so the object begins to move and the acting friction becomes kinetic friction."
    )
