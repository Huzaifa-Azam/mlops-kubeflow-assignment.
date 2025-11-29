pipeline {
    agent any
    stages {
        stage('Environment Setup') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Pipeline Compilation') {
            steps {
                sh 'python pipeline.py'
            }
        }
    }
}
