# Use an official Python runtime as a base image
FROM python:3.9-alpine
### install python dependencies if you have some
# RUN pip3 install pyfiglet

### We make sure that we have authorizations to write on /tmp
RUN chmod 777 -R /tmp && chmod o+t -R /tmp 

# Copy the current directory contents into the container
COPY ./src /app

#tun the app
ENTRYPOINT ["python3", "/app/app.py"]




# # Set the working directory in the container
# WORKDIR /app

# COPY . /app
