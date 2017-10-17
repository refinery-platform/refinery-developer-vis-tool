# [refinery-developer-vis-tool](https://hub.docker.com/r/scottx611x/refinery-developer-vis-tool/) [![Build Status](https://travis-ci.org/scottx611x/refinery-developer-vis-tool.svg?branch=master)](https://travis-ci.org/scottx611x/refinery-developer-vis-tool)
A basic Refinery-compatible visualization tool to aid prospective Refinery VisualizationTool developers.

This docker image runs an nginx server and expects one to populate `/usr/share/nginx/html/data` with a valid JSON valid called: `input.json`. Whatever information is inside of `/usr/share/nginx/html/data/input.json` is displayed in a webpage like so:

![screen shot 2017-10-17 at 12 39 51 pm](https://user-images.githubusercontent.com/5629547/31677301-52cce4d6-b338-11e7-93d6-4be45e42be66.png)



🐳
`docker pull scottx611x/refinery-developer-vis-tool`

# Running tests
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
