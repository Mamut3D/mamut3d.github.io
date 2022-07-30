---
layout: page
title:  "Personal KB"
---
## Termux


- Allow app install from unknown sources
  - Settings -> Apps -> ... -> Special access -> Install unknown apps -> Enable `your browser`
- Install Termux from (via browser for me) https://f-droid.org/en/packages/com.termux
- Install Termux-api from ( via browser for me) https://f-droid.org/en/packages/com.termux.api/
- Test packages for viruses at https://www.virustotal.com/gui/home/url
- Disable installation of apps from unknown sources
  - Settings -> Apps -> ... -> Special access -> Install unknown apps -> Disable `your browser`

```bash
# update all
pkg update -y

# Install necessary apps ;-)
pkg install -y bash-completion \
               git \
               htop \
	       tmux \
	       openssh \
	       vim \
	       termux-api \
	       python

# Gen new ssh key (if you don't have old one)
ssh-keygen -t ed2551
```

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

EOF
```

## Vim

- prepare folders for spellcheck

```bash
mkdir -p ~/.vim/spell
```

- configure vim

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
" remove trailing whitespaces on save https://vim.fandom.com/wiki/Remove_unwanted_spaces
autocmd BufWritePre * :%s/\s\+$//e
" replace selected text in visual with regexp https://stackoverflow.com/questions/676600/vim-search-and-replace-selected-text
vnoremap <C-r> "hy:%s/<C-r>h//gc<left><left><left>
" point to additional words for spellchecking
set spellfile=~/.vim/spell/en.utf-8.add
EOF
```

### Spell checking

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

## Python

TODO console autocomplete

## Termux

```bash
# Termux config, use only once or edit the cat  ;-)

cat << EOF >> ~/.termux/termux.properties
# Disable termux bell
bell-character=ignore
# Disable additional keys for termux
extra-keys = []
EOF

# Allow termux to access data on phone in ~/storage
termux-setup-storage
```

## gcloud

Termux how to install gcloud cli

```bash
# https://cloud.google.com/sdk/docs/install

# Make trash tmp in your home
mkdir ~/tmp

# Download tar ball
curl -O ~/tmp/gcloud.tar.gz https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-386.0.0-linux-arm.tar.gz

# Untar
tar xvf  ~/tmp/gcloud.tar.gz --directory ~/tmp

# Install googlecli
~/tmp/google-cloud-sdk/install.sh \
  --usage-reporting false \
  --rc-path ~/.bashrc \
  --command-completion true \
  --path-update true \
  --quiet

# Activate/authorize gcloud cli connection
gcloud auth login --activate --no-launch-browser

## Open the received link in browser and provide back verification code
#
# You are now logged in as [XYZ@gmail.com].
#
# Yay :-)

# Connect to your free google cloud shell
# Ephemeral Debian vm with 4vCPU and 16GB ram
#
# Additional stuff:
# - flags for keepalive are sent, so your VM won't die due to inactivity in around 10m
# - port 8080 from remote vm is forwared to localhost
#   (feel fre to replace by any other port you might need)
gcloud cloud-shell ssh --ssh-flag=-L8080:127.0.0.1:8080 --ssh-flag=-oServerAliveInterval=30

# Test remote session by running grafana container in google cloud shell
cloudshell:~$ docker run -it --rm -p 8080:3000 grafana/grafana

# Now try openning in your browser:
# http://localhost:8080
```

### gcloud desktop experience

Actually you can use gcloud as remote desktop. References:
- https://www.kadifeli.com/fedon/hint.php?cloud_gc_shell
- https://idroot.us/install-vnc-server-debian-11/

```bash
# connect to gcloud shell with default vnc port portforwarded to your localhost
gcloud cloud-shell ssh --ssh-flag=-L5901:127.0.0.1:5901 --ssh-flag=-oServerAliveInterval=30

# Install desktop environment packages and vnc server without interactive promt
sudo DEBIAN_FRONTEND=noninteractive apt install xfce4 xfce4-goodies vnc4server dbus-x11 -y

# Create vnc password
vncpasswd

# Create vnc server config
mkdir ~/.vnc
cat << EOF >> ~/.vnc/xstartup
#!/bin/bash
export XKL_XMODMAP_DISABLE=1
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
xsetroot -solid grey
vncconfig -iconic &
startxfce4
EOF

# Start vnc server
vncserver -localhost

# Install VNC client on your local machine and use it to connect to localhost:5901
# I have succesfully tested https://play.google.com/store/apps/details?id=com.iiordanov.freebVNC&hl=cs&gl=US  on my S10 phone

# Stop vnc server
vncserver -kill :1

```

## Hex editor

```bash
# Cool terminal hex vier xxd
xxd <filename>

# Can be used to edit hex data in vim
# https://www.kevssite.com/using-vi-as-a-hex-editor/

vim <Filename>
# vim view and edit file in hex view
:%!xxd
# revert edited file back
:%!xxd -r
```

## GitHub pages links

- [Repo prep](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll)
- [Local jekyll test](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)
  - download gems `cd docs && bundle install`
  - Test locally on termux requires fix at `vim /data/data/com.termux/files/usr/lib/ruby/gems/3.1.0/gems/jekyll-3.9.2/lib/jekyll/utils/platforms.rb` according to <https://github.com/jekyll/jekyll/issues/7045>
  - also one more fix all ready present in this repo Gemfile <https://github.com/jekyll/jekyll/issues/8523>
  - serve pages locally `bundle exec jekyll serve --host 0.0.0.0.`
