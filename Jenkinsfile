pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    pip install -r requirements.txt
                    pip install pytest pytest-html
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    pytest tests --html=reports/report.html --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            publishHTML(target: [
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Pytest HTML Report',
                keepAll: true,
                alwaysLinkToLastBuild: true,
                allowMissing: false
            ])
        }
    }
}
