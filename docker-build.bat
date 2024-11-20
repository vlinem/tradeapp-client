@echo off
REM Windows BATCH script to build docker container
@echo on
docker rmi tradeapp-client
docker build -t tradeapp-client .
