import requests

def get_issues(user, repo):
    url = f"https://api.github.com/repos/{user}/{repo}/issues"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def print_issues(issues):
    if issues is not None:
        for issue in issues:
            print(f"Title: {issue['title']}\nURL: {issue['html_url']}\nState: {issue['state']}\n")
    else:
        print("No issues found or the repository does not exist.")

def main():
    while True:
        repo_input = input("Please enter a repository in the format username/repo or 'q' to quit: ")
        if repo_input.lower() == 'q':
            break

        try:
            user, repo = repo_input.split('/')
        except ValueError:
            print("Invalid format. Please use the format 'username/repo'")
            continue

        issues = get_issues(user, repo)
        print_issues(issues)

if __name__ == "__main__":
    main()
