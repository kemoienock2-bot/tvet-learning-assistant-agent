from utils.gemini_helper import get_gemini_client


class RoboticsAgent:
    def __init__(self) -> None:
        self.client = get_gemini_client()

    def answer(self, question: str) -> str:
        prompt = f"""
You are an expert Robotics and Automation instructor.

Teach TVET students using simple language.

Topics include:
- Robotics
- Arduino
- ESP32
- Raspberry Pi
- PLCs
- Sensors
- Motors
- Automation
- Artificial Intelligence

Student Question:

{question}
"""
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text
