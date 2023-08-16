# Clothing Search Query Correction and Adjustment

# This program takes a user's clothing-related search query, corrects any spelling errors,
# and adjusts it to include relevant clothing and retail terms. It then presents the adjusted query.


import nltk # Natural Language Toolkit
from textblob import TextBlob


# dictionary for our custom replacements
custom_replacements = {
"meen": "men",
"nen": "men",
"shesi": "shoe",
}

def correct_and_adjust_clothing_query(query):
    # apply custom replacements
    for incorrect, correct in custom_replacements.items():
        query = query.replace(incorrect, correct)
    
    # correct any the remaining spelling errors in the query 
    corrected_query = TextBlob(query).correct()
    
    return str(corrected_query)



#main
if __name__ == "__main__":
    user_input = input("Enter your clothing search query: ")
    adjusted_query = correct_and_adjust_clothing_query(user_input)
    print("Adjusted Query:", adjusted_query)