Set a global value across all your tmux sessions by using the `set-option -g` prefix.
For example, to set your tmux history limit:

1. `vim ~/.tmux.conf`
2. `set-option -g history-limit 50000`
3. Restart any/all tmux sessions

To look up all of the tmux options, just checkout the man page.
