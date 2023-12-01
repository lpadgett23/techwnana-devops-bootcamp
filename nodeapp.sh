#!/bin/bash



# download the artifact
curl -O "https://node-envvars-artifact.s3.eu-west-2.amazonaws.com/bootcamp-node-envvars-project-1.0.0.tgz"

# extract the tarball
tar -xvf bootcamp-node-envvars-project-1.0.0.tgz

# install Node.js and npm
sudo cp -R node-{$1}/bin/* /usr/local/bin

#check the versions 
$1=node -v
$2=npm -v

# set the needed environment variables
export APP_ENV=dev
export DB_USER=myuser
export DB_PWD=mysecret

# change into the unzipped package directory
cd ~/app/

# run the NodeJS application
npm install
node server.js
