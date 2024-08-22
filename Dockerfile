# Use an official Python runtime as the base image
FROM python:3.12.4

# Set the working directory in the container
WORKDIR /app

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Copy the website files into the container
COPY --chown=appuser:appgroup ./ ./pacman

# Copy the Python script into the container
COPY --chown=appuser:appgroup main.py .

# Switch to the non-root user
USER appuser

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
CMD curl --fail http://localhost:8080/health || exit 1

# Expose the port the server will run on
EXPOSE 8080

# Run the Python script when the container starts
CMD ["python", "main.py"]
