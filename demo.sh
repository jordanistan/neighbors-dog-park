#!/bin/bash

sleep 5
echo
echo
echo
echo "Welcome to the Membership Renewal List Demo"
echo
echo
ls -l

echo
echo
sleep 3
echo "Find and run the members_renewal_list.py script by running the following:"
echo "python members_renewal_list.py"
sleep 3

python3 members_renewal_list.py

sleep 2

echo
echo
echo "Now let's check the results in the renewal_list.csv file."
sleep 2
echo
echo
echo "Here are the results of the members:"
echo
cat renewal_list.csv
echo
echo
echo
echo
echo
echo
echo
echo
