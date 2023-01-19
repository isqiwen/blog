#!/usr/bin/env bash

set -e

if [[ -f /etc/arch-release ]]; then
    yay -Sy --needed nodejs
elif [[ -f /etc/debian_version ]]; then
    sudo apt install -y nodejs
elif [[ -f /etc/redhat-release ]]; then
    sudo dnf makecache
    sudo dnf install nodejs
else
    echo "Unsupported OS"
fi

scriptsPath=$(dirname $(readlink -f $0))
rootPath="${scriptsPath}/.."

python3 -m pip install virtualenv -i https://pypi.tuna.tsinghua.edu.cn/simple

echo "Deleting the old virtual environment(${rootPath}/.pyvenv)..."
rm -rf virtualenv ${rootPath}/.pyvenv

virtualenv ${rootPath}/.pyvenv
${rootPath}/.pyvenv/bin/python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
${rootPath}/.pyvenv/bin/python -m pip install -r ${rootPath}/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

source ${rootPath}/.pyvenv/bin/activate
pc init
