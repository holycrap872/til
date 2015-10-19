# Can you do sparse checkouts in git-svn?

Sparse checkouts are a way that SVN uses to get around the fact that
the repo's it creates are so big.  Essetnially, you can choose a specific
part of the repo that you want to download and ignore the rest.  Git
has these same features.  This document examines how sparse checkouts
work with git, and whether they can be extended to git-svn.

To answer this question I did a series of quick experiments.  

## Can you do a sparse clone of a git repo without fetching the entire thing?

First, there's the control... a blank git repo that is then initialized
to be a clone of a sample repo.  I did this using the following commands

1. `mkdir test && cd test`.  Pretty simple.

2. `git init`.  I want to see if a sparse clone is possible, which
means eventually attempting to sparsely clone a repo.  The only way
that I have found to do this is through creating an empty repo and
pulling information into it.  Therefore, in order to be consistent,
I'll do a similar thing for the control.

3. `git remote add origin https://github.com/holycrap872/til.git`. Again,
pretty simple.

4. `git fetch origin`.  This fetches all of the history of the `til` repo.

5. `git checkout -b testBranch origin/master`.  This sets up a branch called
"testBranch" which tracks the origin/master branch.  By doing this, I get
all of the history of the til repo since there's only one branch.

After all of this, checking the size of the repo I get 22 items totalling
102 kbs.

Next, there's the experimental(??? I don't remember the verbiage).

1. `mkdir test2 && cd test2`

2. `git init`

3. `git remote add origin https://github.com/holycrap872/til.git`

4. `git config core.sparsecheckout true`

5. `echo git-svn/ >> .git/info/sparse-checkout`.  Fun fact, running `git log`
at this point produces `fatal: bad default revision 'HEAD'`.  This is because
there is no branch infomation pulled yet.

6. `git fetch origin`

7. `git checkout -b testBranch origin/master`.  This yields only the git-svn
folder in the til/ repo.  When I view the size of the folder, it is merely 6.5
kb with 2 items.  Finally, when viewing the log, every commit message since
the start of the repo is present, whether it has to do with git-svn/ or not.

The real proof, however, is in the pudding.  When checking the size of the
of the .git folder using `du -c`, I got 760 for the sparse folder whereas
I got 892 for the non-sparse checkout.

## Can git-svn do a sparse checkout?
