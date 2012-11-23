cshosts
=======

UT CS host selector.

Contains a script to select the CS host with the lowest load and prints out its hostname, as well as a configurable script to connect to the CS host chosen by the previous script.

Usage of `cshosts.py`
=====================

	$ cshosts.py (32|64)

Prints out the hostname of the (32- or 64-bit, respectively) UT CS host with the lowest load.

Configuration of `csconnect.sh`
===============================

In `csconnect.sh`, replace `[AAAA]` with your UT CS username, and `[BBBB]` with your preference of 32-bit or 64-bit machines.

Usage of `csconnect.sh`
=======================

After configuring:

	$ csconnect.sh

Connects via SSH to the UT CS host with the lowest load.
