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
                    # Создаем venv при необходимости
                    if [ ! -d "${VENV_PATH}" ]; then
                        python3 -m venv "${VENV_PATH}"
                        . "${VENV_PATH}/bin/activate"
                        pip install --upgrade pip wheel
                    else
                        . "${VENV_PATH}/bin/activate"
                    fi
                    
                    # Установка зависимостей
                    pip install -r "${PROJECT_DIR}/requirements.txt"
                """
            }
        }

        // stage('Test') {
        //     steps {
        //         sh """
        //             cd "${PROJECT_DIR}"
        //            . ./venv/bin/activate
                    
        //             # Установка тестовых зависимостей
        //             pip install pytest pytest-cov
                    
        //             # Запуск тестов
        //             python -m pytest tests/ \
        //                 --cov=app \
        //                 --cov-report=xml:coverage.xml \
        //                 --junitxml=test-results.xml \
        //                 --disable-warnings
        //         """
        //         junit "${PROJECT_DIR}/test-results.xml"
        //         cobertura coberturaReportFile: "${PROJECT_DIR}/coverage.xml"
        //     }
        // }

        stage('Deploy') {
            steps {
                sh """
                    cd "${PROJECT_DIR}"
                    sh """
                    # Создаем venv при необходимости
                    if [ ! -d "${VENV_PATH}" ]; then
                        python3 -m venv "${VENV_PATH}"
                        . "${VENV_PATH}/bin/activate"
                    else
                        . "${VENV_PATH}/bin/activate"
                    fi
                    
                    # Установка зависимостей
                    pip install -r "${PROJECT_DIR}/requirements.txt"
                """

                    
                     # Проверка venv
                     if [ ! -f "\$PROJECT_DIR/venv/bin/python" ]; then
                          echo "ERROR: Виртуальное окружение не найдено"
                          exit 1
                     fi


                    // # Остановка предыдущего процесса
                    // pkill -f "python app.py" || true
                    
                    # Запуск приложения с логированием
                    // nohup python app.py > app.log 2>&1 &
                    python app.py
                    # Проверка запуска
                    sleep 5
                    if ! pgrep -f "python app.py"; then
                        echo "ERROR: Процесс не запустился"
                        cat app.log
                        exit 1
                    fi
                """
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: "${PROJECT_DIR}/app.log", allowEmptyArchive: true
            cleanWs()  // Очистка workspace
        }
        success {
            slackSend (
                channel: '#deployments',
                message: "✅ Успешный деплой ${env.JOB_NAME} (#${env.BUILD_NUMBER})\n" +
                         "Ссылка: ${env.BUILD_URL}"
            )
        }
        failure {
            slackSend (
                channel: '#deployments',
                message: "❌ Ошибка в ${env.JOB_NAME} (#${env.BUILD_NUMBER})\n" +
                         "Логи: ${env.BUILD_URL}/console"
            )
        }
    }
}
