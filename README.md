# All_Things_F1
An intelligent, multi-agent system that provides real-time and historical Formula 1 insights using the OpenF1 API and Google Gemini.

## 🌟 Core Features
- **Multi-Agent Architecture**: Separate agents for Planning, Execution, and Verification to ensure high-quality, reasoned outputs.
- **Natural Language Queries**: Ask complex F1 questions (e.g., "Compare the tire degradation between Verstappen and Norris in the last 10 laps").
- **Real-Time Data**: Integrates directly with [OpenF1](https://openf1.org/docs/) for car telemetry, lap times, and race control data.
- **Structured Output**: Returns verified, clean JSON or markdown responses.

## 🛠️ Tech Stack
- **Framework**: FastAPI (Python)
- **LLM**: Google Gemini (via `google-genai` SDK)
- **Data Source**: OpenF1 API (No-auth required)
- **Environment**: Python 3.10+

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10 or higher.
- A Google Gemini API Key (obtained from [Google AI Studio](https://aistudio.google.com/)).

### 2. Installation
```bash
# Clone the repository
git clone [https://github.com/your-username/f1_ops_assistant.git](https://github.com/your-username/f1_ops_assistant.git)
cd f1_ops_assistant

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
python -m pip install -r requirements.txt

