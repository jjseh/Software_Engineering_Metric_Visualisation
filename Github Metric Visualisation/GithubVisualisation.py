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
    # Show what language each Repository is mainly coded in
    print("Language:", repositories.language)
    print("")
    # Stars
    # Show what Repositories are stared and count of stars
    print("Number of stars:", repositories.starCount)


listOfRepositories = {} 
languages = {}

# Count the number of Repositories
def addRepositoryToList(repositories):
    # Catch Error 
    try:
        if repositories.get_commits() is not None:
            commits = repositories.get_commits().totalCount
            listOfRepositories[f"{repositories.name}"] = commits
    except:
        listOfRepositories[f"{repositories.name}"] = 0

def addLanguagesOfRepositories(repositories):
    if repositories is not None:
        language = repositories.language
        if language in languages:
            languages[language] = languages[language] + 1

def printRepoCommits(repositories):

    try:
        if repositories.get_commits() is not None:
            commits = repositories.get_commits().totalCount
    except:
        print("The number of commits = 0")

numberOfLanguages = []

numberOfCommits = []

# Count and add each Language to array.
for lang in languages:
    numberOfLanguages.append(languages[lang])

# Count and add each Repository to array.
for reps in listOfRepositories:
    numberOfCommits.append(listOfRepositories[reps])



#if __name__ == '__main__':



