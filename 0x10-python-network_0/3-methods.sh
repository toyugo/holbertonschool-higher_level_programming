#!/bin/bash
# check header for http methode
curl -s -I 0.0.0.0:5000/route_4 | grep "Allow" | cut -d ':' -f 2 | cut -c2-
