# Create a new dictionary to hold the transformed answers
new_answers = {}
# Loop through the original answer list and transform each dictionary
for i, answer in enumerate(my_dict["answers"]):
    # Get the answer text
    answer_text = answer["answer"]
    # Create a new key with the answer option number
    option_key = f"option{i+1}"
    # Add the answer text to the new dictionary with the option key
    new_answers[option_key] = answer_text
    # Check if the answer is correct and set the isCorrect key if it is
    if answer["correct"]:
        is_correct = option_key

# Create the updated dictionary
updated_dict = {"question": my_dict["question"],
                "answers": new_answers,
                "isCorrect": new_answers[is_correct]}

# Print the updated dictionary
print(updated_dict)