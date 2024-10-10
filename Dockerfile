FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE estagios.settings

ARG EMAIL_HOST_PASSWORD_ARG
ENV EMAIL_HOST_PASSWORD $EMAIL_HOST_PASSWORD_ARG

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /code/