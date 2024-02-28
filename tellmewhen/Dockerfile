FROM alpine:latest
WORKDIR /root/

# Install dependencies
RUN apk update && \
    apk add --no-cache python3 dcron py3-toml py3-requests py3-twilio

# Copy Python scripts
COPY python/* ./
# Assemble cron jobs
RUN python3 when.py

COPY entrypoint.sh ./
ENTRYPOINT ["./entrypoint.sh"]
