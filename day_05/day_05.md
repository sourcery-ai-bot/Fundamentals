# Fundamentals Day 05  

Let's talk a little about [git](https://git-scm.com/docs). Git is a very useful tool for saving code change history, and other things.  

## Git

```
git init
```

`git init` initializes a git repository. What this means is that the program git creates a hidden directory and starts to track changes in the directory you are in.


`git commit` will _commit_ (or save) the history of change for the files that were staged.

```
git log
```
`git log` shows the commit history.

```
git show <commit hash>
```
`git show` will show the actual changes for a given commit.

```
git remote add <remote name> <remote address>
```
`git remote add` is used to add an address and name for a remote repository. For example `git remote add origin https://github.com/compsciacademy/Git_Fun.git`. This will add a remote named `origin` at the address `https://github.com/compsciacademy/Git_Fun.git`

You can view your git remotes with the `-v` or `--verbose` option, i.e. `git remote -v`.

```
git push <remote name> <branch name>
```

`git push` is used to push the local commits to the remote. For example, if I want to push the changes on my master branch to the `origin` remote, I can use `git push origin master`.

`git commit --amend` will open up your default editor, which is maybe VI or VIM (hint: `:w` to write/save changes, `:q` to quit).

If you amend a commit that you have already pushed, you will need to force push, e.g. `git push -f origin master`.
