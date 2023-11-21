#Author : Dinesh Kumar(M22AIE227)
#take python image
FROM python:3.9.17
#set ork dir
WORKDIR /news_summarizer
# copy code folder
COPY . /news_summarizer/
#install dependancy
RUN pip3 install --no-cache-dir -r /news_summarizer/requirements.txt
ENV FLASK_APP=app
#command to run flask app
CMD ["python", "app.py"]