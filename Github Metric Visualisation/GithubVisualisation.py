from github import Github
from pprint import pprint
import pygal
from pygal.style import DarkSolarizedStyle as DRKS
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

# Set the styling, used to visualise the collected data
set_Syling = pygal.Config()
set_Syling.width = 1030
set_Syling.height = 485
set_Syling.truncate_label = 15
set_Syling.x_label_rotation = 45
set_Syling.show_y_guides = False
set_Syling.show_legend = False
set_Syling.title_font_size = 25
set_Syling.label_font_size = 15
set_Syling.major_label_font = 18

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

if __name__ == '__main__': 
   
    stackChart = pygal.StackedBar(style = DRKS)
    stackChart.width = 1600
    stackChart.height = 740
    stackChart.title = f"Number of Stars for each Github Repository owned by {githubUser.login}"
    count = 0
    for name in namesOfRepos:
        stackChart.add(name, startCount[count])
        count = count + 1
    stackChart.render_in_browser()
    stackChart.render_to_file('OutputtedCharts/starsChart.svg')


    pieChart = pygal.Pie(inner_radius=.4, style = DRKS)
    pieChart.width = 1600
    pieChart.height = 740
    pieChart.title = f"Number of Github Repositories owned by {githubUser.login} using a certain Language."
    numberofLang = 0
    for language in languages:
        pieChart.add(language, languages[language])
        numberofLang = numberofLang + 1
    pieChart.render_in_browser() 
    pieChart.render_to_file('OutputtedCharts/languagePieChart.svg')


    barChart = pygal.Bar(set_Syling,style = DRKS)
    barChart.title = f"Github Repositories owned by {githubUser.login} and Commits of each Repository"
    barChart.x_labels = namesOfRepos
    barChart.add("", numberOfCommits)
    barChart.render_in_browser()
    barChart.render_to_file('OutputtedCharts/commitsBarChart.svg')