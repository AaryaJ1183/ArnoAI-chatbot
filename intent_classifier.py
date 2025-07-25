from groq import Groq
import json

intent_prompt_template = (
    "Classify what the user wants. Output JSON with:\n"
    "- intent: either 'definition' or 'follow_up'\n"
    "- term: the legal term (only if intent is 'definition')\n"
    "- action: (only if follow_up), one of ['another_example', 'simplify_further', 'rephrase']\n\n"
    "Examples:\n"
    "User: What is estoppel?\nOutput: {\"intent\": \"definition\", \"term\": \"estoppel\"}\n\n"
    "User: Can you give another example?\nOutput: {\"intent\": \"follow_up\", \"action\": \"another_example\"}\n\n"
    "User: Explain it in simpler words.\nOutput: {\"intent\": \"follow_up\", \"action\": \"simplify_further\"}\n\n"
)

def detect_intent(user_input):
    try:
        client = Groq(api_key="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")
        full_prompt = intent_prompt_template + f"User: {user_input}\nOutput:"
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a JSON-only intent classifier."},
                {"role": "user", "content": full_prompt}
            ]
        )
        content = response.choices[0].message.content
        # print(f"[INTENT DEBUG] Groq Output: {content}")
        return json.loads(content)
    except Exception as e:
        print(f"Intent detection error: {e}")
        return {"intent": "unknown"}
