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

" Set line moves with Ctrl +hjkl
nnoremap <C-j> :m .+1<CR>
nnoremap <C-k> :m .-2<CR>
inoremap <C-j> <Esc>:m .+1<CR>gi
inoremap <C-k> <Esc>:m .-2<CR>gi
vnoremap <C-j> :m '>+1<CR>gv
vnoremap <C-k> :m '<-2<CR>gv

:set shiftwidth=1
nnoremap <C-h> :<1<CR>
nnoremap <C-l> :>1<CR>
inoremap <C-h> <Esc>:<1<CR>gi
inoremap <C-l> <Esc>:>1<CR>gi
vnoremap <C-h> < gv
vnoremap <C-l> > gv

" improve autocomplete behavior based on https://vim.fandom.com/wiki/Make_Vim_completion_popup_menu_work_just_like_in_an_IDE

" enable vim-plugin
call plug#begin('~/.vim/plugged')

Plug 'mzlogin/vim-markdown-toc'
Plug 'davidhalter/jedi-vim'

" Initialize plugin system
call plug#end()

" enable spell check for markdown files
autocmd FileType markdown setlocal spell

" Disable netrw help header
let g:netrw_banner=0

""" Python stuff start

" jedi-vim config
" disable automatic autodot extension, use <CTRL>+<Space>
let jedi#popup_on_dot=0

" configure function call signature
let g:jedi#show_call_signatures=1

" use tabs for showing Pydoc
let g:jedi#use_tabs_not_buffers = 1

" autogenerate import for python files on save
autocmd bufwritepost *.py execute  "silent !tidy-imports --quiet --replace-star-imports --action REPLACE " . bufname("%")
""" Python stuff end
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

# Remove word to local spell file (when hovering over word)
zug

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

## Autocomplete

- `<CTRL>+p` - show autocomplete options
  - `<CTRL>+p` - cycle back in autocomplete options
  - `<CTR>+n` - cycle forward in autocomplete options
  - `<CTR>+y` - select from autocomplete options

## Python autocomplete

So far I am testing [jedi-vim](https://github.com/davidhalter/jedi-vim) plugin. I found another blog post how to do this in Termux [here](https://hax4us.github.io/2020-07-12-install-jedi-vim-termux/).

```console
# Install Termux package to add python3 support for vim
pkg install vim-python

# Download required git repo
$ git clone --recursive https://github.com/davidhalter/jedi-vim.git ~/.vim/bundle/jedi-vim

# Ensure us use Plug for vim plugins and have jedi-vim defined in ~/.vimrc
$ cat ~/.vimrca
...
Plug 'davidhalter/jedi-vim'
...

# Start vim and install plugins defined in ~/.vimrc
$ vim
:PlugInstall
```
### Jedi-vim shortcuts

Keyboard shortcuts:

> <leader> key in vim is `\` by default

- `<C-Space>` - Autocomplete
- `<leader>d` - Goto definition
- `K` - Show Documentation/Pydoc
- `<leader>r` - rename

## Random tips

- Disable word highlight after searching in vim via `/regexp`

```console
:noh
```

- Open URL links in browser

```console
# Hower over url and press
gx
```

## Netrw

Key shortcuts to use netrw - vim's directory browser.

- `d` - create directory
- `D` - delete current file
- `%` - create new file
- `R` - rename current file

## Insert mode tips

- exit insert mode: `CTRL` + `[`
## Where to go next

- [Insert mode tips](https://dev.to/iggredible/the-only-vim-insert-mode-cheatsheet-you-ever-needed-nk9)
