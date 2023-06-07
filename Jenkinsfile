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
                def buildLog = currentBuild.rawBuild.getLog(1000) // Change the number to limit the log size if desired
                def errorLines = buildLog.findAll { line -> line.contains("ERROR") || line.contains("Exception") } // Modify the condition as needed
                def errorMessage = errorLines.join('\n')

                emailext subject: 'Build Successful', 
                          body: errorMessage,
                          to: 'waqas.rafique@nayatel.com',
                          from: 'malikwaqas14796@gmail.com'
            }
        }
    }
}