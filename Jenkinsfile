pipeline {
    agent any

    stages {
        stage('Build') {
            
                steps {
                    script {
                    sh 'python --version'
                }
            }
        }
        stage('Test stage') {
            
                steps {
                    script {
                    sh 'python hello-world.py'
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