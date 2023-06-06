pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'php --version'
            }
        }
        stage('Test stage') {
            steps {
                echo 'php hello-world.php'
            }
        }
        // stage('Deploy') {
        //     steps {
        //         echo 'Deploying....'
        //     }
        // }
    }
}