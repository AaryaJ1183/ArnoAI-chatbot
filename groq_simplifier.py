from groq import Groq

prompt_initial = ("You are the world’s best explainer when it comes to explaining complicated legal terms to the lay-man."
          "You have a unique way of explaining terms in such simplicity that anyone can understand its meaning."
          "Also use it in a sentence to help them.")
prompt_reused = ("As the world's best explainer, convert this definition into something simple:")

# def simplify_definition_groq(definition):
#     try:
#         client = Groq(api_key="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")
#         stream = client.chat.completions.create(
#             model="llama-3.3-70b-versatile",
#             stream=True,
#             messages=[
#                 {"role": "system", "content": prompt_initial},
#                 {"role": "user", "content": prompt_reused + f"{definition}"}
#             ]
#         )
#         for chunk in stream:
#             print(chunk.choices[0].delta.content, end="")
#     except Exception as e:
#         return f"Hmmm. There seems to be an error. Wanna know what it is? Here it is anyways: \n {e}"

def simplify_definition_groq(definition):
    try:
        client = Groq(api_key="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")
        stream = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            stream=True,
            messages=[
                {"role": "system", "content": prompt_initial},
                {"role": "user", "content": prompt_reused + f"{definition}"}
            ]
        )
        print("\nArnoBot: ")
        for chunk in stream:
            content = chunk.choices[0].delta.content
            if content:
                print(content, end="")
        return None
    except Exception as e:
        return f"Hmmm. There seems to be an error. Wanna know what it is? Here it is anyways: \n {e}"
