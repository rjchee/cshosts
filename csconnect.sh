# Change this to your UT CS username.
username="clay"

# Change this to 32 if you would rather connect to a 32-bit machine.
# Or set it to $1 to make the first argument the bits, e.g.:
# 	$ csconnect.sh 32
# 	$ csconnect.sh 64
bits=64

ssh -X $username@`cshosts.py $bits`
