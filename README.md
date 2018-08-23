A python CLI simulated release tool 
An assignment I did.

Details:
1. All release versions and release names are defined in the file 'releng/release_info.csv'.
2. The next release will be 'Cake/1.2' defined in 'release.plist' file.
3. Feature Flags settings are stored in the file 'featureflags/FF.csv'.

Your code should be able to do at least the following:
1. Create a separate git branch to represent the new release.
2. Make sure the release file (release.plist) reflects the next release.
3. Generate a feature flag report (text file is fine) to see what feature flags have changed since the last release.

Requirements:
1. Please create a dev branch 'release-dev' out of this repo, in your dev branch, create a directory "release-tools" for your code and put all your delieverables under that directory. Note: this 'release-dev' branch is not the release branch.
2. Along with your code, include a write up of the test cases you would create in a text file in the "release-tools" directory. There is no need to create real tests.

