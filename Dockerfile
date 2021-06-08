#Download Python from DockerHub and use it
FROM python:3.9.2

#Set the working directory in the Docker container
WORKDIR /app

COPY requirements.txt .

#Copy the Flask app code to the working directory
COPY . /app

#Install the dependencies
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

#Run the container
CMD [ "main.py" ]
