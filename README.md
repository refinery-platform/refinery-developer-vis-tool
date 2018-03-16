# [refinery-developer-vis-tool](https://hub.docker.com/r/scottx611x/refinery-developer-vis-tool/) [![Build Status](https://travis-ci.org/scottx611x/refinery-developer-vis-tool.svg?branch=master)](https://travis-ci.org/scottx611x/refinery-developer-vis-tool)
A basic Refinery-compatible visualization tool to aid prospective Refinery VisualizationTool developers.

This docker image runs simple webserver using python and expects one to populate `/usr/src/app` with a valid JSON file called: `input.json`. 
This is done by providing a url to the container that points to valid JSON. See [build_run_test.sh](https://github.com/scottx611x/refinery-developer-vis-tool/blob/master/build_run_test.sh#L11)
Whatever information is inside of `/usr/src/app/input.json` is displayed in a webpage like so:

<img width="1130" alt="screen shot 2017-10-17 at 4 21 19 pm" src="https://user-images.githubusercontent.com/5629547/31687440-450d943e-b357-11e7-9ba3-3d7500cf8f37.png">




🐳
`docker pull scottx611x/refinery-developer-vis-tool`

## Running the conatiner
See [build_run_test.sh](https://github.com/scottx611x/refinery-developer-vis-tool/blob/master/build_run_test.sh) for an idea of how to properly run this container.

## Running tests
`./build_run_test.sh`

Some ouput data should be displayed with your test results as well as where to access your running container:
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
