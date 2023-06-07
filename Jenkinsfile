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
                    bat 'python C:/Users/muhammad-waqas/Desktop/test-case/test-case.py'
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
                          body: '''$BUILD_LOG''',
                          to: 'waqas.rafique@nayatel.com',
                          from: 'malikwaqas14796@gmail.com'
            }
        }
    }
}