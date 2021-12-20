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
    print("\n*****************************************************************************************\n ")
    print(" Invalid Credentials! ")
    print(" Program will execute with invalid token. RateLimited!!!\n")
    print("***************************************************************************************** ")
    accessToken = Github()
    githubUser = accessToken.get_user(github_username)
    

print(" Program running......")
print(" Program execution time is dependant on the number of repositories owned by searched github user.\n ")


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



# Make Data Visualisation
if __name__ == '__main__':
    
    # Chart to Visualise number of Stars 
    stackChart = pygal.StackedBar(style = DRKS)
    # Set Chart display
    stackChart.width = 1600
    stackChart.height = 740
    # Title of chart
    stackChart.title = f"Number of Stars for each Github Repository owned by {githubUser.login}"
    # Add data accessed from github onto chart
    count = 0
    for name in namesOfRepos:
        stackChart.add(name, startCount[count])
        count = count + 1
    # Open bar chart in browser
    stackChart.render_in_browser()
    # Save chart inside folder for easier viewing 
    stackChart.render_to_file('OutputtedCharts/starsChart.svg')
  
  
    # print(" ")
    # Pie chart for Visualise Languagues count
    pieChart = pygal.Pie(inner_radius=.4, style = DRKS)
    # Set chart display
    pieChart.width = 1600
    pieChart.height = 740
    # Title of Pie Chart
    pieChart.title = f"Number of Github Repositories owned by {githubUser.login} using a certain Language."
    # Add the data accessed from github onto pie chart
    numberofLang = 0
    for language in languages:
        pieChart.add(language, languages[language])
        numberofLang = numberofLang + 1
    # Open bar chart in browser
    pieChart.render_in_browser()
    # Save chart inside folder for easier viewing 
    pieChart.render_to_file('OutputtedCharts/languagePieChart.svg')


    # BarChart for Visualising Commit count
    barChart = pygal.Bar(set_Syling,style = DRKS)
    # Title of Bar Chart
    barChart.title = f"Github Repositories owned by {githubUser.login} and Commits of each Repository"
    # Define x axis of chart
    barChart.x_labels = namesOfRepos
    # Add the data accessed from github onto bar chart
    barChart.add("", numberOfCommits)
    # Open bar chart in browser
    barChart.render_in_browser()
    # Save chart inside folder for easier viewing 
    # If OAuth Token is invalid or not enter code execution will be ratelimited so after 
    # each execution relevent charts generated will be saved in the folder.
    barChart.render_to_file('OutputtedCharts/commitsBarChart.svg')