#!/usr/bin/env bash

set -e

source define_repo.sh

docker pull $REPO
docker build --tag $NAME \
             --cache-from $REPO \
             context

DATA_DIR=/tmp/refinery-developer-vis-tool_`date +"%Y-%m-%d_%H-%M-%S"`

cp -a test-data $DATA_DIR

docker run --detach \
           --name $NAME \
           --publish 80 \
           --volume $DATA_DIR:/usr/share/nginx/html/data \
           $NAME

python test.py $NAME