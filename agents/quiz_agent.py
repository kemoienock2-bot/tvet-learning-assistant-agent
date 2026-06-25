"""
Quiz Agent

Generates revision questions for TVET students.
"""

class QuizAgent:
def generate_quiz(self, topic):
return [
f"What is the definition of {topic}?",
f"State two applications of {topic}.",
f"Explain the importance of {topic}.",
f"Describe a practical use of {topic}.",
f"List safety precautions related to {topic}."
]
