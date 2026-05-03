# We define a function to 'squish' names together
def collapse_names(name_list):
    # Create an empty list to store our squished names
    squished_list = []
    
    # Loop through every name in our input list
    for name in name_list:
        # Remove spaces
        clean_name = name.replace(" ", "")
        squished_list.append(clean_name)
        
    # Return the final list
    return squished_list


# --- TESTING THE SQUISH ---

# Original actors list
actors = ["Tom Cruise", "Tom Hanks", "Scarlett Johansson"]

# ✅ Action Item: Director list
directors = ["Christopher Nolan"]

# Run the function
cleaned_actors = collapse_names(actors)
cleaned_directors = collapse_names(directors)

# Open output file
with open("name_squish_test.txt", "w") as file:
    # Print and save actor results
    line1 = f"Original Actors: {actors}"
    line2 = f"Squished Actors: {cleaned_actors}"
    
    print(line1)
    print(line2)
    
    file.write(line1 + "\n")
    file.write(line2 + "\n")

    # Print and save director results
    line3 = f"Original Director: {directors}"
    line4 = f"Squished Director: {cleaned_directors}"
    
    print(line3)
    print(line4)
    
    file.write(line3 + "\n")
    file.write(line4 + "\n")

    # Logic check
    if "ChristopherNolan" in cleaned_directors:
        success_msg = "\n Success: Christopher Nolan was squished correctly!"
        print(success_msg)
        file.write(success_msg + "\n")