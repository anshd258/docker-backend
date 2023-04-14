FROM python:3.8
ENV PYTHONUNBUFFERED 1
# Create app directory
WORKDIR /app

# Create Python virtualenv and use it
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt ./

RUN pip install -r requirements.txt --no-cache-dir

COPY . /app
