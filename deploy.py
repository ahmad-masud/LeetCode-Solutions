import os
import subprocess
import sys

def deploy():
    # Check if a commit message was provided
    if len(sys.argv) < 2:
        print("Error: No commit message provided.")
        print("Usage: python deploy.py \"Your commit message\" [extra git args]")
        sys.exit(1)

    # Extract commit message and additional arguments
    commit_message = sys.argv[1]
    extra_args = sys.argv[2:]  # Capture any additional arguments passed after the commit message

    # Run package.py
    result = subprocess.run(["python", "package.py"], capture_output=True, text=True)
    if result.returncode != 0:
        print("Error running package.py:")
        print(result.stderr)
        sys.exit(1)

    # Stage all changes
    subprocess.run(["git", "add", "."], check=True)

    # Commit with the provided message
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # Push changes with additional arguments (if any)
    push_command = ["git", "push"] + extra_args
    subprocess.run(push_command, check=True)

if __name__ == "__main__":
    deploy()