# 💬 Voice Agent Test Lab for Overdue Credit Card Bill Reminders

This project automates testing and self-improvement of a voice-based AI assistant designed for **banks reminding customers about overdue credit card bills**. It simulates real-world conversations, evaluates the agent’s responses, and evolves the assistant’s behavior through self-correction based on performance metrics.

---

## 🚀 Features

- 🤖 Voice agent powered by GPT-4o and Cartesia TTS
- 🗣️ Persona simulation of various customer types (angry, confused, anxious, etc.)
- 📈 Conversation evaluation using OpenAI to detect repetition and neglect
- 🔁 Automatic prompt rewriting based on failure modes
- 📞 Outbound call simulation with WAV call recording
- 🧪 Iterative test loop for continuous agent improvement

---

## 🛠️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/voice-agent-testlab.git
cd voice-agent-testlab
```

### 2. Create Python Environment

We recommend using `conda`:

```bash
conda create -n voicebot python=3.10
conda activate voicebot
```

Or using `venv`:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file in the root directory and include:

```env
OPENAI_API_KEY=your_openai_api_key
HUGGINGFACE_TOKEN=your_huggingface_token
```

> These are required for the GPT-4o LLM and HuggingFace-powered voice models.

### 5. Authenticate Hugging Face

Your Python code will call:

```python
from huggingface_hub import login
login(token="your_huggingface_token")
```

You can also authenticate via CLI:

```bash
huggingface-cli login
```

---

## 🧪 Run Testing & Self-Correction Loop

To run the AI testing cycle that evaluates and evolves the agent’s prompt:

```bash
python run_test_loop.py
```

Each iteration simulates a customer persona, conducts a conversation, evaluates the outcome, and updates the assistant if necessary.

---

## 🧠 Files Explained

### `agents/assistant.py`
Defines the assistant behavior and initial instructions.

### `simulators/persona_generator.py`
Generates different customer personas with emotions, due amounts, and negotiation styles.

### `evaluators/metrics.py`
Uses OpenAI to evaluate the conversation for repetition and neglect.

### `self_corrector/prompt_rewriter.py`
Modifies the assistant prompt based on evaluation feedback.

### `run_test_loop.py`
Runs the testing loop: persona → conversation → evaluation → correction.

---

## 📞 Running the Voice Agent (LiveKit)

To start the voice bot in a real-time audio session (e.g., outbound reminder bot):

1. Ensure LiveKit server or LiveKit Cloud is set up.
2. Configure the `entrypoint.py` session with STT, TTS, VAD, and noise suppression.
3. Start the agent:

```bash
python agents/entrypoint.py
```

The bot will initiate a call-like scenario and speak first (outbound).

### Recording Calls

Modify your `entrypoint.py` session to include audio recording with:

```python
import soundfile as sf
import io

recorded_audio = io.BytesIO()
await session.start_recording(recorded_audio)
# ... agent interaction ...
with open("call_recording.wav", "wb") as f:
    f.write(recorded_audio.getvalue())
```

---

## 📊 Evaluation Metrics

We track the following:

- **Repetition** — Did the bot repeat itself unnecessarily?
- **Neglect** — Did the bot ignore or avoid customer questions?

Each is scored from 0–5. Scores above a set threshold will trigger prompt rewriting.

---

## 🔄 Agent Self-Correction Flow

1. Simulate a persona with overdue bill behavior.
2. Run a mock conversation.
3. Evaluate the conversation.
4. If metrics fail, rewrite the agent prompt.
5. Repeat until the bot passes the tests.

---

## 📦 Optional Improvements

- Add UI for results (e.g., Streamlit)
- Add conversation logs and analytics
- Support multilingual personas
- Extend with real audio files instead of chat simulation
- Deploy to cloud with Docker or Kubernetes

---

## 🧾 License

MIT License

---

## 🧠 Credits

Built using:
- [LiveKit Agents](https://docs.livekit.io/agents)
- [Cartesia TTS](https://cartesia.ai)
- [Deepgram STT](https://deepgram.com)
- [OpenAI GPT-4o](https://platform.openai.com)
- [Hugging Face Transformers](https://huggingface.co)
