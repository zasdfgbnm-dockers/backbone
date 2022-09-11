FROM zasdfgbnmsystem/basic
USER root
COPY . /opt/zasdfgbnmsystem/backbone
RUN cd /opt/zasdfgbnmsystem/backbone/ && ./build.py
CMD /opt/zasdfgbnmsystem/backbone/run.sh