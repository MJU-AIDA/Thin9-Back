FROM python:3.9-slim
LABEL authors="chaegiung"
WORKDIR /app
ADD . .
# COPY ./requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000
EXPOSE 5432
EXPOSE 8001
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
#ENTRYPOINT ["npm", "start"]