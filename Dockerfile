from python:3.8-slim
RUN apt-get update && \
    apt-get install --no-install-recommends -y git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip3 install --user matplotlib numpy discord.py
RUN git clone https://github.com/threexc/SquireBot.git
WORKDIR /SquireBot
CMD ["python3", "Squire.py"]
