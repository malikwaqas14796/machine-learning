pipeline {
    agent any

    stages {
        stage('Build') {
            
                steps {
                    script {
                        ${'python --version'}
                    // 'python --version'
                }
            }
        }
        stage('Test stage') {
            
                steps {
                    script {
                    ${'python hello-world.py'}
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