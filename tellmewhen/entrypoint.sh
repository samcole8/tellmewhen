#!/bin/sh
set -e

# Start crond in the foreground
crond -f &

# Keep the script running
tail -f /dev/null