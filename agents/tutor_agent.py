"""
Tutor Agent

Provides educational explanations for TVET students.
"""

class TutorAgent:
def answer_question(self, question: str) -> str:
question = question.lower()

```
    if "ohm" in question:
        return (
            "Ohm's Law states that Voltage (V) equals Current (I) "
            "multiplied by Resistance (R). Formula: V = I × R."
        )

    if "relay" in question:
        return (
            "A relay is an electrically operated switch used to "
            "control high-power circuits using a low-power signal."
        )

    if "resistor" in question:
        return (
            "A resistor is an electronic component that limits "
            "the flow of electric current."
        )

    return (
        "I can help with Electrical Installation, Electronics, "
        "and Robotics concepts. Please ask a specific question."
    )
```

if **name** == "**main**":
tutor = TutorAgent()

```
print(tutor.answer_question("Explain Ohm's Law"))
print(tutor.answer_question("What is a relay?"))
```
