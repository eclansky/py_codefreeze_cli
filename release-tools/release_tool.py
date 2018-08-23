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

# WIP
# Bump release.plist ver using awk/sed/ or py type string tool
# Gen FF report
# Logic to check if branch exists, abort, (idempotent)

# PyGithub for talking to GithubAPI; pip install PyGithub
from github import Github
from pathlib import Path
import csv
import argparse
import sys
import plistlib

###########################################################
# Use CSV lib to create arrays of the files, and make releases lib
###########################################################

rls_name = []
rls_ver = []
releases = {}

# Load into arrays using csv's DictReader function
for cell in csv.DictReader(open('../releng/release_info.csv')):
    rls_name.append(cell['rls_name'])
    rls_ver.append(cell['rls_ver'])

# Create dictionary out of the two arrays for later use and accessiblity.
releases = dict(zip(rls_name, rls_ver))
# print("Here's our releases dictionary {}".format(releases))



###########################################################
# Use pyGithub to create branch
###########################################################

# Open and read the token
tokenfile = Path('auth_token')
if tokenfile.is_file():
    tokey = open('auth_token').read()
    # Use an access token for github access. Use rstrip to rip off the white space and \n
    gitobj = Github(tokey.rstrip())
else:
    print("\nGithub auth_token is not in the release-tools dir!! Aborting mission!\n")
    exit()


# Currently a permissions issue creating a branch in the slack repo,
# So i'm testing pointing at one of my current repos
# repoName = "br-code-exercise-82044407"
repoName = "lpic101"
source_branch = 'master'

# Create target_branch name from rel version using argument and corresponding value
# in dict
# IF argument exists, Build target branch name
if len(sys.argv) > 1:
    if sys.argv[1] in releases:
        target_branch = 'release_' + sys.argv[1] + releases[sys.argv[1]]

repo = gitobj.get_user().get_repo(repoName)
sb = repo.get_branch(source_branch)


###########################################################
# Create commandline functionality using argparse
###########################################################
# Make function we can call based on CLI input
def create_branch(version, target_branch):
    print("Releasing build {} to new branch".format(target_branch))
    repo.create_git_ref(ref='refs/heads/' + target_branch, sha=sb.commit.sha)
parser = argparse.ArgumentParser()

# Create an argument that ideally takes in the input and releases correct version
parser.add_argument("version", help="Version to release? ")
args = parser.parse_args()

# Was working on a way to test if branch exsisted before trying to create one.
# showbr = repo.get_branches()
# print("\nThe branches that exist are {}\n".format(showbr))


# need logic to test if branch already exists.
if args.version == 'Apple':
    create_branch(sys.argv[1], target_branch)

elif args.version == 'Cake':
    create_branch(sys.argv[1], target_branch)

# Throws error if user doesnt enter one of the available arguments
elif sys.argv[1] not in releases:
    print("You must enter one of the following versions as an argument (case-sensitive): Apple, Cake")

###########################################################
# Update release.plist using plistlib
###########################################################

# print("Updating Plist file version to {}".format(releases[sys.argv[1]]))
# p = plistlib.readPlist('../release.plist')
# if "CFBundleShortVersionString" in p:
#     p["CFBundleShortVersionString"] = releases[sys.argv[1]]
#     plistlib.writepPlist(p, '../release.plist')
