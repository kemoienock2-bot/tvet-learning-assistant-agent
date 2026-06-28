from utils.gemini_helper import get_gemini_client


class QuizAgent:
    def __init__(self) -> None:
        self.client = get_gemini_client()

    def generate(self, topic: str) -> str:
        prompt = f"""
Create a 10-question multiple-choice quiz for TVET students.

Topic:

{topic}

Requirements:

- Four options (A–D)
- Indicate the correct answer
- Brief explanation for each answer
"""
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text
