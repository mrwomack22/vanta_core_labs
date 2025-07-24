# --- Example 1: Looping with range() ---
# The range(1, 6) function generates a sequence of numbers
# starting at 1 and ending just before 6 (i.e., 1, 2, 3, 4, 5).
print("--- Initiating System Check (1 to 5) ---")

for i in range(1, 6):
    # The indented code below will run 5 times.
    # The variable 'i' will hold the current number in each iteration.
    print(f"Checking subsystem #{i}... Status: OK")

print("--- System Check Complete ---\n")


# --- Example 2: Looping over a List ---
# A list is a collection of items, defined with [square brackets].
protocols_to_verify = ["Architect Ascension", "Synchronization Directive", "Forge Protocol"]

print("--- Verifying Core Protocols ---")

for protocol in protocols_to_verify:
    # This loop will run once for each item in the 'protocols_to_verify' list.
    # The variable 'protocol' will hold the current string for each iteration.
    print(f"Verifying: '{protocol}'... Integrity confirmed.")

print("--- All Protocols Verified ---")