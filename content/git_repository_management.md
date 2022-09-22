Title: Uploading / Downloading Remote Repositories on GitHub
Date: 2022-09-10
Category: programming
Tags: git
Status: published
Slug: git-repositories
Summary: How to upload a local Git repository to GitHub.

This is a quick summary describing how to create and upload a local Git repository to a remote repository on GitHub. It also 

## Uploading to a remote repo

1. Create the remote repository on the GitHub website--this is straightforward, just follow the prompts
1. Create a `.gitignore` file in the local directory. Add to this any files or folders that should not be committed
1. Run `git init` in the local directory
1. Run `git add .`
1. Run `git commit -m "Commit message."`
1. Run `git remote add origin https://github.com/your-github-username/name-of-repo.git`
1. Run `git push -u origin main` (main is my default name)

You'll need to put in your username and password at various points.

---

## Removing the remote repo

To do this run `git remote remove origin` or whatever you've used instead of origin for the name. (Think origin is customary.)

---

## Renaming the main aka master branch.

Run `git branch -M new-name`

---

## Downloading remote repositories from GitHub

To download a repo from GitHub (e.g. to a new machine), run `git clone https://github.com/your-github-username/name-of-repo.git` By default, this will save the repository in the current directory, in a folder with the same name as the repository. If the repository is private, you will need to enter a username and password.
