# Log Assistant

The Log Assistant is a Python package that provides a simple yet powerful tool to log function calls and send log messages for analysis using the OpenAI GPT-3.5-Turbo model. It allows you to easily track the number of function calls and generate insightful log messages with just a decorator.

## Features

- Decorator to log function calls with customizable log messages.
- Automatic retries for API requests in case of failure.
- Horizontally centered and dashed lines for aesthetically pleasing log messages.
- Integration with OpenAI GPT-3.5-Turbo model for log message generation.

## Installation

You can install the Log Assistant package using `pip`:

```bash
pip install logassistant
```

# Usage
To use the Log Assistant in your Python code, follow these steps:

1. Import the LogAssistant class:
```python
from logassistant import LogAssistant
```
2. Create an instance of the LogAssistant:
```python
logassistant = LogAssistant()
```
3. Apply the `@log_assistant.log` decorator to any function you want to log:
```python
@logassistant.log
def example_function(x):
    return x ** 2
```
4. Use the decorated function as usual:
```python
result = example_function(5)
print(result)  # Output: 25
```

The Log Assistant will automatically generate log messages for each function call, analyze them using the GPT-3.5-Turbo model, and print the results to the console.

# Configuration
Before using the Log Assistant, make sure to set up your OpenAI API key as an environmental variable named `OPENAI_API_KEY`.

# Dependencies
The Log Assistant relies on the following external libraries:
- requests
- openai

# License
This project is licensed under the MIT License. See the LICENSE file for more details.

# Contributing
Contributions to the Log Assistant are welcome! If you encounter any issues or have ideas for improvements, please feel free to open an issue or submit a pull request on our GitHub repository.