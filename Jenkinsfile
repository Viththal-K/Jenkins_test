pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Viththal-K/Jenkins_test.git']])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/Viththal-K/Jenkins_test.git'
                bat 'python3 list_op.py'
            }
        }
        stage('Test') {
            steps {
                bat 'python3 -m pytest -v'
            }
        }
    }
}
