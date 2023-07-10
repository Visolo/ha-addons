# https://developers.home-assistant.io/docs/add-ons/configuration#add-on-dockerfile
ARG BUILD_FROM
FROM $BUILD_FROM

# Execute during the build of the image
# ARG TEMPIO_VERSION BUILD_ARCH
# RUN \
#     curl -sSLf -o /usr/bin/tempio \
#     "https://github.com/home-assistant/tempio/releases/download/${TEMPIO_VERSION}/tempio_${BUILD_ARCH}"
	
# Install requirements for add-on
RUN \
  apk add --no-cache \
#    python3 \
#    python3-dev \
#    py3-serial \
#    py3-smbus \
#    py3-pip \
#    py3-psutil \
    gcc \
    musl-dev \
    bash-completion \
  && pip install jinja2 \
#  && pip install xmltodict \
  && pip install RPi.GPIO

# Copy root filesystem
COPY rootfs /

# Compile & Install modules
RUN \
  cd /ups-pico/install/package \
  #&& python3 setup.py install \
  && pip install . \
  && cd /ups-pico/install/picofssd \
  #&& python3 setup.py install
  && pip install .


# Home Assistant CLI
ARG BUILD_ARCH
ARG CLI_VERSION
RUN curl -Lso /usr/bin/ha \
        "https://github.com/home-assistant/cli/releases/download/${CLI_VERSION}/ha_${BUILD_ARCH}" \
    && chmod a+x /usr/bin/ha \
    && /usr/bin/ha completion > /usr/share/bash-completion/completions/ha
