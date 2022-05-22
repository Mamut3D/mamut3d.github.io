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
export PS1="\[\033[32m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\] $ "

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

