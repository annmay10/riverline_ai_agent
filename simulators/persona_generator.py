import random

PERSONAS = [
    {
        "age": 35,
        "location": "Delhi",
        "amount": "₹50,000",
        "months_due": 3,
        "mood": "angry",
        "negotiation_style": "wants a waiver due to job loss"
    },
    {
        "age": 28,
        "location": "Bangalore",
        "amount": "₹15,000",
        "months_due": 1,
        "mood": "confused",
        "negotiation_style": "asks for installment plan"
    },
    {
        "age": 42,
        "location": "Mumbai",
        "amount": "₹25,000",
        "months_due": 2,
        "mood": "anxious",
        "negotiation_style": "is willing to pay partially now and rest later"
    },
    {
        "age": 31,
        "location": "Kolkata",
        "amount": "₹35,000",
        "months_due": 4,
        "mood": "defensive",
        "negotiation_style": "claims not to have received previous reminders"
    },
    {
        "age": 39,
        "location": "Chennai",
        "amount": "₹10,000",
        "months_due": 1,
        "mood": "cooperative",
        "negotiation_style": "requests a payment link via SMS"
    }
]

def generate_persona():
    persona = random.choice(PERSONAS)
    prompt = f"You are a {persona['age']}-year-old customer from {persona['location']} who has an overdue credit card bill of {persona['amount']} for {persona['months_due']} months. You are feeling {persona['mood']} and you {persona['negotiation_style']}."
    return prompt