pipeline {
    agent any
    stages {
        stage('Environment Setup') {
            steps {
                bat 'C:\\Users\\huzai\\AppData\\Local\\Programs\\Python\\Python310\\python.exe -m pip install -r requirements.txt'
            }
        }
        stage('Pipeline Execution') {
            steps {
                bat 'C:\\Users\\huzai\\AppData\\Local\\Programs\\Python\\Python310\\python.exe pipeline.py'
            }
        }
    }
}
