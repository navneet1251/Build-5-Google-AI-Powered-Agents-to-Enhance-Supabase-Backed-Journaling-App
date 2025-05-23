# Use an official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy code and install dependencies
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8000

# Start FastAPI using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
