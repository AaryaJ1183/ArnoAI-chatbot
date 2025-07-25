import pandas as pd
import difflib

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

# def chat_loop(legal_dict):
#     print("\nHello, welcome to ArnoBot. Your personal legal dictionary.")
#     print("I'll help break down fancy-sounding legal terms for you.")
#     print("Type a legal term to look it up. Type 'exit' to quit.")
#
#     while True:
#         term = input("\n\nEnter the term whose definition you'd like: ").strip().lower()
#
#         if term in ('exit', 'quit'):
#             print("Thank you for using ArnoBot!")
#             break
#
#         definition = legal_dict.get(term.upper())
#
#         if definition:
#             print(f"\nSure! The definition of '{term}' is as follows:\n📖 {definition}")
#         else:
#             print("I'm sorry. It seems like I can't find that term.")

def chat_loop(legal_dict):
    print("\nHello, welcome to ArnoBot. Your personal legal dictionary.")
    print("I'll help break down fancy-sounding legal terms for you.")
    print("Type a legal term to look it up. Type 'exit' to quit.")

    all_terms = list(legal_dict.keys())  # Preload all normalized terms

    while True:
        user_input = input("\n\nEnter the term whose definition you'd like: ").strip().lower()


        if user_input.lower() in ('exit', 'quit'):
            print("Thank you for using ArnoBot!")
            break

        search_term = user_input.upper()

        # Exact match
        if search_term in legal_dict:
            print(f"\nSure! The definition of '{user_input}' is as follows:\n📖 {legal_dict[search_term]}")
        else:
            # Fuzzy match: find closest term(s)
            matches = difflib.get_close_matches(search_term, all_terms, n=1, cutoff=0.7)
            if matches:
                best_match = matches[0]
                print(f"\nDid you mean '{best_match}'?")
                print(f"📖 Which means: {legal_dict[best_match]}")
            else:
                print("I'm sorry. It seems like I can't find that term.")


# Test call
if __name__ == '__main__':
    path = '../lexpredict-legal-dictionary/sources/blacks_second_edition/blacks_second_edition_terms.csv'
    legal_dict = load_legal_dictionary(path)

    if legal_dict:
        chat_loop(legal_dict)
