import os
import subprocess

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# List all files in the current directory
files = os.listdir(current_dir)

# Filter out files that start with 'Test' and end with '.py'
test_files = [f for f in files if f.startswith('[Test]') and f.endswith('.py')]

# Execute each test file one by one
for test_file in test_files:
    print(f"Executing {test_file}...")
    subprocess.run(['python3', os.path.join(current_dir, test_file)])