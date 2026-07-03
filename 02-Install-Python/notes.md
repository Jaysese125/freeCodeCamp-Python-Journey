\# 💻 Study Notes: Installing Python \& Running Code Locally



\## 1. Local Environment Setup

\* \*\*Official Source:\*\* Always download the official installer directly from \[python.org](https://www.python.org/).

\* \*\*Windows Execution Layout:\*\* When running the Windows `.exe` installer, it is critical to check the \*\*"Add python.exe to PATH"\*\* checkbox. This binds the Python binary path to the global environment variables, allowing execution from any shell interface.

\* \*\*macOS Setup:\*\* Uses a `.pkg` installer. On modern setups, `python3` is standard, while `python` may reference deprecated Python 2 runtimes on legacy machines.



\## 2. Integrated Development Environments (IDEs)

\* An \*\*IDE\*\* bundles a text/code editor, debugging features, built-in terminals, and extensions into a unified workspace.

\* \*\*Industry Standards:\*\* VS Code, PyCharm, and Spyder.

\* \*\*Native Running:\*\* Scripts are saved with the `.py` file extension and executed from the workspace directory using:

&#x20; ```bash

&#x20; python main.py

## 3. The Interactive Shell (REPL)

Trigger Command: Typing python or python3 alone into a terminal opens the interactive shell, signified by the >>> user input prompt.

\* REPL Cycle Execution:

\* \*\*Read:\*\* Takes the raw user input line.

\* \*\*Evaluate:\*\* Interprets and executes the expression.

\* \*\*Print:\*\* Displays the evaluation result directly to the terminal screen.

\* \*\*Loop:\*\* Resets the interface back to >>> for subsequent commands.

\* \*\*Termination:\*\* Safely exit the loop using exit() or key combinations like Ctrl + Z + Enter (Windows).

