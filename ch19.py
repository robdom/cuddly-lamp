"""

=====CREATE A NEW REPOSITORY ON GITHUB=====

Log in to Github account

Click on the + button at the top right corner of the screen

Click New Repository from the drop-down menu

Give the repository a name

Select the Public option, and check the box Initialize the Repository with a README

Click Create repository

Hit the button in the top right corner and select Your Profile
You will see the name of your repository
Click on the Clone or Download button
Save the link

=====DOWNLOAD LOCAL REPOSITORY=====

cd into the directory where you want to keep the repository

git clone [repository_url]

ls

Move files and folders into new local repository

=====UPDATE CENTRAL REPOSITORY WITH CHANGES FROM LOCAL REPOSITORY=====

# STAGE FILES

git status

git add <file> OR git add -A

git status again

[git reset <file> to unstage a file]

# COMMIT FILES

git commit -am [commit_message]

"If applied, this commit will [commit_message]"

# PUSH CHANGES

git push [-u] origin master OR git push

git log

# PULL CHANGES

git pull origin master

What about git init?

"""
