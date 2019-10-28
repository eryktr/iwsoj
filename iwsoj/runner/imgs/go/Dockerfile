FROM golang

ARG fpath

COPY $fpath /runner/target.go
COPY ./run.sh /runner/run.sh
RUN chmod +x /runner/run.sh
CMD /runner/run.sh
