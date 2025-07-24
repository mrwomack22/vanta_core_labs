# dashboard.py - Our first integrated script

def check_system_component(component_name):
    """A simulation function that checks a system and returns its status."""
    print(f"--> Checking '{component_name}'...")
    # In a real-world script, this would contain complex logic.
    # For now, it will always return a healthy status.
    return "OK"


def print_dashboard():
    """Defines the list of systems and loops through them to print a status report."""
    print("--- VANTA_CORE System Status Dashboard ---")
    
    # YOUR TASK - PART 1:
    # Fill this list with at least three system component names.
    # e.g., "Forge", "Immune System", "Codex Link", "Gemini Core"
    components_to_check = [ "Forge", "Immune System", "Codex Link", "Gemini Core"]

    # YOUR TASK - PART 2:
    # Write a 'for' loop here that iterates through your 'components_to_check' list.
    # Inside the loop:
    # 1. Call the check_system_component() function, passing it the current component name.
    # 2. Store the return value in a variable called 'status'.
    # 3. Print a formatted string showing the component name and its status.
    #    e.g., "Forge Status: OK"
    for component in components_to_check:
        status = check_system_component(component)
        print(f"{component} Status: {status}")

    print("--------------------------------------")


# This is the main execution block that runs our program.
if __name__ == "__main__":
    print_dashboard()