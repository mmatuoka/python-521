
pipeline {
    
    agent any:
    
    parameters {
        string(
            name: "SOURCE_BRANCH",
            defaultValue: "dev",
            description: "Source branch of changes"
        )
    }

    stages {
        stage("Preparation") {
            steps {
                echo "Preparando ...";
                sleep 10;
            }
        }
        stage('Build') {
            steps {
                echo 'Buildando ...'
                sleep 10;
            }
        }

        stage('Resultados') {
            steps {
                echo 'Finalizando o deploy ...'
                sleep 10;
            }
        }
    }
}