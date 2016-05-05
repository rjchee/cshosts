# Change this to your UT CS username.
username=""

# If you have a preferred machine (so you don't have to add SSH keys or
# whatnot), and you would like to ssh into it if its load is less than some
# threshold (default 0.3), change the bash variables below appropriately. Note
# you can't define threshold without a fav_host

fav_host="deaths-head-hawkmoth" # could be empty string if you don't have one
threshold="" # use the default threshold, any float is valid

ssh -X $username@`./cshosts.py $fav_host $threshold`.cs.utexas.edu
