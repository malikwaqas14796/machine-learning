pipeline {
    agent any

    stages {
        stage('Build') {
            
                steps {
                    script {
                    batt 'python --version'
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
        failure {
            script{
                emailext subject: 'Build Successful', 
                          body: 'The build was successful. Congratulations!',
                          to: 'malikwaqas14796@gmail.com',
                          from: 'malikwaqas14796@gmail.com'
            }
        }
    }
}