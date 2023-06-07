pipeline {
    agent any

    stages {
        stage('Build') {
            
                steps {
                    script {
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
        //         bat 'ping 172.16.178.94'
        //     }
        // }
    }

    post {
        success {
            script {
                emailext subject: 'Build Successful', 
                          body: 'The build was successful. Congratulations!',
                          to: 'waqas.rafique@nayatel.com',
            }
        }
    }
}