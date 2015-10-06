# Clone from an SVN Repository

SVN is not designed with nearly the same capacity for branching as git.
The traditional SVN repo contains three top level folders ... 

```
branches
tags
trunk
```

The basic structure contains a .svn folder in each of the directories
(recursively) in the repository.  This contains information that allows
SVN to store the complete history of the project (Not to get too technical
but it uses "additive data structures" to reconstruct each particular
commit).  Git on the other hand uses a series of diffs and pointers to
reconstruct the history.

What makes SVN branching so difficult is that there is a clear concept
of a "trunk".  This doesn't really exist in git, branches are just
given the name master by convention.  The branches of SVN are stored
in the top level branches folder.  Each branch contains a complete
copy of all of the files that were in the trunk at the time the branch
was created.

To merge these two very different ways of storing information, we can
use git svn.  Git svn allows local branching and treats the SVN branches
and trunk stored in the SVN repo as separate remote repositories.

In order to get these "remotes" onto your computer so that you can
then do your local branching

1) Clone the SVN Repo: `git svn clone {'svn+ssh' | 'http'}://url/project`
Assuming the svn repo is following the standard layout.

2) Copy over the ignore information: `git svn show-ignore >> 
.git/info/exclude`

3) View all of the available remotes: `git branch -r`

4) Checkout a branch that is associated with an SVN branch: `git 
checkout -b name-svn remotes/name`
