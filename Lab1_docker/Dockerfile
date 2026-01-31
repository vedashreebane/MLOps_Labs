# Use an official Python runtime 
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the source files into the container
COPY src/ .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
CMD ["python", "main.py"]