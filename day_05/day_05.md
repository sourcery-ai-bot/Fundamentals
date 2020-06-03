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

## Handling Errors

Sometimes, you will have errors. How you choose to handle errors (or not) is up to you :)

```python
while True:
    try:
        x = int(input("give me a number: "))
    except ValueError:
        print("There was an error")

```

## Reading from and Writing to Files  
  
We worked on a program that allowed us to view, add, and remove users. Let's add edit (or update) to the list of options, and let's store users in a file. That way, we can save the list of users when we exit the program. Think about what the file should look like.


## Exercise 01

Create two files in a directory, `app.py` and `lol`

lol
```
this is line 1
here is another line
the third line is here

```

app.py
```python
my_file = open('lol')

for line in my_file:
    print(line)

my_file = open('lol', 'w')
my_file.write("Here is a new line!")
```

If you run the app, you'll notice it overwrites the file. Using what you know now, write some code such that you can add a new line to a file without losing the file data.

e.g. the result should be:

lol
```
this is line 1
here is another line
the third line is here
Here is a new line!

```

Exercise 01 Answer
```
my_file = open('some_file', 'a')

my_file.write("Here is a new line!\n")

f = open('some_file', 'r')

for line in f:
    print(line, end='')

```

## Exercise 02

a.) Write a program that prompts the user to enter their name. The program should allow you to enter your name or view all entries. It should also store the names in a file.

b.) Next, add the ability to update a name (by index).
