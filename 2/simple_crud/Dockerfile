FROM python
WORKDIR /project/
COPY . ./simple_crud
RUN pip install -r requirements.txt
CMD gunicorn simple_crud.wsgi -b 0.0.0.0:8000