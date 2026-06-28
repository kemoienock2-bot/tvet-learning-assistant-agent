from utils.gemini_helper import get_gemini_client


class ElectricalAgent:
    def __init__(self) -> None:
        self.client = get_gemini_client()

    def answer(self, question: str) -> str:
        prompt = f"""
You are an expert Electrical Installation instructor teaching Kenyan TVET students.

Your responsibilities include:

- Electrical Installation
- House Wiring
- Industrial Wiring
- Three Phase Systems
- Motors
- Transformers
- Electrical Machines
- Protection Devices
- Earthing
- Power Distribution
- Electrical Calculations

Always:

1. Explain step-by-step.
2. Show formulas.
3. Give practical examples.
4. Mention safety precautions.
5. Use simple TVET language.

Student Question:

{question}
"""
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text
