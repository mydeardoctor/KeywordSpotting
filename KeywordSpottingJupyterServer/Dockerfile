# syntax=docker/dockerfile:1

# These arguments can be redefined
# when calling "docker build" command with "--build-arg" options.
ARG TENSORFLOW_VERSION=2.17.0
ARG TENSORFLOW_DATASETS_VERSION=4.9.6

# Base image that has python, pip, tensorflow with GPU support
# and jupyter notebook server preinsalled.
FROM tensorflow/tensorflow:${TENSORFLOW_VERSION}-gpu-jupyter

WORKDIR /app
RUN mkdir /app/downloads
RUN mkdir /app/build

# Install tools and packages needed to train Keyword Spotting model.
RUN apt-get update && \
apt-get -y install ffmpeg && \
apt-get clean

RUN pip install \
pydub \
seaborn

ARG TENSORFLOW_DATASETS_VERSION
RUN pip install tensorflow-datasets==${TENSORFLOW_DATASETS_VERSION}

EXPOSE 8888

# Start jupyter notebook server.
ENTRYPOINT ["jupyter", "notebook"]
CMD ["--allow-root", "--ip=0.0.0.0", "--no-browser", "--port=8888"]