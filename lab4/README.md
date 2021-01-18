1.В даній лабораторній ознайомився з Docker, перевірив версію, вивів help та image.
---
2.Створив власний репозиторій на Docker Hub - AndriyRubets/lab4/
---
3.Для запуску веб-сервера використав команду: "sudo docker run -it --name=django --rm -p 8000:8000 AndriyRubets/lab4:django"
---
4.Створив файл Dockerfile.site
---
5.Для отримання логів серверу виконую команди: sudo docker run -it --name=django --rm -p 8000:8000 alcori/lab4:django sudo docker run -it --rm --net=host -v $(pwd)/server.log:/app/server.log alcori/lab4:monitoring
---
