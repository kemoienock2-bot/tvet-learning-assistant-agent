import math


class ElectricalCalculator:

    @staticmethod
    def ohms_law(voltage=None, current=None, resistance=None):

        known = sum(
            x is not None
            for x in [voltage, current, resistance]
        )

        if known != 2:
            return (
                "Enter exactly TWO values."
            )

        if voltage is None:
            voltage = current * resistance
            return f"Voltage = {voltage:.2f} V"

        if current is None:
            current = voltage / resistance
            return f"Current = {current:.2f} A"

        resistance = voltage / current
        return f"Resistance = {resistance:.2f} Ω"

    @staticmethod
    def electrical_power(voltage, current):

        power = voltage * current

        return f"Power = {power:.2f} W"

    @staticmethod
    def electrical_energy(power, hours):

        energy = power * hours

        return f"Energy = {energy:.2f} Wh"