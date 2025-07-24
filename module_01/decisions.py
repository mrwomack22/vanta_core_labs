# 1. The input() function prompts the user and waits for them to type something.
#    It always returns the input as a string (text).
user_input = input("Enter the current SEED number: ")

# 2. To perform a mathematical comparison, we must convert the text input
#    into an integer (a whole number). This is called 'type casting'.
current_seed = int(user_input)

# 3. Conditional logic lets the program make decisions.
#    It checks each condition in order and runs the code block for the first one that is True.
print("--- Analyzing Input ---")

if current_seed == 13:
    # The == operator checks if two values are exactly equal.
    print("Status: Correct. We are on SEED 13.")
elif current_seed < 13:
    # The < operator checks if a value is less than another.
    print("Status: Behind schedule. We are past that SEED.")
else:
    # The 'else' block runs if none of the above conditions were True.
    print("Status: Ahead of schedule. We need to catch up!")

print("--- Analysis Complete ---")