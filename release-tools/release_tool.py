# Details:
#
# All release versions and release names are defined in the file 'releng/release_info.csv'.
# The next release will be 'Cake/1.2' defined in 'release.plist' file.
# Feature Flags settings are stored in the file 'featureflags/FF.csv'.
# Your code should be able to do at least the following:
#
# Create a separate git branch to represent the new release.
# Make sure the release file (release.plist) reflects the next release.
# Generate a feature flag report (text file is fine) to see what feature flags have changed since the last release.
# Requirements:
#
# Please create a dev branch 'release-dev' out of this repo, in your dev branch, create a directory "release-tools" for your code and put all your delieverables under that directory. Note: this 'release-dev' branch is not the release branch.
# Along with your code, include a write up of the test cases you would create in a text file in the "release-tools" directory. There is no need to create real tests.
# Once you finish, create a Pull Request against master of this repo
#
# cmdline options
# 1) deploytool newbranch => creates branch 'new-release'
# 2) Update release.plist deploytool bump # increment release.plist to next version
# 3) Generate feature flag report, to tell which FF's changed since last rel.

# PyGithub for talking to GithubAPI; pip install PyGithub

from github import Github
import csv


###########################################################
# Create commandline functionality using argparse
###########################################################


###########################################################
# Use CSV lib to create arrays of the files
###########################################################
# Load the CSV's into arrays
# Open the feature flag CSV
# ff = open("../featureflags/FF.csv")
# csv_ff = csv.reader(ff)
#
# # Open the release info csv_f
# rif = open("../releng/release_info.csv")
# csv_rif = csv.reader(rif)

rls_name = []
rls_ver = []

# Load into array using csv's DictReader function
for cell in csv.DictReader(open('../releng/release_info.csv')):
    rls_name.append(cell['rls_name'])
    rls_ver.append(cell['rls_ver'])

print("release names = {}".format(rls_name))
print("Release versions = {}".format(rls_ver))

# We'd do something similiar with FF.csv to read in, then modify


###########################################################
# Use pyGithub to create branch
###########################################################

# Open and read the token
tokey = open('auth_token').read()

# Use an access token for github access. Use rstrip to rip off the white space and \n
gitobj = Github(tokey.rstrip())

# Currently a permissions issue creating a branch in the slack repo,
# So i'm testing pointing at one of my current repos 
# repoName = "br-code-exercise-82044407"
repoName = "lpic101"
source_branch = 'master'

# Create new release branch name from rel version
# # Create the name of the rel branch
target_branch = 'release_' + rls_name[2] + '.' + rls_ver[1]

repo = gitobj.get_user().get_repo(repoName)
sb = repo.get_branch(source_branch)
repo.create_git_ref(ref='refs/heads/' + target_branch, sha=sb.commit.sha)

###########################################################
# Update release.plist
###########################################################

# Find location of the ver number after line CFBundleShortVersionString
# Replace it
#
# with fileinput.FileInput('../release.plist', inplace=True, backup='.bak') as file:
#     for line in file:
        # print(line.replace(text_to_search, replacement_text), end='')
