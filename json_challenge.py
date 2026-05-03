# Import the Abstract Syntax Trees (ast) library
import ast

# Original messy genre string
messy_cell = '[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}]'

# New messy keywords string (Action Item)
messy_keywords = '["superhero", "marvel", "billionaire"]'

# Open output file
with open("json_unpacked.txt", "w") as file:
    # Prove original type
    before_type = f"Before Unwrapping: {type(messy_cell)}"
    print(before_type)
    file.write(before_type + "\n")

    # Unwrap both strings
    clean_list = ast.literal_eval(messy_cell)
    messy_list = ast.literal_eval(messy_keywords)

    # Check new type
    after_type = f"After Unwrapping: {type(clean_list)}"
    print(after_type)
    file.write(after_type + "\n")

    # First genre
    first_genre = f"First Genre Found: {clean_list[0]['name']}"
    print(first_genre)
    file.write(first_genre + "\n")

    # Loop through genres
    for item in clean_list:
        line = f"Found Genre: {item['name']}"
        print(line)
        file.write(line + "\n")

    # ✅ Action Item: print second keyword
    second_keyword = f"Second Keyword: {messy_list[1]}"
    print(second_keyword)
    file.write(second_keyword + "\n")