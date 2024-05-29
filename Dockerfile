FROM python:3.7
WORKDIR /code

RUN python3 -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt
EXPOSE 8000
COPY . .
CMD [ "python", "app.py" ]