Advanced LIGO CDS Python EPICS interface
========

Ezca is a wrapping around pyepics containing methods specially
designed for interfacing with the Advanced LIGO CDS front-end control
system (e.g. "RCG").  Beyond providing standard methods for reading
and writing EPICS channels, it also includes the LIGOFilter object for
interacting with CDS Standard Filter Modules.  It also handles
abstracting information about the interferometer under control, and
sub-classing specific control domains.

It is specifically designed to be integrated into the Guardian
automation platform, but it's also perfectly usable on it's own.
