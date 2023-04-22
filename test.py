pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        // Run a shell command to build the code
        sh 'npm install'
      }
    }
    stage('Test') {
      steps {
        // Run a shell command to run tests
        sh 'npm test'
      }
    }
    stage('Deploy') {
      steps {
        // Run a shell command to deploy the code
        sh 'npm deploy'
      }
    }
  }
}
