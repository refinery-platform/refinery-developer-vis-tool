# [refinery-developer-vis-tool](https://hub.docker.com/r/scottx611x/refinery-developer-vis-tool/) [![Build Status](https://travis-ci.org/scottx611x/refinery-developer-vis-tool.svg?branch=master)](https://travis-ci.org/scottx611x/refinery-developer-vis-tool)
A basic Refinery-compatible visualization tool to aid prospective Refinery VisualizationTool developers.

This docker image runs an nginx server and expects one to populate `/usr/share/nginx/html/data` with a valid JSON file called: `input.json`. Whatever information is inside of `/usr/share/nginx/html/data/input.json` is displayed in a webpage like so:

![screen shot 2017-10-18 at 10 11 14 am](https://user-images.githubusercontent.com/5629547/31723398-bac2030a-b3ec-11e7-9cdc-30bb1adb4979.png)





🐳
`docker pull scottx611x/refinery-developer-vis-tool`

## Running the conatiner
See [build_run_test.sh](https://github.com/scottx611x/refinery-developer-vis-tool/blob/master/build_run_test.sh) for an idea of how to properly run this container.

## Running tests
`sh /build_run_test.sh`

Some ouput data show be displayed with your tests results and where to access your running container:
```
test_home_page (__main__.ContainerTest) ... ok
test_input_data_exists (__main__.ContainerTest) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.153s

OK
browse:   http://localhost:32787/
clean up: docker ps -qa | xargs docker stop | xargs docker rm
PASS!
```
