---
Title: Introduction to Git Commands
Date: 2022-09-09
Category: programming 
Tags: git
Status: published
Slug: git-basics
Summary: An introduction to version control with Git.
---

Here are some introductory Git commands to help with version control.

## Creating a gitignore file

Before starting, a file named `.gitignore` (no file extension) should be created within the project folder. In the case of a Python project (which is how I first encountered Git), it should contain the following text and nothing else:

```
__pycache__/
```

This tells Git to ignore any files in the `__pycache__` directory as we don't want these backed up.

---

## Initialising the repository ##

A repository is the set of files that Git is actively tracking. `git init` initialises the Git repository, which starts empty.

---

## Get repository status ##

The `git status` command lists the following:

* Current branch (i.e. version of the project)
* Which files are tracked (i.e. will be committed)
* Which files are untracked (i.e. will not be committed)

---

## Choosing files to commit ##

The `git add FILENAME` command adds the specified file to the repository. It does NOT commit the file - it just tells Git to start paying attention to it.

### Adding all files ###

`git add .` adds ALL files within a project that aren't already being tracked to the repository. As above, it does not commit them. Any files-- or files within folders-- specified within the `.gitignore` file will be ignored by this command.

### Removing added files before committing ###

To remove all files added (e.g. if you notice that you forgot to include a folder in your `.gitignore` file), *without* changing any edits made since the `add`, run `git reset --mixed`

---

## Committing files ##

`git commit` will commit files in their current state to the repository. Each time, we want to see a message stating that we have a clean working tree.

### Adding a commit message  ###

Use `git commit -m "TEXT"` to avoid the prompt to add a commit message that would otherwise appear. The -m flag will record the text that follows in the project's log.

### Simultaneously adding files and committing ###

`git commit -a` adds all files in the repository that have been modified after the last commit to the current commit. This bypasses the need to run `git add .` before committing.

NB: It's possible to use multiple flags simultaneously e.g. `-am`

---

## Viewing previous commits ##

Each time a commit is made, Git generates a unique 40-character reference ID. It also records who made the commit, when it was made, and any message recorded. Additionally, it reports the branch within which the commit was made. To see this history, run `git log`

### Returning a less detailed history ###

`git log --pretty=oneline` only returns the reference ID, branch and message. Useful when looking back over lots of commits.

---

## Examining previous versions of a project ##

`git checkout ID` will revert to a previous version of a project. The first six characters of the reference ID of the desired commit should be typed after the comment e.g. `git checkout abc123`. (To find this ID, run `git log`--see above.) This takes you out of the master branch and puts you in 'detached HEAD' state. (HEAD is the current committed state of the project.) You can commit any changes but can later discard them by performing another checkout.

### Saving changes to a new branch ###

`git checkout -b "NEW_BRANCH_NAME"` creates and saves a new branch which retains any commits made in detached HEAD mode. This does not overwrite the master branch.

### Returning to the master branch ###

`git checkout master` returns you to the `master` branch. If your master branch is instead called `main`, then use this instead.

### Abandoning changes ###

`git checkout .` abandons all changes made since the *last commit*, i.e. restores the project to the last committed state. Useful if you've completely broken something and can't figure out how.

---

## Renaming branches

`git branch -m old-name new-name`

---

## Deleting branches ##

`git branch -d "BRANCH_NAME"` deletes the specified branch. It is not possible to delete a branch whilst checking it out.

---

## Reverting to an old commit ##

`git reset --hard "FIRST SIX CHARACTERS OF REFERENCE ID"` permanently reverts to the commit at the specified reference ID.

---

## Deleting the repository ##

Use `rm -rf .git` to permanently delete the repository.

NB: **BE VERY CAREFUL WITH `rm -rf`**. The `-rf` flags stand for *recursive* (i.e. all sub-directories will be deleted) and *force* (i.e. the system will not ask you to confirm deletion). It is possible to accidentally and **permanently** delete things unintentionally, potentially even rendering your system irretrievable. Before using this command to delete a directory, it's a good idea to use `ls your-directory` to list the directory's contents, to double-check you are deleting the right one. Then, instead of re-typing the`rm` command and directory name, press your keyboard's `Up` key to load the last command (most terminal emulators will do this, to my knowledge), then change `ls` to `rm -rf`. That way, you can be certain of avoiding catastrophic typos.
