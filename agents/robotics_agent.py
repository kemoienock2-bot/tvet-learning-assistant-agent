from utils.gemini_helper import generate_gemini_response


class RoboticsAgent:
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
        return generate_gemini_response(prompt)
