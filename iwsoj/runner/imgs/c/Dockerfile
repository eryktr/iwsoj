FROM gcc

ARG fpath

RUN echo fpath is $fpath
COPY ./$fpath /runner/target.c
COPY ./run.sh /runner/run.sh
RUN chmod +x /runner/run.sh
CMD /runner/run.sh
