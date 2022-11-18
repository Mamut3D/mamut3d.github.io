+++
title = "RSS"
+++

> Note: Configuration from this KB can be applied through [this](https://github.com/Mamut3D/mamut3d.github.io/blob/main/ansible/playbooks/personal_config.yml) Ansible playbook.

## Newsboat

[Newsboat](https://newsboat.org) is a cli RSS reader usable also with Termux. There is only one thing that sucks on small screens, and that is that Newsboat does not wrap article tittle names.

TLDR here is the config:

```conscole
$ cat .newsboat/config
# Quality of life stuff
refresh-on-startup yes
show-read-feeds no
show-read-articles no

# Open browser articles in browser called from termux
browser "termux-open-url %u"

# unbind keys
unbind-key j
unbind-key k
unbind-key J
unbind-key K

# bind keys - vim style
bind-key j down
bind-key k up
bind-key l open
bind-key h quit
bind-key H prev-feed
bind-key L next-feed

# bind keys - show read feeds with keybind
bind-key r toggle-show-read-feeds

# List article name only due to screen size
articlelist-format "%t"
```
