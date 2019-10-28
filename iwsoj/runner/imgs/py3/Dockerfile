FROM python:3.7

ARG fpath

COPY $fpath /runner/target.py
COPY ./run.sh /runner/run.sh
RUN chmod +x /runner/run.sh
CMD /runner/run.sh

