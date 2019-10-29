FROM openjdk

ARG fpath
ARG stdinfpath

COPY $stdinfpath /runner/input.txt
COPY $fpath /runner/target.java
COPY ./run.sh /runner/run.sh
RUN chmod +x /runner/run.sh
CMD /runner/run.sh