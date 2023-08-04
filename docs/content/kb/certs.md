+++
title = "Certs"
+++

## View and manipulate cert tricks

```bash
#  view remote certs used for tls on remote server
echo | openssl s_client -showcerts -servername localhost -connect localhost:8443 2>/dev/null | openssl x509 -inform pem -noout -text

# Get CA PEM file simple human readable cert info per certificate
keytool -printcert -file /tmp/ca.crt | grep -A 6 'Certificate\['
```
