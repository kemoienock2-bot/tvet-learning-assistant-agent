from utils.gemini_helper import generate_gemini_response


class QuizAgent:
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
        return generate_gemini_response(prompt)
