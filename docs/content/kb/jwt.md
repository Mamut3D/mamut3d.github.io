+++
title = "JWT"
+++

## JWT tricks

```bash
# View JWT token claims bash single line cmd
cat /run/secrets/tokens/jwt | cut -d "." -f 2 | base64 -d 2> /dev/null || echo
```
