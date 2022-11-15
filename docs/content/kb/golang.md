+++
title = "Golang"
+++

> Note: Configuration from this KB can be applied through [this](https://github.com/Mamut3D/mamut3d.github.io/blob/main/ansible/playbooks/personal_config.yml) Ansible playbook.

## Go vim autocomplete

Taken from [here](https://github.com/fatih/vim-go).

```conscole
$ cat ~/.vimrc
...
call plug#begin('~/.vim/plugged')

Plug 'fatih/vim-go', { 'do': ':GoUpdateBinaries' }

" Initialize plugin system
call plug#end()
```

- To invoke autocomplete menu press `<CTRL>+X` and then`CTRL+O`

## Golang tips

- run go program from vim
  ```bash
  :GoRun
  ```

- go micro service rest [example](https://go.dev/doc/tutorial/web-service-gin)
