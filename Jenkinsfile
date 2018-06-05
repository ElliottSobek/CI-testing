pipeline {
    agent any
    options {
        timeout(time: 1, unit: "HOURS")
        timestamps()
    }
    stages {
        stage("Build") {
            steps {
                bat "source C:\\Users\\Developer\\Documents\\Environments\\General\\Scripts\\Python.exe"
                bat "pip install -r REQUIREMENTS"
            }
            post {
                always {
                    echo "Done Build"
                }
            }
        }
        stage("Test") {
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
            post {
                always {
                    echo "Done Deploy"
                }
            }
        }
    }
}
