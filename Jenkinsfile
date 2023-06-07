pipeline {
    agent any

    stages {
        stage('Build') {
            
                steps {
                    script{
                    bat 'python --version'
                }
            }
        }
        stage('Test stage') {
            
                steps {
                    script {
                    bat 'python hello-world.py'
                }
            }
        }
        stage('Deploy') {
            steps {
                bat 'telnet 172.16.178.94 2002 >error.log'
            }
        }
    }
}