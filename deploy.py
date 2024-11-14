import os
import subprocess
import sys

def deploy():
    # Check if a commit message was provided
    if len(sys.argv) < 2:
        print("Error: No commit message provided.")
        print("Usage: python deploy.py \"Your commit message\"")
        sys.exit(1)

    commit_message = sys.argv[1]

    # Run package.py
    result = subprocess.run(["python", "package.py"], capture_output=True, text=True)
    if result.returncode != 0:
        print("Error running main.py:")
        print(result.stderr)
        sys.exit(1)

    # Stage all changes
    subprocess.run(["git", "add", "."], check=True)

    # Commit with the provided message
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # Push changes
    subprocess.run(["git", "push"], check=True)

if __name__ == "__main__":
    deploy()