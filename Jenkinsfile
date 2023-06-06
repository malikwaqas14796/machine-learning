pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                'python --version'
            }
        }
        stage('Test stage') {
            steps {
                'python hello-world.php'
            }
        }
        // stage('Deploy') {
        //     steps {
        //         echo 'Deploying....'
        //     }
        // }
    }
}