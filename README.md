# refinery-developer-vis-tool
[![Build Status](https://travis-ci.org/refinery-platform/refinery-developer-vis-tool.svg?branch=master)](https://travis-ci.org/refinery-platform/refinery-developer-vis-tool)
[🐳 `docker pull scottx611x/refinery-developer-vis-tool`](https://hub.docker.com/r/scottx611x/refinery-developer-vis-tool/)

A demonstration of the different ways inputs can be provided in a 
Refinery visualization tool, and, potentially, a starting point 
for other simple tools.

[build_run_test.sh](https://github.com/scottx611x/refinery-developer-vis-tool/blob/master/build_run_test.sh)
encapsulates the whole process of building and deploying a visualization tool. 
- In a real application, the tool image would already be built and would be available on DockerHub,
- and, in a real application, django_docker_engine or some other API would be used to start
the containers, rather than just using the Docker CLI.

## Running tests
```
$ pip install -r requirements.txt
$ ./build_run_test.sh`
...

OK
browse:   http://localhost:32787/
clean up: docker ps -qa | xargs docker stop | xargs docker rm
PASS!
```

At the end, you can hit the server it spun up for a manual check.
It should show JSON from three different sources.

## Release
Successful Github tags and PRs will prompt Travis to push the built image to
Dockerhub. For a new version number:
```
git tag v0.0.x && git push origin --tags
```
