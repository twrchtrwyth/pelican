---
Title: Introduction to Git Commands
Date: 2022-09-09
Category: programming 
Tags: git
Status: published
Slug: git-basics
Summary: An introduction to version control with Git.
---

Here are some introductory Git commands to help with version control. There is further information on managing repos [here]({filename}git_repository_management.md).

## Creating a gitignore file

Before starting, a file named `.gitignore` (no file extension) should be created within the project directory. In the case of a Python project (which is how I first encountered Git), it should contain the following text and nothing else:

```
__pycache__/
```

This tells Git to ignore any files in the `__pycache__` directory as we don't want these backed up.

---

## Initialising the repository ##

A repository is the set of files that Git is actively tracking. `git init` initialises the Git repository, which starts empty.

---

## Get repository status ##

```
git status
```

Lists the following:

* Current branch (i.e. version of the project)
* Which files are tracked (i.e. will be committed)
* Which files are untracked (i.e. will not be committed)

---

## Choosing files to commit ##

```
git add <filename>
```

Adds the specified file to the repository. It does not commit the file--rather it tells Git to start paying attention to it.

### Adding all files ###

```
git add .
```

Adds all files within a project that aren't already being tracked to the repository. As above, it does not commit them. Any files--or files within directories--specified within the `.gitignore` file will be ignored by this command.

### Removing added files before committing ###

```
git reset --mixed
```

Removes all files added (e.g. if you notice that you forgot to include a directory or file in your `.gitignore` file), *without* changing any edits made since files were added.

---

## Committing files ##

```
git commit
``` 

Commits files in their current state to the repository. Each time, we will want to see a message stating that we have a clean working tree.

### Adding a commit message  ###

```
git commit -m "<message>"
```

Avoids the editor opening to add a commit message (that would otherwise appear). The `-m` flag will record the text that follows in the project's log.

### Simultaneously adding files and committing ###

```
git commit -a
```

Adds all files in the repository that have been modified after the last commit to the current commit. This bypasses the need to run `git add .` before committing.

NB: It's possible to use multiple flags simultaneously e.g. `-am`

---

## Viewing previous commits ##

```
git log
```

Each time a commit is made, Git generates a unique 40-character reference ID. It also records who made the commit, when it was made, and any message recorded. Additionally, it reports the branch within which the commit was made. To see this history in full, run the above command.

### Returning a less detailed history ###

```
git log --pretty=oneline
```

If wanting a quick overview of commits, the above command returns just the reference ID, branch and message.

---

## Examining previous versions of a project ##

```
git checkout <ID>
```

Reverts to a previous version of a project. The first six characters of the reference ID of the desired commit should be typed after the comment e.g. `git checkout abc123`. (To find this ID, run `git log`--see above.) This takes you out of the master branch and puts you in *detached HEAD* state. (HEAD is the current committed state of the project.) You can commit any changes made, and/or can discard them by performing another checkout.

### Saving changes to a new branch ###

```
git checkout -b "<new_branch_name>"
```

Creates and saves a new branch which retains any commits made in detached HEAD mode. This does not overwrite the master branch.

### Returning to the master branch ###

```
git checkout master
```

Returns you to the `master` branch. If your master branch is instead called `main`, then use this instead.

### Abandoning changes ###

```
git checkout .
```

Abandons all changes made since the *last commit*, i.e. restores the project to the last committed state. Useful if you've completely broken something and can't figure out how.

---

## Renaming branches

```
git branch -m old-name new-name
```

---

## Deleting branches ##

```
git branch -d "<branch_name>"
```

Deletes the specified branch. It is not possible to delete a branch whilst checking it out.

---

## Reverting to an old commit ##

```
git reset --hard "<ID>"
```

Permanently reverts to the commit at the specified reference ID.  As with the `checkout` command above, use the first six characters of the reference ID (which can be found in the log).

---

## Deleting the repository ##

```
rm -rf .git
```

Permanently deletes the repository.

NB: **BE VERY CAREFUL** with `rm -rf`. The `-rf` flags stand for *recursive* (i.e. all sub-directories will be deleted) and *force* (i.e. the system will not ask you to confirm deletion). It is possible to accidentally and **permanently** delete things unintentionally, potentially even rendering your system irretrievable. Before using this command to delete a directory, it's a good idea to use `ls your-directory` to list the directory's contents, to double-check you are deleting the right one. Then, instead of re-typing the`rm` command and directory name, press your keyboard's `Up` key to load the last command (most terminal emulators will do this, to my knowledge), then change `ls` to `rm -rf`. That way, you can be certain of avoiding catastrophic typos.
