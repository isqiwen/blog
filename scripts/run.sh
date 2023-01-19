#!/usr/bin/env bash

scriptsPath=$(dirname $(readlink -f $0))
rootPath="${scriptsPath}/.."

source ${rootPath}/.pyvenv/bin/activate

runProduction=0

while getopts "p" arg
do
    case $arg in
        p)
            runProduction=1
            ;;
        ?)
            echo "unknown argument"
            exit 1
            ;;
    esac
done

if [[ $runProduction -eq 1 ]]; then
    pc run --env prod
else
    pc run
fi
