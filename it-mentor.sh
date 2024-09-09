#!/bin/bash

cd /d/it-mentor
git add .
read -p "Введите сообщение коммита: " commit_message
git commit -m "$commit_message"
git push origin main
