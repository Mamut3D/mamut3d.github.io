+++
title = "Filesystem"
+++

## Find what takes space

```bash
# What arw largest files in path
du -ahx /dir | sort -rh | head -n 20

# Find log file larger than 10G
find /dir -name "*.log" -size +10G
```
