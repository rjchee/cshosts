cshosts
=======

UT CS host selector.

Contains a script to select the CS host with the lowest load and prints out its
hostname, as well as a configurable script to connect to the CS host chosen by
the previous script.

Usage of `cshosts.py`
=====================
Prints out the hostname of the 64-bit UT CS host with the lowest load. If a
favorite host is specified, choose that host if its load is less than the
threshold (default 0.3). If the host is down or its load is more than the
threshold, it chooses the host with the lowest load as it normally would.

	$ cshosts.py fav_host? threshold?

Usage of `csconnect.sh`
=======================
Connects via SSH to the UT CS host with the lowest load.

1. Configure `csconnect.sh` by opening it in a text editor and adding your UT CS username.
2. After configuring:

	$ csconnect.sh

