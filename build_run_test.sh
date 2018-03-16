#!/usr/bin/env bash

set -e

source define_repo.sh

docker pull $REPO
docker build --tag $NAME \
             --cache-from $REPO \
             context
docker run --env INPUT_JSON_URL=http://data.cloud.refinery-platform.org.s3.amazonaws.com/data/scott/sample.json \
           --detach \
           --name $NAME \
           --publish 80 \
           $NAME

python test.py $NAME