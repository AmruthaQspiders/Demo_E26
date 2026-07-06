pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '''
                    py -m pip install --upgrade pip
                    py -m pip install -r requirements.txt
                    py -m pip install pytest pytest-html
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    if not exist reports mkdir reports
                    py -m pytest tests --html=reports/report.html --self-contained-html
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
