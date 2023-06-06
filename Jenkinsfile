pipeline {
    agent any

    stages {
        stage('Build') {
            
                steps {
                    script {
                    'python --version'
                }
            }
        }
        stage('Test stage') {
            
                steps {
                    script {
                    'python hello-world.php'
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