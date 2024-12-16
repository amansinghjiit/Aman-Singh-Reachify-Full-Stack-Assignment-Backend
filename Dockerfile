FROM python:3.11-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN python manage.py migrate

RUN python manage.py shell <<EOF
from django.contrib.auth.models import User

username = 'admin'
email = 'admin@gmail.com'
password = 'admin'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Superuser created successfully.")
else:
    print("Superuser already exists. Skipping creation.")
EOF

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
