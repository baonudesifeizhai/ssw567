import requests
import json

def connect(user):
    code200 = True
    repo_url = "https://api.github.com/users/%s/repos" ## % (userid)
    commit_url = "https://api.github.com/repos/%s/%s/commits" ## % (id, repo)
    repos = {}

  
    repo_page = requests.get(repo_url % user)
    if repo_page.status_code == 200:
        repo_data = repo_page.json()
        ## Parse Repositories
        for each in repo_data:
            repo_name = each["name"]
            ## Get Repo Commits
            commit_page = requests.get(commit_url % (user, repo_name))
            if commit_page.status_code == 200:
                commit_data = commit_page.json()
                repos[repo_name] = commit_data
                print("Repo: ", repo_name, "   Commits: ", len(commit_data))
            else:
                print("No Connection: Line 26")
                code200 = False
    else:
        print("No Connection: Line 18")
        code200 = False
        
    return  repos

## Run Program
def run():
    user = input("Please enter a GitHub user ID: ")
    try:
        connect(user)
    except(AttributeError):
        print("Unable to find an acount with that username")


if __name__ == '__main__':
    run()
