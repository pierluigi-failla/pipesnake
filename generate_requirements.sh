#!/usr/bin/env bash

pipreqs --force --savepath=requirements.txt pipesnake
pipreqs --force --savepath=requirements-dev.txt ../pipesnake
echo "pipreqs==0.4.9" >> requirements-dev.txt
echo "sphinx==1.6.5" >> requirements-dev.txt
echo "nose==1.3.7" >> requirements-dev.txt
