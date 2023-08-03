import requests
import textwrap
import re

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
            print("+{}+".format("-" * 74))
            title_lines = textwrap.wrap(issue['title'], width=65)
            url_lines = textwrap.wrap(issue['html_url'], width=65)
            body_lines = textwrap.wrap(issue['body'], width=65)
            print("| State: {:65} |".format(issue['state']))
            print("| Title: {:65} |".format(title_lines[0]))
            for line in title_lines[1:]:
                print("|        {:65} |".format(line))
            print("| URL:   {:65} |".format(url_lines[0]))
            for line in url_lines[1:]:
                print("|        {:65} |".format(line))
            print("| Body:  {:65} |".format(body_lines[0]))
            for line in body_lines[1:]:
                print("|        {:65} |".format(line))
            print("+{}+".format("-" * 74))
            print("\n")
    else:
        print("No issues found or the repository does not exist.")

def main():
    while True:
        repo_input = input("Please enter a repository in the format username/repo or 'q' to quit: ")
        repo_input = re.sub('[^a-zA-Z0-9_\-/.]', '', repo_input)
        repo_input = re.sub('/+', '/', repo_input)
        repo_input = repo_input.rstrip('/')
        repo_input = repo_input.lstrip('/')

        if repo_input.lower() == 'q':
            break

        try:
            user, repo = repo_input.split('/')
            if not user or not repo:
                raise ValueError
        except ValueError:
            print("Invalid format. Please use the format 'username/repo'")
            continue

        issues = get_issues(user, repo)
        print_issues(issues)

if __name__ == "__main__":
    main()
