# Step 1: Use official FastAPI & Uvicorn image as base
FROM python:3.9-slim

# Step 2: Set work directory
WORKDIR /app

# Step 3: Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy the project files into the Docker container
COPY . /app

# Step 5: Expose the application port
EXPOSE 8000

# Step 6: Command to run the app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
