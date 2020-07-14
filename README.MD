# Bird Filters
Created a python script that updates the prefixes (of upstream/downstream customers) and stores it in a file. 

# Crontab

`0 */4 * * * /root/configs/bird_filters/run.sh /root/configs/bird_filters > /tmp/log  2>&1`