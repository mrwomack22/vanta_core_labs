# main.py - Core logic for SEED_AGENT_002: The Web Scraper
import requests
from bs4 import BeautifulSoup

class VantaScraperAgent:
    def __init__(self, agent_id, mission, target_url):
        self.agent_id = agent_id
        self.mission = mission
        self.target_url = target_url
        self.status = "STANDBY"
        print(f"Agent {self.agent_id} initialized. Mission: {self.mission}")

    def execute_mission(self):
        self.status = "EXECUTING"
        print(f"\n--- {self.agent_id} connecting to {self.target_url}... ---")

        try:
            # Step 1: Use 'requests' to download the webpage's raw HTML
            response = requests.get(self.target_url)
            response.raise_for_status() # This will raise an error if the page is not found (e.g., 404)

            # Step 2: Use 'BeautifulSoup' to parse the HTML into a searchable object
            soup = BeautifulSoup(response.text, 'html.parser')

            # Step 3: Find the specific HTML element we want.
            # After inspecting http://quotes.toscrape.com in a browser, we know the first
            # quote is inside a <span> tag that has a class called 'text'.
            quote_element = soup.find('span', class_='text')

            if quote_element:
                # If the element was found, extract just the text content from it.
                quote_text = quote_element.get_text(strip=True)
                self.status = "COMPLETE"
                print("--- Mission Complete. Data extracted. ---")
                return quote_text
            else:
                self.status = "FAILED - ELEMENT NOT FOUND"
                return "Could not find the quote element on the page."

        except requests.exceptions.RequestException as e:
            # This 'except' block handles network errors (e.g., no internet connection)
            self.status = f"FAILED - NETWORK ERROR"
            print(f"An error occurred: {e}")
            return self.status

# This is the main execution block that runs our program.
if __name__ == "__main__":
    # We will use a website that is specifically designed for scraping practice.
    URL_TO_SCRAPE = "http://quotes.toscrape.com"

    scraper_agent = VantaScraperAgent(
        agent_id="AGENT_002",
        mission=f"Extract the first quote from {URL_TO_SCRAPE}",
        target_url=URL_TO_SCRAPE
    )

    # Run the agent's mission and store the result.
    result = scraper_agent.execute_mission()

    print("\n--- AGENT REPORT ---")
    print(f"Agent Status: {scraper_agent.status}")
    print(f"Extracted Data: {result}")
    print("--------------------")