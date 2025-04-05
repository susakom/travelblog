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
                    cd "${PROJECT_DIR}"
                    python3 -m venv venv
                    pip install --upgrade pip wheel
                    . ./venv/bin/activate
                    pip install -r backend/requirements.txt
                """
            }
        }
   
        stage('Deploy') {
            steps {
                sh """
                    # Переход в директорию проекта
                    cd "${PROJECT_DIR}"
                    . ./venv/bin/activate
                    python app.py &
                                        
                """
            }
        }

    }
}
