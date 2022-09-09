+++
title = "Bash"
+++

## Bashrc

Random bashrc stuff, review bashrc before using since it overrides everything

``` bash
cat << EOF > ~/.bashrc
# Show git branch on PS1
# Origin: https://coderwall.com/p/fasnya/add-git-branch-name-to-bash-prompt
parse_git_branch() {
  git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
export PS1="\[\033[32m\]\w\[\033[33m\]/\$(parse_git_branch)\[\033[00m\] $ "

## Eternal bash history.
# ---------------------
# Undocumented feature which sets the size to "unlimited".
# http://stackoverflow.com/questions/9457233/unlimited-bash-history
export HISTFILESIZE=
export HISTSIZE=
export HISTTIMEFORMAT="[%F %T] "
# Change the file location because certain bash sessions truncate .bash_history file upon close.
# http://superuser.com/questions/575479/bash-history-truncated-to-500-lines-on-each-login
export HISTFILE=~/.bash_eternal_history
# Force prompt to write history after every command.
# http://superuser.com/questions/20900/bash-history-loss
PROMPT_COMMAND="history -a; $PROMPT_COMMAND"

# set default editor in bash to vim
EDITOR=vim

EOF
```

## Edit command in editor

How to edit current command in text editor (based on $EDITOR env variable)

```console
$ random command

# Press CTRL+x CTRL+e
# to open the command in text editor
```
