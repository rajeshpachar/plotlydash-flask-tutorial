FROM python:3.8.0-slim as builder
RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean
COPY requirements.txt /app/requirements.txt
WORKDIR app
RUN pip install --user -r requirements.txt
COPY . /app
# Here is the production image
FROM python:3.8.0-slim as app
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app/ /app/

WORKDIR app
ENV PATH=/root/.local/bin:$PATH
RUN pip install gunicorn[gevent]

EXPOSE 5000
CMD gunicorn --worker-class gevent --workers 5 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info