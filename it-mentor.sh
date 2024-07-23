#! bash

cd /d/ucheba_python/it-mentor
git add .
read -p "Введите сообщение коммита: " commit_message
git commit -m "$commit_message"
git push origin main
