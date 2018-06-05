pipeline {
    agent any
    options {
        timeout(time: 1, unit: "HOURS")
        timestamps()
    }
    stages {
        stage("Build") {
            steps {
                bat 'C:\\\\Users\\\\Elliott\\\\Documents\\\\Environments\\\\General\\\\Scripts\\\\activate'
                // bat "pip install -r REQUIREMENTS"
            }
        }
        stage("Test") {
            steps {
                echo "Starting Tests"
            }
            post {
                always {
                    echo "Done Tests"
                }
            }
        }
        stage("Deploy") {
            when {
                branch "master"
            }
            steps {
                echo "Starting Deploy"
            }
            post {
                always {
                    echo "Done Deploy"
                }
            }
        }
    }
}
