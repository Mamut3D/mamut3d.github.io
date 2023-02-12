+++
title = "Cpu"
+++

## CPU

### CPU architecture visualisation

I wanted to find how CPU is split into NUMA nodes, and how many CPU has. Turns out, there is a cool CLI utility called `lstopo` which can export this arch as png.

```Bash
# on Debian/Ubuntu
apt install hwloc

lstopo --of png > cpu.png
```

Export from gcloud shell VM (sadly only single NUMA there as expected):

![Gcloud shell CPU visualisation](/kb/cpu/cpu.png)
