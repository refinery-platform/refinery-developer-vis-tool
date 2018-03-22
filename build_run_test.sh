#!/usr/bin/env bash
set -o verbose
set -o errexit
set -o nounset

source define_repo.sh

docker pull $REPO
docker build --tag $NAME \
             --cache-from $REPO \
             context

STAMP=`date +"%Y-%m-%d_%H-%M-%S"`
CONTAINER_NAME=$NAME-$STAMP
DATA_DIR=/tmp/refinery-developer-vis-tool_$STAMP
mkdir $DATA_DIR
echo '{"name": "Nils", "beverage": "water?"}' > $DATA_DIR/input.json

# In real life, input would only be supplied by one mechanism,
# but we want to test them all.
JSON='{"name": "Chuck", "beverage": "tea"}'
URL='http://data.cloud.refinery-platform.org.s3.amazonaws.com/data/scott/sample.json'
MOUNT="$DATA_DIR:/usr/src/app/data"
DEFAULTS="--detach --name $CONTAINER_NAME --publish 80 $NAME"

#####

docker run --env INPUT_JSON_URL="$URL" \
           --volume "$MOUNT" \
           $DEFAULTS
python test.py --container_name $CONTAINER_NAME --skip_envvar_value
docker stop $CONTAINER_NAME && docker rm $CONTAINER_NAME

#####

docker run --env INPUT_JSON="$JSON" \
           --volume "$MOUNT" \
           $DEFAULTS
python test.py --container_name $CONTAINER_NAME --skip_envvar_url
docker stop $CONTAINER_NAME && docker rm $CONTAINER_NAME

#####

docker run --env INPUT_JSON="$JSON" \
           --env INPUT_JSON_URL="$URL" \
           $DEFAULTS
python test.py --container_name $CONTAINER_NAME --skip_mounted
docker stop $CONTAINER_NAME && docker rm $CONTAINER_NAME

#####

docker run --env INPUT_JSON="$JSON" \
           --env INPUT_JSON_URL="$URL" \
           --volume "$MOUNT" \
           $DEFAULTS
python test.py --container_name $CONTAINER_NAME
# Leave the last one running for manual tests.