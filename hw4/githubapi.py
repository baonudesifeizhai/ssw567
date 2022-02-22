import requests
import json

def GithubApi(username):
    response = requests.get("https://api.github.com/users/"+username+"/repos")
    
    if response.status_code != 200:
        print("No Account with that Username/No Response")
        return False

    response = response.json()

    if len(response) == 0:
        print("No Repositories")
        return False
  
    for repo in response:
        repoResponse = requests.get(repo['commits_url'].split("{")[0])
        repoResponse = repoResponse.json()
        print("Repository Name: "+ repo['name'] + " \t\t\t\tNumber Of Commits: " + str(len(repoResponse)))
   
    return True

if __name__ == "__main__":
    userInput = input("enter github username: ")
    GithubApi(userInput)
