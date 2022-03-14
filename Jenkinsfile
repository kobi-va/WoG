pipeline {
    agent { label 'agent_1' }
    stages {
        stage('Build docker image') {
            steps {
                sh 'docker build -t moditamam/selenium:from-jenkins-pipeline .'
            }
        }
        stage('Run & Test') {
            agent {
                docker {
                    image "moditamam/selenium:from-jenkins-pipeline"
                    reuseNode true
                }
            }
            steps {
                sh 'python3 /app/MainScores.py &'
                sh 'sleep 5'
                sh 'python3 /app/e2e.py'
            }
        stage('Docker Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dockerhubPassword', usernameVariable: 'dockerhubUser')]) {
                    sh "docker login -u ${env.dockerhubUser} -p ${env.dockerhubPassword}"
                    sh 'docker push kobiva/wog:latest'
                }
            }
        }        
    }
}
