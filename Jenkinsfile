pipeline {
    agent any

    environment {
        PROJECT_DIR = 'backend'
        VENV_PATH = "${PROJECT_DIR}/venv"
        FLASK_APP = "${PROJECT_DIR}/app.py"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: 'main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/susakom/travelblog.git',
                        credentialsId: 'github-credentials'  // Добавьте credentials в Jenkins
                    ]]
                ])
            }
        }

        stage('Setup Environment') {
            steps {
                sh """
                    python3 -m venv venv
                    pip install --upgrade pip wheel
                    . ./venv/bin/activate
                    //  Установка зависимостей
                    pip install -r backend/requirements.txt
                """
            }
        }

   
        stage('Deploy') {
            steps {
                sh """
                    # Переход в директорию проекта
                    cd "${PROJECT_DIR}"
                    
                    # Создаем venv при необходимости
                    if [ ! -d "${VENV_PATH}" ]; then
                        python3 -m venv "${VENV_PATH}"
                        . "${VENV_PATH}/bin/activate"
                        
                    else
                        . "${VENV_PATH}/bin/activate"
                    fi
                    
                    # Установка зависимостей
                    pip install -r "${PROJECT_DIR}/requirements.txt"
                    
                    # Проверка venv
                    if [ ! -f "${VENV_PATH}/bin/python" ]; then
                        echo "ERROR: Виртуальное окружение не найдено"
                        exit 1
                    fi
                    
                    python app.py &
                    
                    sleep 5
                    if ! pgrep -f "python app.py"; then
                        echo "ERROR: Процесс не запустился"
                        [ -f app.log ] && cat app.log
                        exit 1
                    fi
                """
            }
        }

    }
}
