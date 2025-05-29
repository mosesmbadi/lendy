pipeline {
  agent any
  stages {
    stage('Clone') {
      steps {
        echo 'Cloning repository...'
        dir(path: 'lendy') {
          git(branch: 'main', url: 'https://github.com/victorgpt0/lendy.git')
        }

      }
    }

    stage('Install Dependencies & Test') {
      steps {
        echo 'Installing dependencies in the Jenkins container... python version matters'
      }
    }

    stage('Build Docker Image') {
      steps {
        echo 'Building Docker image...'
        dir(path: 'lendy') {
          sh '''
                        docker build -t $IMAGE_NAME .
                    '''
        }

      }
    }

    stage('Push Docker Image to dockerhub') {
      steps {
        echo 'Pushing Docker image to Docker Hub...'
        dir(path: 'lendy') {
          script {
            def dockerImageTag = "${DOCKER_HUB_REPO}:latest"
            // Using credentials for Docker Hub login securely
            withCredentials([usernamePassword(
              credentialsId: 'dockerhub-creds',
              usernameVariable: 'DOCKER_USER',
              passwordVariable: 'DOCKER_PASS'
            )]) {
              sh """
              echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
              docker tag $IMAGE_NAME $dockerImageTag
              docker push $dockerImageTag
              """
            }
          }

        }

      }
    }

    stage('Run Docker Image') {
      steps {
        echo 'run Docker image...'
        sh '''
                    docker rm -f lendy_container || true
                    docker run -d --name lendy_container -p 8080:8080 $IMAGE_NAME
                '''
      }
    }

  }
  environment {
    IMAGE_NAME = 'lendy-app'
    SECRET_KEY = credentials('DJANGO_SECRET_KEY')
    COMPOSE_FILE = 'lendy/docker-compose.yml'
    DOCKER_HUB_REPO = 'victorgptea/v1ct0rg'
  }
  post {
    success {
      echo 'Build and deploy successful!'
    }

    failure {
      echo 'Build or deploy failed.'
    }

    always {
      echo 'Pipeline finished.'
    }

  }
}