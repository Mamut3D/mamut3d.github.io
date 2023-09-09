+++
title = "netcat tar file transfer"
+++

## netcat tar file transfer

Sometime you want to:
- send unencrypted files over network fast
- rsync transfer speed and checksums slow you down and you like to live dangerously

> based on [1](https://www.google.com/amp/s/karnsonline.com/netcat-tar-pipe/amp/), [2](https://thejoe.it/en/2018/12/03/trasferire-file-di-grandi-dimensioni-velocemente-sulla-rete-con-netcat/)

```bash
# requirements
# tar - probably everywhere in linux world
# netcat/nc - utility for read and write of data over a network
# pv - monitor of data send through pipeline (technically unnecessary)

# on the receiver
nc -l -p 6666 | pv | tar -xpf - ./

# on the sender
tar -cf - ./<filename or *> | pv | nc <receiver_hostname/ip> 6666
```
