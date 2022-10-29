+++
title = "Tmux"
+++

> Note: Configuration from this KB can be applied through [this](https://github.com/Mamut3D/mamut3d.github.io/blob/main/ansible/playbooks/personal_config.yml) Ansible playbook.

## Tmux configuration

- configure Tmux to allow switching between panes using vim navigation keys.
  ```console
  $ cat ~/.tmux.conf
  bind h select-pane -L
  bind j select-pane -D
  bind k select-pane -U
  bind l select-pane -R
  ```

## Tmux tips

- hide/show status bar (useful on small screens :-))
  ```bash
  # use <CTRL+B> before inputting commands

  # hide tmux status bar for current session
  :set status off
  ```
- show time: `CTRL` + `B` then `T`
