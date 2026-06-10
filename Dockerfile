# 1. Use an official, lightweight Python runtime
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the dependencies file
COPY requirements.txt .

# 4. Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your API script code into the container
COPY main.py .

# 6. Expose the port that FastAPI runs on
EXPOSE 8000

# 7. Command to run the server inside the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]