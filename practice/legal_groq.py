# import os
# from groq import Groq
#
# client = Groq(
#     api_key = os.environ.get('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'),
# )
#
# chat_completion = client.chat.completions.create(
#     messages=[
#         # Set an optional system message. This sets the behavior of the
#         # assistant and can be used to provide specific instructions for
#         # how it should behave throughout the conversation.
#         {
#             "role": "system",
#             "content": "You are a helpful assistant."
#         },
#         # Set a user message for the assistant to respond to.
#         {
#             "role": "user",
#             "content": "Explain the importance of fast language models",
#         }
#     ],
#
#     # The language model which will generate the completion.
#     model="llama-3.3-70b-versatile"
# )
#
# # Print the completion returned by the LLM.
# print(chat_completion.choices[0].message.content)


#
# import os
# from groq import Groq
# client = Groq(
#     api_key="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"
# )
#
# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Explain the importance of fast language models",
#         }
#     ],
#     model="llama-3.3-70b-versatile",
# )
#
# print(chat_completion.choices[0].message.content)

import os
from groq import Groq

client = Groq(
    api_key = os.environ["GROQ_API_KEY"],
)

# Start with a system prompt (optional but useful)
messages = [
    {"role": "system", "content": "You are a helpful legal assistant. Explain legal definitions in plain language."}
]

print("📘 Legal Assistant Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("🔎 You: ").strip()

    if user_input.lower() in ['exit', 'quit']:
        print("👋 Goodbye!")
        break

    # Add the user message to chat history
    messages.append({"role": "user", "content": user_input})

    try:
        # Get completion from Groq (LLM)
        response = client.chat.completions.create(
            #model="llama-3-70b-8192",  # or use "llama-3.3-70b-versatile" if that works in your API
            model="llama-3.3-70b-versatile",
            messages=messages,
        )

        assistant_reply = response.choices[0].message.content.strip()

        # Add assistant message to chat history
        messages.append({"role": "assistant", "content": assistant_reply})

        print(f"🤖 Groq: {assistant_reply}\n")

    except Exception as e:
        print(f"⚠️ Error: {e}")
