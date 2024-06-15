pipeline {
    agent any

    environment {
        TEST_RESULTS_DIR = "results"
        RECIPIENT = "dualcorp2007@gmail.com"
    }

    stages {
        stage('Prepare Environment') {
            steps {
                script {
                    sh "mkdir -p ${env.TEST_RESULTS_DIR}"
                }
            }
        }

        stage('Source') {
            steps {
                // Obtener el código de un repositorio de GitHub
                git 'https://github.com/dualcorp/unir-cicd.git'
                sh 'ls -ltr'
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building stage!'
                sh 'make build'
            }
        }

        stage('Unit tests') {
            steps {
                sh 'make test-unit'
                archiveArtifacts artifacts: 'results/*.xml'
                archiveArtifacts artifacts: 'results/*.html'
            }
        }
        
        stage('Test Api') {
            steps {
                sh 'make test-api'
                archiveArtifacts artifacts: 'results/*.xml'
                archiveArtifacts artifacts: 'results/*.html'
            }
        }
        
        stage('Test e2e') {
            steps {
                sh 'make test-e2e'
                archiveArtifacts artifacts: 'results/*.xml'
                archiveArtifacts artifacts: 'results/*.html'
            }
        }
    }
    
    post {
        success {
            
             emailext(
                subject: "Jenkins Job '${env.JOB_NAME}' (${env.BUILD_NUMBER}) Ejecutado Satisfactoriamente",
                body: """
                Master Unir DevOps pruebas Jenkins
                <p>Pipeline <b>${env.JOB_NAME}</b> se ha completado.</p>
                <p>La referencia del proyecto esta en <a href="${env.BUILD_URL}">${env.BUILD_URL}</a> para ver mas resultado.</p>
                """,
                to: "${env.RECIPIENT}",
                attachmentsPattern: "results/*.xml"
            )
        }
        
        always {
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'results',
                reportFiles: 'coverage/index.html',
                reportName: 'Test Reports Converge'
            ])
            
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'results',
                reportFiles: 'cypress_result.html',
                reportName: 'Test Cyprex'
            ])
            junit 'results/*_result.xml'
            //cleanWs()
        }
        
        unstable {
            emailext(
                subject: "Jenkins Job '${env.JOB_NAME}' (${env.BUILD_NUMBER}) Ejecucion Inestable",
                body: """
                <p>Pipeline <b>${env.JOB_NAME}</b> es inestable.</p>
                <p>La referencia del proyecto esta en <a href="${env.BUILD_URL}">${env.BUILD_URL}</a> para ver mas resultado.</p>
                """,
                to: "${env.RECIPIENT}",
                recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'CulpritsRecipientProvider']]
            )
        }
    }
}
