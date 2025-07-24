# main.py - Core logic for SEED_AGENT_001
import yaml # Used to read the .yaml configuration file

# This is the blueprint for our agent.
class VantaAgent:
    # The __init__ method runs when we first create the agent.
    def __init__(self, agent_id, mission):
        self.agent_id = agent_id
        self.mission = mission
        self.status = "STANDBY"
        self.config = self.load_config()
        
        print(f"Agent {self.agent_id} initialized. Mission: {self.mission}")
        if self.config:
            print(f"--- Config loaded: searching for {self.config.get('keywords_to_find')} in '{self.config.get('target_log_file')}' ---")

    # This function opens and reads our config.yaml file.
    def load_config(self):
        try:
            with open('config.yaml', 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print("ERROR: config.yaml not found. Agent cannot proceed.")
            return None

    # This is the main function where the agent performs its task.
    def execute_mission(self):
        if not self.config:
            self.status = "FAILED - NO CONFIG"
            return None

        self.status = "EXECUTING"
        print(f"\n--- {self.agent_id} is executing mission... ---")
        found_lines = []
        
        try:
            with open(self.config['target_log_file'], 'r') as log_file:
                for line in log_file:
                    for keyword in self.config['keywords_to_find']:
                        if keyword.lower() in line.lower():
                            found_lines.append(line.strip())
                            break 
        except FileNotFoundError:
            print(f"  ERROR: Log file not found at '{self.config['target_log_file']}'")
            self.status = "FAILED - FILE NOT FOUND"
            return None

        self.status = "COMPLETE"
        print(f"--- Mission Complete. Found {len(found_lines)} matching lines. ---")
        return found_lines

# This block only runs when you execute 'python main.py' directly.
if __name__ == "__main__":
    log_analyzer_agent = VantaAgent(
        agent_id="AGENT_001",
        mission="Analyze system log for critical keywords"
    )
    
    results = log_analyzer_agent.execute_mission()
    
    if results:
        print("\n--- REPORT: Critical Lines Found ---")
        for line in results:
            print(line)
        print("------------------------------------")