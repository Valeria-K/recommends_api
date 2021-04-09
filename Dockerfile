FROM python:3
COPY . /
WORKDIR /
RUN pip3 install -r requirements.txt
CMD ["python", "./app.py"]