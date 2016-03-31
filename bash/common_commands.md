#Helpful Bash Commands

It's incredible how long I went without knowing the commands below.  I would
spend much of my time interacting with the shell holding down the left or right
arrow, trying to get to a particular part of the command.  A classic use case
would be me executing a command, and then re-executing it with a slight change
at the beginning.  If it was long and the scroll was slow, it would literally
take tens of seconds.  Stupid! Stupid!  When will I learn that if I am doing
something that takes more than ~2 seconds, there's definitely a hot key
available.

## Jump to the front of the command line

`ctrl a` 

## Jump to the end of the command line

`ctrl e`

## Find a command in history based on it's prefix

`ctrl r` then type the start of the command you're tyring to find.  Even more
helpful, you can do as much as you remember.  You can then use `ctrl r` to move
up in the list of matching commands.  You can also scroll down, but the keys
collide with some terminal functionality.  See the link below to get around
these problems.

## Delete *entire* word prior to the cursor

`ctrl w`

## Jump to end of bash history

Assume you hit the up arrow a lot, looking for a particular command.  By hitting
`Meta >` you can jump to the end.  "In most cases, the 'meta' key is
`alt`" meaning the command would be `alt shift .`.

## Execute History Quickly

`history X` will show the last X commands of the form

```
50  history
51  man history
52  history 10
53  history
54  history 5
```

You can then quickly run a particular command by typing `!51`.

[thanks](https://www.digitalocean.com/community/tutorials/how-to-use-bash-history-commands-and-expansions-on-a-linux-vps)
