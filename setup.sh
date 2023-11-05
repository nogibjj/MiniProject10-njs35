#!/usr/bin/env bash
source /home/vscode/venv/bin/activate
#append it to bash so every shell launches with it 
echo 'source /home/vscode/venv/bin/activate' >> ~/.bashrc
# Set JAVA_HOME
echo 'export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64' >> ~/.bashrc
source ~/.bashrc