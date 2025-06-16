from agents.assistant import Assistant
from simulators.persona_generator import generate_persona
from evaluators.metrics import evaluate_conversation
from self_corrector.prompt_rewriter import rewrite_prompt

MAX_ITERS = 5
THRESHOLD = 2  # Max allowed score for repetition and neglect

current_prompt = None
for i in range(MAX_ITERS):
    print(f"\n--- Iteration {i + 1} ---")
    persona_prompt = generate_persona()
    print(f"[Persona]: {persona_prompt}")

    agent = Assistant(instructions=current_prompt)

    # Simulate conversation between persona and agent (mocked)
    conversation = f"Customer: {persona_prompt}\nBot: Hello, this is a reminder from your bank regarding overdue payments..."

    critique = evaluate_conversation(conversation)
    print(f"[Evaluation]: {critique}")

    repetition_score = int(critique.split('repetition=')[1].split(',')[0])
    neglect_score = int(critique.split('neglect=')[1].split('.')[0])

    if repetition_score <= THRESHOLD and neglect_score <= THRESHOLD:
        print("Agent passed the test.")
        break

    print("Agent needs improvement. Rewriting prompt...")
    current_prompt = rewrite_prompt(agent.instructions, critique)

print("\n--- Final Prompt ---\n")
print(current_prompt or agent.instructions)
