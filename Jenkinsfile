pipeline {
    agent any
    bat "source C:\\Users\\Developer\\Documents\\Environments\\General\\Scripts\\Python.exe"
    options {
        timeout(time: 1, unit: "HOURS")
        timestamps()
    }
    stages {
        stage("Build") {
            steps {
                bat "pip install -r REQUIREMENTS"
            }
            post {
                always {
                    echo "Done Build"
                }
            }
        }
        stage("Test") {
            steps {
                //
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
                //
            }
            post {
                always {
                    echo "Done Deploy"
                }
            }
        }
    }
}
