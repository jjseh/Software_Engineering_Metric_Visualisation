from github import Github
from pprint import pprint
import base64


# Github Username
# Get the URL to request
# API call for username
Url = f"https://api.github.com/users/{username}"
# Request information and return the information as a json

# Pretty print the JSON data/strings
pprint(collected_data)
 
github_username = input("Enter Github username: ")


try:
    authentication_token = input("Enter OAuth Token: ")
    accessToken = Github(authentication_token)
    githubUser = accessToken.get_user(github_username)
    print("Valid Token : Accepted")
except:
    print("invalid")
    accessToken = Github()
    githubUser = accessToken.get_user(github_username)
    
def repositoriesPrint(repositories):
     
     # Print Repository Content 
     for info in repositories.getInfo(""):
         print(info)
     # try catch - error handling
     try:
        print("License:", base64.b64decode(repositories.get_license().info.encode()).decode())
     except:
    print("Full name:", repositories.name)
    print("")
    # The date of when the repo was created
    # Show when Repository is created.
    print("Repository created on: ", repositories.repoCreated)
    print("")

if __name__ == '__main__':



