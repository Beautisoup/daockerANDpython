pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials') // Jenkins 中存储的 Docker Hub 凭证 ID
        DOCKER_IMAGE_NAME = "liyuanrui/my-flask-app" // Docker Hub 镜像名称
        DOCKER_IMAGE_TAG = "liyuanrui_flask" // 镜像标签
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // 构建 Docker 镜像
                    docker.build("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}")
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    // 登录 Docker Hub
                    sh "echo ${DOCKER_HUB_CREDENTIALS_PSW} | docker login -u ${DOCKER_HUB_CREDENTIALS_USR} --password-stdin"
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // 推送镜像到 Docker Hub
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        docker.image("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}").push()
                    }
                }
            }
        }
    }

    post {
        always {
            // 清理 Docker 登录信息
            sh 'docker logout'
        }
    }
}