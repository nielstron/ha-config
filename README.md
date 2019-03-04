# Tools and custom components

This repository contains tools, examples for a home assistant configuration and custom components.

Namely there is one script for generating template sensors that each
monitor a one hour forecast of the dark sky component.

Also there is a custom component that fetches data and sets
analogous outputs of the UVR1611
via the webinterface provided by a BLNET component using the library
[pyblnet](https://github.com/nielstron/pyblnet).

At last a custom component is included, that fetches data from Fronius
solar devices. The current version is a crude JSON parser but it is planned
to make use of the library [pyfronius](https://github.com/nielstron/pyfronius).

