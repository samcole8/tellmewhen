FROM alpine:3.19.0

# Set working directory
WORKDIR /root/

# Install dependencies
RUN apk update && \
    apk add --no-cache python3 dcron py3-pip py3-virtualenv

# Copy Python scripts
COPY python/* ./

# Create virtualenv
RUN python3 -m venv env && \
    source env/bin/activate && \
    pip3 install toml requests twilio && \
    # Assemble cron jobs
    python3 when.py


# Install and run entrypoint
COPY entrypoint.sh ./
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
