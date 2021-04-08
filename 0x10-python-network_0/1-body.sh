#!/bin/bash
# Get the byte size
if [ "$(curl -sL -w "%{http_code}" -I "$1" -o /bin/null)" -eq 200 ]; then curl -sL "$1" ; fi
