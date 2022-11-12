+++
title = "Termux"
+++

## Installation and configuration

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
	       python \
	       exiftool

# Gen new ssh key (if you don't have old one)
ssh-keygen -t ed2551
```

## Tips

- Copy/open url links from Termux

  ```console
  CTRL+shift+m
  > Select URL
  > enter(short press copy / long open in browser)
  ```
