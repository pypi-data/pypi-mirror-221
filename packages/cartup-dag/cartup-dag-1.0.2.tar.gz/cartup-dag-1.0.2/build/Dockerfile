FROM python:3.8-slim-buster

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
RUN pip install -U pip setuptools wheel &&\
    pip install -U spacy &&\
    python -m spacy download en_core_web_sm &&\ 
    python -m spacy download nl_core_news_sm

COPY build/requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY ./ /app

CMD ["gunicorn", "--bind", "0.0.0.0:5000","--timeout", "600", "webservice_handlers:app"]