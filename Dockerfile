FROM python:3.9-slim
LABEL authors="chaegiung"
WORKDIR /app
ADD . .
# COPY ./requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000
EXPOSE 5432
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD [ "python", "manage.py", "runserver" ]
#ENTRYPOINT ["npm", "start"]