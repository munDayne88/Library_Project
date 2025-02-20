# Base image:
FROM python:3.12.3
# Setting the working directory within the container
WORKDIR /app
# Get the files from local repo into container image
COPY docker_app /app/
RUN pip install --no-cache-dir -r requirements.txt
# Running the application
ENTRYPOINT ["python", "Lib_Transform_App.py"]