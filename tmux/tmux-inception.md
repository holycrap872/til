#Tmux Inception

I accidently got stuck in a tmux session inside a tmux session.  Everytime I
tried to do anything with the interior tmux screen, the outer one would respond
instead.

In order to fix, this, simply change the tmux command (`ctrl+b`) to a different
key sequence (ex. `ctrl+a`).  At this point, do what you want to do and, when
you're done, change the outer one back to the original tmux command.

To change to a particular key set do:

```
tmux command key (ex. ctrl+b)
:set -g prefix C-a
```

With this, the tmux command will be set to `crtl+b`.

[thanks](https://ricochen.wordpress.com/2011/06/08/how-to-get-out-from-tmux-session-inside-a-tmux-window/)
