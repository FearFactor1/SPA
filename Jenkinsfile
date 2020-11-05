pipeline {
 agent {
  docker {
   image 'login'
  }
 }
 
  stages {
    stage('build') {
      steps {
        sh 'pip install pytest'
      }
    }
    stage('test/login') {
      steps {
        sh 'python3 -m pytest -v test/login'
      }   
    }
  }
}
