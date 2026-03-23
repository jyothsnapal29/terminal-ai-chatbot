FROM python:3.11-slim

#Setting the working directory
WORKDIR /app

#Copy requirements.tsx
COPY requirements.txt .

#Install python libraries
RUN pip install --no-cache-dir -r requirements.txt

#Copy the rest of the project
COPY . .

#Expose port
EXPOSE 8000

#Run main script
CMD ["python", "src/main.py"]

