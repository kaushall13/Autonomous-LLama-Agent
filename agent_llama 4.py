from agno.agent import Agent, RunResponse
from agno.models.groq import Groq
from agno.tools.serpapi import SerpApiTools
import os
from dotenv import load_dotenv
import time

# Load environment variables from .env file
load_dotenv()

# Get SerpAPI key from environment
serpapi_api_key = os.getenv("SERPAPI_API_KEY")

class GoalOrientedAgent(Agent):
    """
    A goal-driven autonomous agent using a large language model and SerpAPI
    to search the web, complete tasks, reflect on outcomes, and adapt its behavior.
    """
    def __init__(self, name, model, tools, instructions, goals=None, **kwargs):
        super().__init__(name=name, model=model, tools=tools, instructions=instructions, **kwargs)
        self.goals = goals if goals else []
        self.completed_goals = []
        self.failed_tasks = []
        self.task_attempts = {}
        self.reflection_enabled = True
        self.last_query = None
        self.last_response = None

    def evaluate_goal(self, current_task):
        """
        Mark a goal as completed if it was successfully executed.
        """
        if current_task in self.goals:
            self.goals.remove(current_task)
            self.completed_goals.append(current_task)
            return True
        return False

    def add_goal(self, goal):
        """
        Add a new goal to the agent's task list.
        """
        if goal not in self.goals:
            self.goals.append(goal)

    def manage_goals(self):
        """
        Prioritize and sort goals before execution.
        """
        if not self.goals:
            self.ask_for_goal()

        # Prioritize goals based on defined logic
        self.goals = sorted(self.goals, key=lambda g: self.goal_priority(g), reverse=True)

    def ask_for_goal(self):
        """
        Prompt the user to enter a new goal if none are available.
        """
        new_goal = input("Enter the goal you would like the agent to pursue: ")
        self.add_goal(new_goal)

    def goal_priority(self, goal):
        """
        Assign priority score to goals. Customize as needed.
        """
        if "budget" in goal.lower():
            return 10  # High priority for budget-related queries
        return 1

    def reflect_on_task(self, task_name, result, success=True):
        """
        Analyze task performance and update internal state.
        """
        if success:
            print(f"✅ Task '{task_name}' completed successfully.")
        else:
            print(f"❌ Task '{task_name}' failed. Retrying or adjusting strategy.")
            self.failed_tasks.append(task_name)

        # Track task attempts
        self.task_attempts[task_name] = self.task_attempts.get(task_name, 0) + 1

        # Adapt approach if repeated failure
        if self.task_attempts[task_name] > 3 and not success:
            print(f"⚠️ Task '{task_name}' has failed multiple times. Reevaluating approach.")
            self.modify_approach(task_name)

    def modify_approach(self, task_name):
        """
        Adjust search strategy based on prior failure.
        """
        if task_name == "Union Budget 2025":
            print("Refining search strategy for Union Budget 2025.")
            self.tools[0].update_query_params({"time": "latest", "filter": "official sources"})

    def handle_error(self, error):
        """
        Basic error recovery logic.
        """
        print(f"⚠️ Error occurred: {error}. Retrying in 3 seconds...")
        time.sleep(3)
        self.retry_last_task()

    def retry_last_task(self):
        """
        Attempt to rerun the last failed task.
        """
        if self.failed_tasks:
            task = self.failed_tasks[-1]
            print(f"🔁 Retrying task: {task}")
            self.perform_task(task)

    def request_clarification(self, original_query):
        """
        Ask the user to clarify the query if the response is unsatisfactory.
        """
        print("Please provide more details or clarify the query: ")
        clarification = input("Clarification: ")
        return original_query + " " + clarification

    def perform_task(self, task):
        """
        Execute the specified task using the LLM and tools.
        """
        print(f"\n🔍 Performing task: {task}")
        self.last_query = task
        retry_count = 0
        max_retries = 3

        try:
            while retry_count < max_retries:
                # Call LLM to handle query via tools
                response = self.print_response(self.last_query, stream=True)

                if response:
                    self.last_response = response
                    print(f"\n📄 Response: {response}")

                # Ask user if satisfied with answer
                user_input = input("Was the answer satisfactory? (yes/no): ").strip().lower()

                if user_input == "yes":
                    break  # Exit loop if user is satisfied

                # Request clarification and retry
                new_query = self.request_clarification(self.last_query)
                if new_query:
                    self.last_query = new_query
                else:
                    print("Failed to generate a clarified query. Using the last one.")

                retry_count += 1

            if retry_count == max_retries:
                print("⛔ Maximum retry attempts reached. Moving on.")

            self.evaluate_goal(task)
            print("✅ Goal completed. Moving on to the next.")

            # Prompt for new goal
            next_goal = input("Do you want to set a new goal? (yes/no): ").strip().lower()
            if next_goal == "yes":
                self.ask_for_goal()
            else:
                print('👋 Exiting. Bye!')
                exit()

        except Exception as e:
            print(f"❗ An error occurred: {e}")
            self.reflect_on_task(task, result=str(e), success=False)
            self.handle_error(e)


# 🧠 Define the goal-oriented web search agent
web_search_agent = GoalOrientedAgent(
    name="Querying using AgenticAI",
    role="Search the web for information and summarize findings",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[SerpApiTools(api_key=serpapi_api_key)],
    instructions=["Always include sources", "Summarize findings in a concise way"],
    show_tool_calls=True,
    markdown=True
)

# 🔁 Main interaction loop
while True:
    web_search_agent.manage_goals()

    if not web_search_agent.goals:
        web_search_agent.ask_for_goal()

    web_search_agent.perform_task(web_search_agent.goals[0])
