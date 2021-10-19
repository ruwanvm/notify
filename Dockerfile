FROM python:3.9.7-alpine3.14
RUN pip install --target=/app requests
WORKDIR /app
COPY main.py .
ENV PYTHONPATH /app
CMD ["/app/main.py"]
