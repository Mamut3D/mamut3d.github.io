+++
title = "Gcloud"
+++

## CLI installation and configuration

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

### Minikube using ansible

Aim of this, is to create reusable k8s minikube cluster with ingress and argocd on gcloud from scratch as simple as possible

```bash
# Optionally start ssh agent to carry your locall ssh keys with you to gloud shell for github access
eval `ssh-agent` && ssh-add

# connect to gcloud shell vm + port forward 8080 to localhost just in case ;-)
cloud cloud-shell ssh --ssh-flag=-L8080:127.0.0.1:8080 --ssh-flag=-oServerAliveInterval=30 --ssh-flag=-A

# install ansible
pip3 install ansible

# download my github minikube-lab repo
git clone git@github.com:Mamut3D/minikube-lab.git

# apply playbooks on localhost
ansible-playbook playbooks/prep.yml && ansible-playbook playbooks/setup.yml
```
