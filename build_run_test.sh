#!/usr/bin/env bash

set -e

source define_repo.sh

docker pull $REPO
docker build --tag $NAME \
             --cache-from $REPO \
             context
docker run --env INPUT_JSON_URL=https://api.github.com/users/scottx611x/repos \
           --detach \
           --name $NAME \
           --publish 80 \
           --volume $DATA_DIR:/usr/share/nginx/html/data \
           $NAME

python test.py $NAME