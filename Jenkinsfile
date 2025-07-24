pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "vote-app"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/orvencasido/voting-web-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('Stop Existing Container') {
            steps {
                script {
                    sh "docker stop ${DOCKER_IMAGE} || true"
                    sh "docker rm ${DOCKER_IMAGE} || true"
                }
            }
        }

        stage('Run Redis if Not Running') {
            steps {
                script {
                    sh '''
                    if [ "$(docker ps -q -f name=redis)" = "" ]; then
                        if [ "$(docker ps -aq -f status=exited -f name=redis)" != "" ]; then
                            docker start redis
                        else
                            docker run -d --name redis redis:alpine
                        fi
                    fi
                    '''
                }
            }
        }

        stage('Run New Container') {
            steps {
                script {
                    sh "docker run -d -p 5000:5000 --link redis --name ${DOCKER_IMAGE} ${DOCKER_IMAGE}"
                }
            }
        }
    }

    post {
        success {
            echo "Deployment successful! Visit your EC2: http://YOUR_EC2_PUBLIC_IP:5000"
        }
        failure {
            echo "Deployment failed."
        }
    }
}

