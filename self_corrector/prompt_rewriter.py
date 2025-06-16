from openai import OpenAI

openai = OpenAI()

def rewrite_prompt(base_prompt: str, critique: str) -> str:
    prompt = f"""
    Given this base voice agent prompt:
    {base_prompt}

    And these failure critiques:
    {critique}

    Rewrite the prompt to reduce failures while maintaining the bot's goals and tone.
    """
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content