import csv
import os
import pandas as pd
import difflib
from groq_simplifier import simplify_definition_groq
from intent_classifier import detect_intent

def load_legal_dictionary(file_path):
    try:
        df = pd.read_csv(file_path)
        df = df.dropna(subset=['term', 'definition'])

        dictionary = df.set_index('term')['definition'].to_dict()

        print(f"Loading the chatbot... ")
        return dictionary
    except Exception as e:
        print(f"Error loading dictionary: {e}")
        return {}

def chat_loop(legal_dict):
    print("\nHello, welcome to ArnoBot. Your personal legal dictionary.")
    print("I'll help break down fancy-sounding legal terms for you.")
    print("Type a legal term to look it up. Type 'q' to quit.")

    all_terms = list(legal_dict.keys())
    last_definition = ""
    last_term = ""

    while True:
        print("\n-----------------------------------------------------")
        user_input = input("Enter the term whose definition you'd like: ").strip().lower()

        if user_input.lower() in ('exit', 'quit','q'):
            print("Thanks for using ArnoBot!!!")
            break

        intent_data = detect_intent(user_input)
        # intent = intent_data.get("intent")
        intent = intent_data['intent']
#         print("1")
        if intent == "definition":
            og_input_term = user_input.strip().upper()
            term = intent_data.get("term", "").upper()
            # print("2")

            if term in legal_dict and term == og_input_term:
                last_term = term
                last_definition = legal_dict[term]
                simplify_definition_groq(last_definition)
                # print("3.1")
            else:
                # FUZZY MATCHING
                # print("3.2")
                matches = difflib.get_close_matches(term, all_terms, n=1, cutoff=0.7)
                if matches:
                    # print("3.2.1")
                    best_match = matches[0]
                    print(f"\nDid you mean '{best_match}'?")
                    last_term = best_match
                    last_definition = legal_dict[best_match]
                    simplify_definition_groq(last_definition)
                    # print(f"\nArnoBot: {simplified}")
                else:
                    print("-----Oops, term not found. Maybe try another.-----")

        elif intent == "follow_up":
            action = intent_data.get("action", "")
            if not last_definition:
                print("-----No previous term to follow up on. Please ask for a legal term first.-----")
                continue

            # Modify prompt for follow-up
            if action == "another_example":
                prompt = f"Give another example for the term '{last_term}' using this definition:\n{last_definition}"
            elif action == "simplify_further":
                prompt = f"Make this definition of '{last_term}' even simpler:\n{last_definition}"
            elif action == "rephrase":
                prompt = f"Rephrase this definition of '{last_term}':\n{last_definition}"
            else:
                prompt = f"Respond conversationally to the user based on this:\n{last_definition}"

            simplify_definition_groq(prompt)
            # print(f"\nArnoBot: {followup_response}")
        else:
            print("-----Sorry, I didnt understand that. Try asking for a legal term.----")

def main():
    path = 'lexpredict-legal-dictionary/sources/blacks_second_edition/blacks_second_edition_terms.csv'
    legal_dict = load_legal_dictionary(path)
    chat_loop(legal_dict)

if __name__ == '__main__':
    main()
