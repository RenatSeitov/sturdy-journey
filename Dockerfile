FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN python -m venv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt
COPY . /code/
