#!/bin/bash

docker build -t login .
docker run --name my_run login
#docker cp my_run:/app/allure-report .
#./allure/bin/allure serve allure-report
#rm -rf allure-report
docker system prune -f
