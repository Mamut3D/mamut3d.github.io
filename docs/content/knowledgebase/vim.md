+++
title = "Vim"
+++

Tips and tricks for Vim configuration and life with vim.

> Note: Configuration from this KB can be applied through [this](https://github.com/Mamut3D/mamut3d.github.io/blob/main/ansible/playbooks/personal_config.yml) Ansible playbook.

## Config

- prepare folders for spellcheck

```bash
mkdir -p ~/.vim/spell
```

- configure vim

```bash
cat ~/.vimrc
" Disable mouse select
set mouse-=a
" Copy paste maybe TODO in termux https://ibnishak.github.io/blog/post/copy-to-termux-clip/

" General good stuff from https://danielmiessler.com/study/vim/
" highlight syntax
syntax on
" disable the swapfile
set noswapfile
" highlight all results
set hlsearch
" ignore case in search
set ignorecase
" show search results as you type
set incsearch
" set jk as ESC alternative
inoremap jk <ESC>
" remove trailing whitespaces on save https://vim.fandom.com/wiki/Remove_unwanted_spaces
autocmd BufWritePre * :%s/\s\+$//e
" replace selected text in visual with regexp https://stackoverflow.com/questions/676600/vim-search-and-replace-selected-text
vnoremap <C-r> "hy:%s/<C-r>h//gc<left><left><left>
" point to additional words for spellchecking
set spellfile=~/.vim/spell/en.utf-8.add

" enable vim-plugin
call plug#begin('~/.vim/plugged')

Plug 'mzlogin/vim-markdown-toc'

" Initialize plugin system
call plug#end()

" enable spell check for markdown files
autocmd FileType markdown setlocal spell

" Disable netrw help header
let g:netrw_banner=0
```

## Spell checking

- Spellcheck tips were taken from [here](https://linuxhint.com/vim_spell_check/)

```console
# Enable spell checking in vim
:set spell

# Disable spell checking in vim
:set nospell

# Move to next misspelled word
]s

# Move to previous misspelled word
[s

# Add word to local spell file (when hovering over misspelled word)
zg

# Select word from dictionary (when hovering over misspelled word)
z=
```

## TOC plugin for MD files

First of all we need some plugin manager. Let's start with [vim-plug](https://github.com/junegunn/vim-plug).

```bash
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

Restart vim and install [vim-markdown-toc](https://github.com/mzlogin/vim-markdown-toc) plugin.
The following section should be already in `~/.vimrc` from the section above.

```console
# Start vim and install plugins defined in ~/.vimrc

$ vim
:PlugInstall

# Open some md file in vim and generate TOC
:GenTocGFM
```

## Random tips

- Disable word highlight after searching in vim via `/regexp`

```console
:noh
```

## Netrw

Key shortcuts to use netrw - vim's directory browser.

- `d` - create directory
- `D` - delete current file
- `%` - create new file
