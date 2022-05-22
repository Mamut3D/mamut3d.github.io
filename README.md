# Personal KB

## Termux


- Allow app install from unknown sources
  - Settings -> Apps -> ... -> Special access -> Install unknown apps -> Enable `your browser`
- Install Termux from (dl via browser for me) https://f-droid.org/en/packages/com.termux
- Install Termux-api from (dl via browser for me) https://f-droid.org/en/packages/com.termux.api/
- Test packages for viruses at https://www.virustotal.com/gui/home/url
- Disable installation of apps from unknown sources
  - Settings -> Apps -> ... -> Special access -> Install unknown apps -> Disable `your browser`

```bash
# update all
pkg update -y

# Install necessary apps ;-)
pkg install bash-completion git htop tmux openssh vim termux-api -y

# Gen new ssh key (if you don't have old one)
ssh-keygen -t ed2551
```

## Git branch in PS1

``` bash
# Add git branch parsing to PS1, use only once ;-)
# Origin: https://coderwall.com/p/fasnya/add-git-branch-name-to-bash-prompt

cat << EOF >> ~/.bashrc
# Show git branch on PS1
parse_git_branch() {
  git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
export PS1="\[\033[32m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\] $ "
EOF
```

## Vim

```bash
cat << EOF > ~/.vimrc
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
EOF
```

## Python

TODO console autocomplete

## Termux

```bash
# Disable termux bell, use only once ;-)
cat << EOF >> ~/.termux/termux.properties
bell-character=ignore
EOF
```
