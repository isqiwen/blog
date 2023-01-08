#!/usr/bin/env bash

set -e

if [[ -f /etc/arch-release ]]; then
    yay -Sy --needed nodejs
elif [[ -f /etc/debian_version ]]; then
    sudo apt install -y nodejs
else
    echo "Unsupported OS"
fi

scriptsPath=$(dirname $(readlink -f $0))

pip install pynecone-io
pip install -r ${scriptsPath}/../requirements.txt
pc init
