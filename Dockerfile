FROM python:3.13.3


#label
LABEL maintainer="Susak"
LABEL version="1.0"
LABEL description="Python app Flask"

# work directory
WORKDIR /home/susak/python_app


# working port
EXPOSE 80

# установка зависимостей из файла equirements.txt\
# Сначала копируем ТОЛЬКО requirements.txt
COPY ./backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt  
# копируем остальной код
COPY . .  

CMD ["python3", "./backend/app.py"]