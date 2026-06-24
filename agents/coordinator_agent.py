"""
Coordinator Agent

Routes student requests to the appropriate specialist agent.
"""

class CoordinatorAgent:
def route_request(self, user_input: str) -> str:
text = user_input.lower()

```
    if any(word in text for word in ["quiz", "test", "exam", "revision"]):
        return "quiz_agent"

    if any(word in text for word in ["project", "arduino", "robot", "circuit"]):
        return "project_agent"

    if any(word in text for word in ["career", "job", "cv", "internship"]):
        return "career_agent"

    if any(word in text for word in ["safety", "ppe", "hazard", "risk"]):
        return "safety_agent"

    return "tutor_agent"
```

if **name** == "**main**":
agent = CoordinatorAgent()

```
examples = [
    "Create a revision quiz on electrical installation",
    "Help me build a line-following robot",
    "How do I write a CV?",
    "What PPE should I use in a workshop?",
    "Explain Ohm's Law"
]

for item in examples:
    print(f"{item} -> {agent.route_request(item)}")
```
