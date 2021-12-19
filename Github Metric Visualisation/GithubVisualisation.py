from github import Github
from pprint import pprint
#import base64



# Github Username
# Get the URL to request
# API call for username
# Url = f"https://api.github.com/users/{username}"
# Request information and return the information as a json
#
# Pretty print the JSON data/strings
# pprint(collected_data)
# 


# Accessing Github API
github_username = input("Enter Github username: ")

# try catch errors and return error to user if necessary
try:
    authentication_token = input("Enter OAuth Token: ")
    accessToken = Github(authentication_token)
    githubUser = accessToken.get_user(github_username)
    print("Valid Token : Accepted")
except:
    print(" Invalid Credentials! ")
    accessToken = Github()
    githubUser = accessToken.get_user(github_username)
    

print(" Program running......")



# Print Repository inforamtion
# Function returns: 
#       Repository Name
#       Date Repository was made
#       Language used in the each Repository
#       Numbers of stars per Repository

# Used for testing Github API access
def repositoriesPrint(repositories):
    # 
    # Print Repository Content 
    # for info in repositories.getInfo(""):
    #     print(info)
    #  try catch - error handling
    # try:
    #    print("License:", base64.b64decode(repo.get_license().info.encode()).decode())
    # except:
    #    
    # Name of the Repository
    print("Full name:", repositories.name)
    print("")
    # The date of when the repo was created
    # Show when Repository is created.
    print("Repository created on: ", repositories.repoCreated)
    print("")
    # Language
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


# Count number of languages used in each Repository
def addLanguagesOfRepositories(repositories):
    if repositories is not None:
        language = repositories.language
        if language is None:
            language = "No language"
        if language in languages:
            languages[language] = languages[language] + 1
        else:
            languages[language] = 1


# Print the number of commits made in each of the repositories
def printRepoCommits(repositories):
    # Catch Error - If no commits
    try:
        if repositories.get_commits() is not None:
            commits = repositories.get_commits().totalCount
            print(f"The number of commits = {commits}")
    except:
        print("The number of commits = 0")


# print(numberOfCommits)
# print(" ")
# print(namesOfRepos)
namesOfRepos = []
numberOfCommits = []
languageNames = []
numberOfLanguages = []
startCount = []

numberofStars = 0
# Count stars 
for repository in githubUser.get_repos():
    if repository.stargazers_count == 0:
        startCount.append(0)
    else: 
        startCount.append(repository.stargazers_count)
    addRepositoryToList(repository)
    addLanguagesOfRepositories(repository)


# Count and add each Language to array.
for lang in languages:
    languageNames.append(lang)
    numberOfLanguages.append(languages[lang])

# Count and add each Repository to array.
for reps in listOfRepositories:
    namesOfRepos.append(reps)
    numberOfCommits.append(listOfRepositories[reps])

#if __name__ == '__main__':



