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
# 1) deploytool newbranch
# 2) Update release.plist deploytool bump # increment release.plist to next version
# 3) Generate feature flag report, to tell which FF's changed since last rel.
