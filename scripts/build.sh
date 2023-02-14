#!/usr/bin/env bash

set -e

if [[ -f /etc/arch-release ]]; then
    yay -Sy --needed nodejs
elif [[ -f /etc/debian_version ]]; then
    sudo apt install -y nodejs
    sudo apt-get install libpq-dev python3-dev
elif [[ -f /etc/redhat-release ]]; then
    sudo dnf makecache
    sudo dnf module install nodejs:12
    sudo yum install libpq-devel python3-devel
else
    echo "Unsupported OS"
fi

scriptsPath=$(dirname $(readlink -f $0))
rootPath="${scriptsPath}/.."

python3 -m pip install virtualenv -i https://pypi.tuna.tsinghua.edu.cn/simple

if [ -d "${rootPath}/.pyvenv" ]; then
    echo "Deleting the old virtual environment(${rootPath}/.pyvenv)..."
    rm -rf virtualenv ${rootPath}/.pyvenv
fi

virtualenv ${rootPath}/.pyvenv --python=python3.10
${rootPath}/.pyvenv/bin/python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
${rootPath}/.pyvenv/bin/python -m pip install -r ${rootPath}/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --no-warn-script-location

source ${rootPath}/.pyvenv/bin/activate
pc init
