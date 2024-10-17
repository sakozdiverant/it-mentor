#!/bin/bash

cd /d/it-mentor
git add .
read -p "Введите сообщение коммита: " commit_message
git commit -m "$commit_message"
git push origin main

#make key
#ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
#eval "$(ssh-agent -s)"
#ssh-add ~/.ssh/git_for_itm
#cat ~/.ssh/id_rsa.pubgit
#Шаг 4: Добавление SSH-ключа на GitHub
#
#    Войдите в вашу учетную запись на GitHub.
#    Перейдите в Settings (нажмите на свой аватар в правом верхнем углу и выберите Settings).
#    В меню слева выберите SSH and GPG keys.
#    Нажмите кнопку New SSH key.
#    Вставьте ваш SSH-ключ в поле Key.
#    Дайте ключу название (например, "My Laptop") и нажмите Add SSH key.
#
#ssh -T git@github.com
#git remote -v
#Если вы видите, что URL начинается с https://github.com/, то репозиторий использует HTTPS.
#git remote set-url origin git@github.com:sakozdiverant/it-mentor.git
#https://github.com/sakozdiverant/it-mentor.git
#Где:
#
#    USERNAME — это ваше имя пользователя на GitHub.
#    REPOSITORY — название вашего репозитория.
#
#Например, если ваш репозиторий называется my-repo, команда будет выглядеть так:

#windows

#ssh-agent
#ssh-add C:\Users\admin\.ssh\git_for_itm
#ssh-agent