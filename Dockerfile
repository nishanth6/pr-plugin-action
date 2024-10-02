FROM python:3.9-slim

# Set up work directory
WORKDIR /app

# Copy Python script and requirements
COPY pr_plugin.py .
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Entry point for the action
ENTRYPOINT ["python", "/app/pr_plugin.py"]
