pipeline {
    agent any

    stages {
        stage('Build') {
            
                steps {
                    script {
                    bat 'choco install python3 -y'
                    bat 'python --version'
                }
            }
        }
        stage('Test stage') {
            
                steps {
                    script{
                    bat 'python hello-world.py'
                }
            }
        }
        // stage('Deploy') {
        //     steps {
        //         echo 'Deploying......'
        //     }
        // }
    }
}