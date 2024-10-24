#! /bin/bash

if [ "{{cookiecutter.create_application}}" == "False" ]; then
    echo "Removing application folder (create_application == False)."
    rm -rf ./{{cookiecutter.slug}}
fi


if [ "{{cookiecutter.create_config}}" == "False" ]; then
    echo "Removing config file (create_config == False)."
    rm -f ./config.yml
fi