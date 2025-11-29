pipeline {
    agent any
    stages {
        stage('Environment Setup') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }
        stage('Pipeline Execution') {
            steps {
                bat 'python pipeline.py'
            }
        }
    }
}
