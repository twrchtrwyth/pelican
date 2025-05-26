---
Title: Uploading / Downloading Remote Repositories on GitHub
Date: 2022-09-10
Category: programming
Tags: git
Status: published
Slug: git-repositories
Summary: How to upload a local Git repository to GitHub.
---

This is a quick summary describing how to create and upload a local Git repository to a remote repository on GitHub.

# Uploading to a remote repo

First, create the remote repository on the GitHub website--this is straightforward, just follow the prompts.  On your machine, create a `.gitignore` file in the local directory.  Add to this file the names of any files or folders that should not be committed.  Wildcards are accepted.

Next, run the following in the local directory:

```shell
git init
git add .
git commit -m "Commit message."
git remote add origin https://github.com/your-github-username/name-of-repo.git
git push -u origin main
```

*NB: The default branch name is* `master`, *but I use* `main`

Username and password will be required at various points.

---

# Removing the remote repo

```shell
git remote remove origin
```

*Or whatever you've used instead of* `origin` *for the name.* *(*`origin` *is customary.)*

---

# Using SSH keys instead of HTTPS

To authenticate with an SSH key instead of HTTPS and a password (which is a massive pain in the arse when using multiple machines), first [generate an ssh key pair][ssh] on your machine.  Then, on GitHub navigate to *settings/keys* within your profile.  Click the *New SSH Key* button, assign it a name, and copy the full contents of `id_rsa.pub` to the relevant field.  (Complete two-factor authentication as needed.)

[ssh]: {filename}/pages/grimoire.md#ssh "My page on ssh"

If you have already used HTTPS for a repo on the machine, simply follow the above process for removing a remote repo and then set the new SSH-compatible origin with the following command:

```shell
git remote add origin git@github.com:user/repo.git
```

---

# Renaming the main (aka master) branch.

```shell
git branch -M new-name
```

---

# Downloading remote repositories from GitHub

To download a repo from GitHub, run:

```shell
git clone https://github.com/your-github-username/name-of-repo.git
```

By default, this will save the repository in the current directory, in a folder with the same name as the repository.  If the repository is private, you will need to enter a username and password.  Alternatively you can use the SSH-style URL as described above.
