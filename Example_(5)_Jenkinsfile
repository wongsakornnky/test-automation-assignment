pipeline {
    agent any

    stages {

        stage('Checkout Code From Git') {
            steps {
                git 'https://github.com/your-repository.git'
            }
        }

        stage('Run Test Automate') {
            steps {
                sh 'python test_script.py'
            }
        }

        stage('Send Result To Jenkins') {
            steps {
                echo 'Test execution completed'
            }
        }

    }
}
