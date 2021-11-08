FROM continuumio/anaconda3
COPY . /usr/app/
EXPOSE 5000:5000
WORKDIR /usr/app/
RUN pip install -r requirements.txt
CMD python flask_api_copy.py