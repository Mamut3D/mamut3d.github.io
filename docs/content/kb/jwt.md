+++
title = "JWT"
+++

## JWT tricks

```bash
# View JWT token claims bash single line cmd
cat /run/secrets/tokens/jwt | cut -d "." -f 2 | base64 -d 2> /dev/null || echo
```

JWT simple copy paste trick

```bash
 | cut -d "." -f 2 | base64 -d 2> /dev/null || echo
```

JWT prettify copy paste trick

```bash
 | cut -d "." -f 2 | base64 -d 2> /dev/null | sed 's/,/,\n/g'
```
