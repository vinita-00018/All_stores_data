import subprocess


def check_git_repo(repo_url):
    try:
        # Run 'git ls-remote' to check if the repo is accessible
        result = subprocess.run(["git", "ls-remote", repo_url], capture_output=True, text=True)

        if result.returncode == 0:
            print("Repository URL is valid and accessible.")
            print(result.stdout)  # Output remote references, such as branches/tags.
        else:
            print(f"Error: {result.stderr}")
            print("Repository URL is not accessible or incorrect.")

    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Test the function with the provided repository URL
repo_url = "https://github.com/vinita-00018/Dashboard_QE_APP.git"
check_git_repo(repo_url)
