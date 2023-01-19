#!/usr/bin/env bash

scriptsPath=$(dirname $(readlink -f $0))
rootPath="${scriptsPath}/.."

source ${rootPath}/.pyvenv/bin/activate
pc run
