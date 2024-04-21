# Specter

## Overview
Specter is a shell utility designed to add an element of unpredictability to command line operations. By introducing random delays, simulating errors, or executing commands normally, Specter offers a dynamic environment ideal for cybersecurity training and command line proficiency exercises.

## Features
- **Random Delays**: Injects random delays before command execution, simulating real-world latency or high system load.
- **Simulated Errors**: Occasionally produces fake error messages, requiring users to discern between actual and simulated command line issues.
- **Transparent Execution**: Executes commands without interference, allowing for a seamless blend of real and altered command outcomes.

## Requirements
- Python 3.x
- Bash shell environment
- Administrative or sudo privileges for installation

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/specter.git


2. **Navigate to the script directory**:
   ```bash
   cd specter

3. **Prepare the script for execution**:
   ```bash
   chmod +x ghostcommands.py

**Configuration**

To integrate Specter into your command line workflow, follow these steps to set up the Python script handler and command aliases in your shell configuration:

Modify .bashrc:
Open your .bashrc file in a text editor:
```bash
nano ~/.bashrc
```
**Insert the Command Handler Function**:

Append the following function to your .bashrc, adjusting the path to where ghostcommands.py is located:
```bash
function cmd() {
    python3 /path/to/specter/ghostcommands.py "$@"
}
alias sudo='sudo '  # Makes sure aliases work with sudo
```

**Establish Aliases for Frequent Commands**:
Create aliases to redirect command execution through Specter:
```bash
alias ls='cmd ls'
alias cat='cmd cat'
alias grep='cmd grep'
# Additional aliases can be set as needed
```
