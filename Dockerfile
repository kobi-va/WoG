FROM moditamam/selenium:python3
RUN pip install flask

WORKDIR /app

COPY *.py /app/
COPY /tests/e2e.py /app/
COPY score.txt /app/
COPY score.html /app/
COPY error.html /app/

EXPOSE 5001

CMD python3 MainScores.py
