# TVET Learning Assistant Agent

An AI-powered multi-agent educational assistant designed to help TVET students learn Electrical Installation, Electronics, and Robotics through personalized guidance, quizzes, project support, and career advice.

## Problem

Many TVET students struggle to access personalized academic support outside the classroom. Technical subjects such as Electrical Installation, Electronics, and Robotics require continuous practice, project guidance, and revision resources that may not always be available.

## Solution

The TVET Learning Assistant Agent provides 24/7 learning support using multiple specialized AI agents that work together to answer questions, generate assessments, guide projects, and promote safe workshop practices.

## Features

### Tutor Agent

* Explains electrical installation concepts
* Teaches electronics fundamentals
* Supports robotics learning
* Answers technical questions

### Quiz Agent

* Generates revision questions
* Creates practice examinations
* Provides explanations for answers

### Project Agent

* Guides practical projects
* Supports Arduino and robotics projects
* Assists with circuit design

### Career Agent

* Provides career guidance
* Helps with CV preparation
* Suggests learning pathways

### Safety Agent

* Promotes electrical safety
* Explains workshop procedures
* Encourages safe tool handling

## Multi-Agent Architecture

Student Request
↓
Coordinator Agent
├── Tutor Agent
├── Quiz Agent
├── Project Agent
├── Career Agent
└── Safety Agent

## Technologies

* Google Agent Development Kit (ADK)
* Gemini API
* Python
* Streamlit
* GitHub

## Example Questions

* Explain Ohm's Law.
* Create a quiz on electrical installation.
* Help me build a line-following robot.
* Explain the function of a relay.
* Suggest a robotics learning pathway.

## Installation

```bash
git clone https://github.com/kemoienock2-bot/tvet-learning-assistant-agent.git

cd tvet-learning-assistant-agent

pip install -r requirements.txt
```

## Configuration

Set your Gemini API key:

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

## Future Improvements

* Swahili language support
* Voice interaction
* TVET curriculum integration
* Student progress tracking
* Mobile application deployment

## License

MIT License

