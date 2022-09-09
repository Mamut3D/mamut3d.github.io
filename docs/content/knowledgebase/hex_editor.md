+++
title = "Hex editor"
+++

## xxd usage

```bash
# Cool terminal hex editor xxd
xxd <filename>

# Can be used to edit hex data in vim
# https://www.kevssite.com/using-vi-as-a-hex-editor/

vim <Filename>
# vim view and edit file in hex view
:%!xxd
# revert edited file back
:%!xxd -r
```
