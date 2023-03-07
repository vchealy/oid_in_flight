FROM python:latest
LABEL Maintainer="vincent.healy"
ARG RUN_IN_PLACE=1
# This line if not included logs an error every few seconds
ENV TERM=xterm

WORKDIR /home
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN mkdir /home/report
RUN mkdir /home/data
COPY . .

# This is the command that runs when a container is initiated
CMD [ "python","./watchdog.py", "run"] 
