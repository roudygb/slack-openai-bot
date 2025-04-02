FROM python:3.11

# Set working directory
WORKDIR /app

# Copy and install dependencies first (layer cache optimization)
COPY requirements.txt .

# Upgrade pip to avoid compatibility issues
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose port for Cloud Run
EXPOSE 8080

# Run the bot
CMD ["python", "bot.py"]