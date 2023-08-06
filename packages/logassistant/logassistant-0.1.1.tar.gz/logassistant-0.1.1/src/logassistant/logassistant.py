import inspect
import os
import shutil
import requests
import time


class LogAssistant:
    def __init__(self):
        # Global variable to keep track of the function calls count
        self.function_call_count = 0

        # Maximum number of retries for the API request
        self.MAX_RETRIES = 3

        # Get the OpenAI API key from environmental variable
        self.OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

        # Initial prints
        self.print_horizontal_line()
        self.print_centered("LOG ASSISTANT")
        self.print_horizontal_line()

    def create_horizontal_line(self):
        terminal_width = shutil.get_terminal_size().columns
        horizontal_line = "-" * terminal_width
        return horizontal_line

    def print_horizontal_line(self):
        print(self.create_horizontal_line())

    def print_centered(self, text):
        terminal_width = shutil.get_terminal_size().columns
        padding = (terminal_width - len(text)) // 2
        centered_text = " " * padding + text
        print(centered_text)

    def send_request(self, content, retries=None):
        if retries is None:
            retries = self.MAX_RETRIES

        # Define the API endpoint
        url = "https://api.openai.com/v1/chat/completions"

        # Set the headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.OPENAI_API_KEY}",
        }

        # Define the payload (data)
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": content}],
            "temperature": 0.7,
        }

        # Retry the API request a maximum of 'retries' times
        for _ in range(retries):
            response = requests.post(url, headers=headers, json=data)

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response
                json_data = response.json()
                # Extract the content from the response
                content = json_data["choices"][0]["message"]["content"]
                return content
            else:
                # Wait for a moment before retrying
                time.sleep(1)

        # Print an error message if all retries fail
        print(
            f"Request failed after {self.MAX_RETRIES} retries with status code: {response.status_code}"
        )
        print(response.json())

    def log(self, func):
        def wrapper(*args, **kwargs):
            self.function_call_count += 1

            # Get the source code of the decorated function
            source_code = inspect.getsource(func)

            # Remove the @log decorator from the source code
            source_lines = source_code.split("\n")
            source_lines = [line for line in source_lines if "@log" not in line]
            source_code = "\n".join(source_lines)

            # Get the function name
            function_name = func.__name__

            # Get the function arguments and their values
            function_arguments = inspect.getcallargs(func, *args, **kwargs)

            # Convert the function arguments to a string representation
            arguments_str = ", ".join(f"{key}={value}" for key, value in function_arguments.items())

            # Execute the function with the provided arguments
            result = func(*args, **kwargs)

            # Prepare the log message
            request_content = f"""Analyze this function call as if it was executed and create a log message that a programmer would write as a sentence, don't write any prefixes: 
                The function is: {source_code} with parameters: {arguments_str}. The result was {result}"""

            print(
                f"Analyzing {function_name} call with parameters: {arguments_str} ...",
                end="",
                flush=True,
            )

            # Send the log message to ChatGPT
            response = self.send_request(request_content)

            print(
                "\r" + " " * (shutil.get_terminal_size().columns - 1), end="\r"
            )  # Delete the loading message
            print(f"{self.function_call_count}.\t{response}")
            self.print_horizontal_line()

            return result

        return wrapper
