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
        // stage('Deploy') {
        //     steps {
        //         echo 'Deploying......'
        //     }
        // }
    }
}