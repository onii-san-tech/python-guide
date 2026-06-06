"""
Virtual Environments

A virtual environment is an isolated Python installation.
It lets you install packages for one project without affecting others.

HOW TO CREATE AND USE A VIRTUAL ENVIRONMENT:

# Create a virtual environment
python -m venv venv

# Activate it:
# On Windows:  venv\\Scripts\\activate
# On Mac/Linux: source venv/bin/activate

# Install packages in the environment
pip install requests pandas numpy

# Save dependencies to a file
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt

# Deactivate when done
deactivate

WHY USE VIRTUAL ENVIRONMENTS?
- Different projects need different package versions
- Keeps your system Python clean
- Makes projects portable and shareable
- Industry standard practice
"""

# Checking the Python executable in use
import sys
print("Python executable:", sys.executable)
print("Python version:", sys.version)

# Checking installed packages
import subprocess
result = subprocess.run([sys.executable, "-m", "pip", "list"], 
                      capture_output=True, text=True)
print("\nInstalled packages (first 10):")
lines = result.stdout.strip().split("\n")
for line in lines[:12]:
    print(line)
