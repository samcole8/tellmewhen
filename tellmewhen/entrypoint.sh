#!/bin/sh
set -e

# Start cron in the foreground
crond -f &

# Keep the script running
tail -f /dev/null