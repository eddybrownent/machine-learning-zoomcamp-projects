FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip install pipenv

RUN pip install Flask

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["dv.bin", "/"]

COPY ["model1.bin", "/model1.bin"]

COPY ["quiz_6.py", "./"]

EXPOSE 9616

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9616", "quiz_6:app"]