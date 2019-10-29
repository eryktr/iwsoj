FROM gcc

ARG fpath
ARG stdinfpath

COPY $stdinfpath /runner/input.txt
COPY $fpath /runner/target.c
COPY ./run.sh /runner/run.sh
COPY ./input.txt /runner/input.txt
RUN chmod +x /runner/run.sh
CMD /runner/run.sh
