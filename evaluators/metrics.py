from openai import OpenAI

openai = OpenAI()

def evaluate_conversation(conversation: str):
    prompt = f"""
    Evaluate this conversation for two issues:
    1. Repetition: Did the bot repeat itself?
    2. Neglect: Did the bot avoid or ignore valid customer questions?

    Rate each from 0 to 5. Format: repetition=score, neglect=score.

    {conversation}
    """
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content