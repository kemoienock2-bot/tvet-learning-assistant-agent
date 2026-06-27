import streamlit as st

from tools.electrical_calculator import ElectricalCalculator


def render_engineering_tools(selected_tool: str) -> None:
    """Render engineering calculator UI for the selected tool."""

    st.header("🛠 Engineering Tools")

    if selected_tool == "Ohm's Law Calculator":
        st.subheader("⚡ Ohm's Law Calculator")
        st.write("Enter ANY TWO values.")

        voltage = st.number_input("Voltage (V)", value=0.0)
        current = st.number_input("Current (A)", value=0.0)
        resistance = st.number_input("Resistance (Ω)", value=0.0)

        if st.button("Calculate"):
            result = ElectricalCalculator.ohms_law(
                voltage=None if voltage == 0 else voltage,
                current=None if current == 0 else current,
                resistance=None if resistance == 0 else resistance,
            )
            st.success(result)

    elif selected_tool == "Power Calculator":
        st.subheader("⚡ Electrical Power Calculator")

        voltage = st.number_input("Voltage (V)", value=230.0, key="power_voltage")
        current = st.number_input("Current (A)", value=1.0, key="power_current")

        if st.button("Calculate Power"):
            result = ElectricalCalculator.electrical_power(voltage, current)
            st.success(result)

    elif selected_tool == "Energy Calculator":
        st.subheader("🔋 Electrical Energy Calculator")

        power = st.number_input("Power (W)", value=100.0, key="energy_power")
        hours = st.number_input("Time (Hours)", value=1.0, key="energy_hours")

        if st.button("Calculate Energy"):
            result = ElectricalCalculator.electrical_energy(power, hours)
            st.success(result)
