# 1. We DEFINE a function using the 'def' keyword.
#    'protocol_name' is a PARAMETER - a placeholder for the data
#    we will pass into the function.
def check_protocol(protocol_name):
    print(f"Checking '{protocol_name}'...")
    # In a real program, we could have complex logic here.
    # For now, we'll just create a simple status string.
    status = f"Result: '{protocol_name}' integrity is 100%."
    return status # The RETURN keyword sends this value back to whoever called the function.

# 2. Now we CALL the function multiple times with different arguments.
#    We are reusing the same block of code without rewriting it.
print("--- Initiating Protocol Integrity Scan ---\n")

# Call the function and store its return value in a variable
status_1 = check_protocol("Architect Ascension")
print(status_1)

print("") # Add a blank line for spacing

status_2 = check_protocol("Synchronization Directive")
print(status_2)

print("\n--- All Scans Complete ---")

def double_it(number):
    """This function takes a number and returns its double."""
    return number * 2

double = double_it(512)
print(f"The double of 512 is: {double}")