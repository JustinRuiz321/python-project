import requests


def get_github_repositories(username):

    url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(url)

    if response.status_code == 200:
        repos = response.json()


        for repo in repos:
            print(f"Repository Name: {repo['name']}")
            print(f"Repository URL: {repo['html_url']}")
            print("-" * 40)
    else:
        print("Error fetching repositories. Status Code:", response.status_code)


# Example usage
if __name__ == "__main__":
    username = input("Enter the GitHub username: ")
    get_github_repositories(username)