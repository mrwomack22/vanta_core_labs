# 1. Variables are containers for storing data.
# We assign a value to a name with the = operator.
mission_name = "Architect Ascension"
current_seed = 12
system_readiness = 99.9

# 2. Python automatically detects the data type.
#    - mission_name is a 'str' (string) for text.
#    - current_seed is an 'int' (integer) for whole numbers.
#    - system_readiness is a 'float' for decimal numbers.

# 3. F-Strings are the best way to print variables within text.
#    The 'f' before the string lets you embed variables directly in {curly_braces}.
status_update = f"System: {mission_name} | Active SEED: {current_seed} | Readiness: {system_readiness}%"

# Print the final combined string to the console.
print(status_update)