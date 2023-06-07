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
        success {
            script {
                emailext subject: 'Build Successful', 
                          body: '<strong>Dear Concerned</strong><br><br>Pipeline executed successfully<br><br>Regards<strong>Jenkins Support</strong>',
                          to: 'waqas.rafique@nayatel.com',
                          from: 'malikwaqas14796@gmail.com'
            }
        }

        failure {
            script{
                emailext subject: 'Build Unsuccessful', 
                          body: '''$BUILD_LOG''',
                          to: 'waqas.rafique@nayatel.com',
                          from: 'malikwaqas14796@gmail.com'
            }
        }
    }
}