#!/bin/bash
# Check internet in a loop
while true; do
    if ping -c 1 8.8.8.8 &> /dev/null; then
        # Internet is available, schedule cron job (every minute)
        crontab -l 2>/dev/null | grep -q 'run_project.sh'
        if [ $? -ne 0 ]; then
            (crontab -l 2>/dev/null | grep -v 'run_project.sh'; echo "* * * * * /home/mubashar4603/PycharmProjects/monitoring-bot/run_project.sh") | crontab -
        fi
        break
    fi
    sleep 10
done

