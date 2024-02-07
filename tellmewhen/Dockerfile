FROM alpine:latest

# Install dependencies
RUN apk update && \
    apk add --no-cache python3 dcron

# Copy Python scripts
COPY python/* /root/
# Assemble cron jobs
RUN /root/when.py

CMD ["crond", "-f"]