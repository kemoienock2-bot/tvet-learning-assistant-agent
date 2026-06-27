from utils.gemini_helper import generate_gemini_response


class ProjectAgent:
    def advise(self, topic: str) -> str:
        prompt = f"""
You are an expert Kenyan TVET project instructor.

Guide students through practical hands-on TVET projects.
Include:
- project planning
- materials and tools
- step-by-step assembly
- testing and troubleshooting
- safety tips

Project Topic:
{topic}
"""
        return generate_gemini_response(prompt)
