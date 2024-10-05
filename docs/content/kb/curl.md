+++
title = "Curl"
+++

## Curl tips and tricks

```bash
# Force resolution to different IP via curl
# Works wih SNI and l7 Hostname header based LBs

curl --resolve '<hostname>:<port>:<ip-to-resolve-to>' https://<hostname>:<port>/path
```
