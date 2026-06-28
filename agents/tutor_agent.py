from utils.gemini_helper import get_gemini_client


class TutorAgent:

    def __init__(self) -> None:
        self.client = get_gemini_client()

    def answer_question(self, question: str) -> str:

        prompt = f"""
You are Kenokip SmartLearn AI.

You are an expert TVET instructor.

Teach students clearly using simple language.

Subjects include:
- Electrical Installation
- Electronics
- Robotics
- PLC
- Arduino
- Industrial Automation
- Electrical Safety

Always:
- Explain step by step.
- Include formulas where appropriate.
- Give practical examples.
- Mention safety precautions if needed.

Student Question:
{question}
"""

        try:

            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )

            return response.text

        except Exception as e:

            return f"Gemini Error:\n\n{e}"