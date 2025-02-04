import subprocess
import os

try:
    folder_path = "D:\\Vinita\\Project\\Final_Project_Streamlit"
    repository_url = "https://github.com/vinita-00018/All_stores_data.git"  # Correct URL

    os.chdir(folder_path)

    # Ensure Git is initialized
    subprocess.run(["git", "init"], check=True)

    # Check if 'origin' remote already exists
    result = subprocess.run(["git", "remote"], capture_output=True, text=True)
    if "origin" not in result.stdout:
        subprocess.run(["git", "remote", "add", "origin", repository_url], check=True)
    else:
        print("Remote 'origin' already exists. Skipping addition.")

    # Update the remote URL to ensure it's correct
    subprocess.run(["git", "remote", "set-url", "origin", repository_url], check=True)

    # Ensure we are on the correct branch
    subprocess.run(["git", "branch", "-M", "main"], check=True)

    # Check if there are unstaged or uncommitted changes
    status_result = subprocess.run(["git", "status"], capture_output=True, text=True)

    if "nothing to commit" in status_result.stdout:
        print("No changes to commit.")
    else:
        # Option 1: Commit the changes
        subprocess.run(["git", "add", "--all"], check=True)
        commit_message = "Initial commit or your custom message"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print("Changes committed.")

        # Option 2: (Alternative) Stash the changes if you don't want to commit
        # subprocess.run(["git", "stash"], check=True)  # Uncomment this to use stashing
        # print("Changes stashed.")

    # Pull the latest changes from the remote repository
    subprocess.run(["git", "pull", "--rebase", "origin", "main"], check=True)

    # Push changes to the remote repository
    subprocess.run(["git", "push", "-u", "origin", "main"], check=True)

    print("Folder has been successfully pushed to GitHub!")

except subprocess.CalledProcessError as e:
    print(f"Git command failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
