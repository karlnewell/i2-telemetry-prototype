FROM telegraf

RUN export DEBIAN_FRONTEND=noninteractive && \
    sed -i 's/main$/main contrib non-free/g' /etc/apt/sources.list && \
    set -x && \
    apt-get update && \
    apt-get -y install snmp-mibs-downloader && \
    rm -r /var/lib/apt/lists/*