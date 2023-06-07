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
        stage('Deploy') {
            steps {
                bat 'ping 172.16.178.94'
            }
        }
    }

    post {
        success {
            script {
                emailext subject: 'Build Successful', 
                          body: '<strong>Dear Concerned</strong><br><br>Job executed successfully. Details are given below<br><br>'+'''$BUILD_LOG'''+'<br><br>Regards<br><br><strong>Jenkins Support</strong>',
                          to: 'waqas.rafique@nayatel.com',
                          from: 'malikwaqas14796@gmail.com'
            }
        }

        failure {
            script {
                emailext subject: 'Build Unsuccessful', 
                          body: '<strong>Dear Concerned</strong><br><br>Job execution unsuccessful. Please go through below details and re-push changes after rectification.<br><br>'+'''$BUILD_LOG'''+'<br><br>Regards<br><br><strong>Jenkins Support</strong>',
                          to: 'waqas.rafique@nayatel.com',
                          from: 'malikwaqas14796@gmail.com'
            }
        }
    }
}