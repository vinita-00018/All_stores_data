import subprocess
import os


def handle_submodule():
    # Check if 'data' is a submodule
    result = subprocess.run(["git", "submodule", "status", "data"], capture_output=True, text=True)
    if result.returncode == 0:  # This means 'data' is a submodule
        print("Submodule 'data' found. Committing changes in submodule.")
        subprocess.run(["git", "submodule", "update", "--remote"], check=True)  # Update submodule
        subprocess.run(["git", "add", "data"], check=True)  # Stage submodule changes
        subprocess.run(["git", "commit", "-m", "Updated data submodule"], check=True)  # Commit submodule changes
        subprocess.run(["git", "push"], check=True)  # Push submodule changes


def main():
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

        # Handle submodule if exists
        handle_submodule()

        # Add all changes
        subprocess.run(["git", "add", "."], check=True)

        # Commit changes
        commit_message = "Initial commit or your custom message"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push to remote repository
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)

        print("Folder has been successfully pushed to GitHub!")

    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
