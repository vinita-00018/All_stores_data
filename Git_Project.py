import subprocess
import os

try:
    folder_path = "D:\\Vinita\\Project\\Final_Project_Streamlit"
    repository_url = "https://github.com/vinita-00018/Fetcher_data.git"

    os.chdir(folder_path)

    # Ensure Git is initialized
    subprocess.run(["git", "init"], check=True)

    # Check if 'origin' remote already exists
    result = subprocess.run(["git", "remote"], capture_output=True, text=True)
    if "origin" not in result.stdout:
        subprocess.run(["git", "remote", "add", "origin", repository_url], check=True)
    else:
        print("Remote 'origin' already exists. Skipping addition.")

    # Ensure we are on the correct branch
    subprocess.run(["git", "branch", "-M", "main"], check=True)

    # Add all files
    subprocess.run(["git", "add", "--all"], check=True)

    # Check if there's anything to commit
    result = subprocess.run(["git", "status"], capture_output=True, text=True)
    if "nothing to commit" in result.stdout:
        print("No changes to commit.")
    else:
        commit_message = "Initial commit or your custom message"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # Push changes
    subprocess.run(["git", "push", "-u", "origin", "main"], check=True)

    print("Folder has been successfully pushed to GitHub!")

except subprocess.CalledProcessError as e:
    print(f"Git command failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
