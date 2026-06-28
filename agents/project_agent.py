from utils.gemini_helper import get_gemini_client


class ProjectAgent:
    def __init__(self) -> None:
        self.client = get_gemini_client()

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
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text
