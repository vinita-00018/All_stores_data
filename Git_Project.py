
import subprocess
import os

try:
    folder_path = "D:\\Vinita\\Project\\Final_Project_Streamlit"
    repository_url = "https://github.com/vinita-00018/Dashboard_QE_APP.git"
    os.chdir(folder_path)
    # Ensure Git is initialized
    subprocess.run(["git", "init"], check=True)
    # Check if 'origin' remote already exists
    result = subprocess.run(["git", "remote"], capture_output=True, text=True)
    if "origin" not in result.stdout:
        subprocess.run(["git", "remote", "add", "origin", repository_url], check=True)
    else:
        print("Remote 'origin' already exists. Skipping addition.")

    subprocess.run(["git", "add", "."], check=True)
    commit_message = "Initial commit or your custom message"
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
    print("Folder has been successfully pushed to GitHub!")
except subprocess.CalledProcessError as e:
    print(f"Git command failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
