FROM zasdfgbnmsystem/basic
USER root
RUN pacman -Sy --noconfirm radvd
COPY . /opt/zasdfgbnmsystem/backbone
RUN cd /opt/zasdfgbnmsystem/backbone/ && ./build.py
CMD /opt/zasdfgbnmsystem/backbone/run.sh