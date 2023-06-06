pipeline {
    agent any

    stages {
        stage('Build') {
            script {
                steps {
                    'python --version'
                }
            }
        }
        stage('Test stage') {
            script {
                steps {
                    'python hello-world.php'
                }
            }
        }
        // stage('Deploy') {
        //     steps {
        //         echo 'Deploying.....'
        //     }
        // }
    }
}