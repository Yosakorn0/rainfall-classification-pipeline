# 1. Base image
FROM python:3.9-slim

# 2. Set working directory
WORKDIR /app

# 3. Install dependencies first (better caching)
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of the app
COPY . .

# 5. Expose port
EXPOSE 5000

# 6. Run the app
CMD ["python", "app.py"]