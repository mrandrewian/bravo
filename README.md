#bravo
<sup>2 Bros + 1 Strava Api = Bravo</sup>

##VERY IMPORTANT NOTE ABOUT USING GITHUB!!!
**This is a public repository.**  That doesn't mean than anyone can edit the files. but it does mean that anyone can SEE the files.  There are bots crawling github constantly that are created to catch people that inadvertently post private information.  This can be anything from addresses and credit card numbers to private API keys.  This isn't meant to scare you, just to make you aware.  There are plenty of good ways to use sensitive information within public repositories if you are careful and deliberate.

## Installing Git and Setting up github access
There are a few steps involved with wetting up github access on your machine.  Follow these steps in order

1. [Download Git](https://git-scm.com/download/mac)
2. [Generate an SSH key](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/) (unless you have a good reason to set a passphrase, you can go ahead and leave it blank by hitting "enter" at the prompt)
3. [Add your SSH key to Github](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)


## Git basics
Before you start working (this part is important!)
`git pull`
After you have made a change that you want to publish to github
`git status` 
Verify that all of the files listed are files that you modified and would like to publish
`git add -A`
`git commit -m "message describing the change you made here"`
`git push`
Congratulations!  Your update is on github!

![Exmaple Terminal Output](http://i.imgur.com/CYClTN3.png)

----------
####If you find yourself in times of trouble
If you need to revert a specific file to the version that is currently on github (abandoning "local" changes) you can use `git checkout file.foo`
Examples:
`git checkout styles.css`
`git checkout index.html`
`git checkout scripts.js`

If you have gotten yourself totally lost and just want to revert EVERYTHING back to the gtihub version you can use `git reset --hard`

[If you want to learn more, start here!](https://try.github.io/)

####When something goes wrong (and it will) do not panic!
Git is complicated and can be frustrating at times, but it is a great tool and is the best way to collaborate on code.  The most common mistake is not doing a `git pull` before you begin working.  In a 2 person project like this one you can all but eliminate merging issues by making sure that your code is up to date before you begin working.

