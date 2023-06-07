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
                    bat 'xvfb-run --server-args="-screen 0 1280x1024x24" python C:/Users/muhammad-waqas/Desktop/test-case/test-case.py'
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
            script{
                emailext subject: 'Build Successful', 
                          body: 'The build was successful. Congratulations!',
                          to: 'waqas.rafique@nayatel.com',
                          from: 'malikwaqas14796@gmail.com'
            }
        }
    }
}