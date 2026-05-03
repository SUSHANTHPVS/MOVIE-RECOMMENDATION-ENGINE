# Import pandas to view our data
import pandas as pd

# Define a function with a 'Parameter' called 'user_choice'
# This 'user_choice' acts as a placeholder for whatever name we provide later
def search_engine(user_choice,num_results):
    # Print a message using the parameter to show we received the input
    print(f"🔍 Searching the database for: {user_choice}...")
    
    # In a real engine, we would find the index here. 
    # For now, we simulate finding the 'Top 3' for that specific choice.
    results = [f"{user_choice} 2", f"{user_choice} 3", f"{user_choice}: Origins"]
    
    # Return the results to the main program
    return results

# --- THE EXECUTION ---

# Step 1: We 'Call' the function with the 'Argument' "Batman"
list_one = search_engine("Batman")
print(f"Recommended for you: {list_one}")

# Step 2: We 'Call' the same function again with a DIFFERENT 'Argument' "Shrek"
# Notice we didn't have to rewrite the code!
list_two = search_engine("Shrek")
print(f"Recommended for you: {list_two}")
