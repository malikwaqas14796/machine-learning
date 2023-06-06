pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'php --version'
            }
        }
        stage('Test stage') {
            steps {
                sh 'php hello-world.php'
            }
        }
        // stage('Deploy') {
        //     steps {
        //         echo 'Deploying....'
        //     }
        // }
    }
}