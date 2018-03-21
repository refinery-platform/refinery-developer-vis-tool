#!/usr/bin/env bash

set -e

source define_repo.sh

docker pull $REPO
docker build --tag $NAME \
             --cache-from $REPO \
             context

DATA_DIR=/tmp/refinery-developer-vis-tool_`date +"%Y-%m-%d_%H-%M-%S"`
mkdir $DATA_DIR
echo '{"name": "Nils", "beverage": "water?"}' > $DATA_DIR/input.json

# In real life, input would only be supplied by one mechanism,
# but we want to test them all.
docker run --env INPUT_JSON_URL=http://data.cloud.refinery-platform.org.s3.amazonaws.com/data/scott/sample.json \
           --env INPUT_JSON='{"name": "Chuck", "beverage": "tea"}' \
           --volume $DATA_DIR:/usr/src/app/data \
           --detach \
           --name $NAME \
           --publish 80 \
           $NAME

python test.py $NAME