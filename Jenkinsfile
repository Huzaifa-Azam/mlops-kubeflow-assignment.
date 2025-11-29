pipeline {
    agent any
    stages {
        stage('Environment Setup') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pip install "kfp<2.0"'
            }
        }
        stage('Pipeline Compilation') {
            steps {
                sh 'python pipeline.py'
                sh 'ls -l pipeline.yaml'
            }
        }
    }
}
