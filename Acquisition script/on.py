#!/usr/bin/env python

import pifacedigitalio
pfd = pifacedigitalio.PiFaceDigital()

pfd.relays[0].value = 1
# turn on/set high the first relay
# pfd.relays[0].value = 0

