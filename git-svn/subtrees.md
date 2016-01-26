# Subtrees and Git

To understand subtrees, it's helpful to understand the problem they're supposed
to solve.  A lot of projects (and indeed some companies) have a single repo into
which all of the code is dumped.  This allows teams that depend on a particular
project to get all of the updates that might be made.  This prevents a
divergence between two projects and allows teams to get necessary updates
immediately.  The problem with this setup is that it can lead to huge,
complicated repos.  While the size can be mitigated with "sparse checkouts",
this doesn't prevent a highly fluid work environment where a small change can
propogate outward very quickly.

Subtrees are an attempt to get around this single huge repo model.  They provide
separation between projects by having a process for intentionally pulling in
the changes with some other project, rather than having them happen in
real-time.  The problems, as I can see it, is two fold:

1) It opens up the possibility of divergence, where an important and necessary
change doesn't propogate to the projects that depend on it.  This can mean that
work is wasted as the direction a sub-project is taken can be missed

2) There seems to be a lot of repetitive code saved into repo's since subtrees
aren't symbolic links, but are instead actually storing code within the main
repo.

## Setting up a Subtree

## Updating code based on a subtree 

Assume that you have the following direction setup

```
.git
main_folder
subtree_folder
```

To pull the 

`git pull -s --squash subtree $SUBTREE_REPO $SUBTREE_BRANCH` (the `--squash`
option turns all of the commits in the subtree repo into a single large commit
in the git history.
