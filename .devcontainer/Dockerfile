FROM python:3.7.11-buster

RUN apt update
RUN apt install -y --no-install-recommends \
    apt-utils gcc build-essential libgl1-mesa-glx
RUN pip install --no-cache-dir autopep8 flake8
RUN apt autoremove -y
RUN apt clean -y
RUN rm -rf /var/lib/apt/lists/*