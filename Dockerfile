FROM python:3.6-slim

COPY . /TheMovieDBAPI
WORKDIR /TheMovieDBAPI
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null