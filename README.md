# ModCloth App

[![Build Status](https://travis-ci.org/modcloth/ansible-role-modcloth-app.svg?branch=master)](https://travis-ci.org/modcloth/ansible-role-modcloth-app)

Application deployment bits for ModCloth

## Requirements &amp; Dependencies

The [`docker_pull`](
https://github.com/modcloth-labs/ansible-module-docker-pull) module is used to
pull docker containers.

## Variables

``` yaml
---
# Application name used in file paths, service actions, etc.
modcloth_app_name: app

# The type of application to be deployed, either "long-running" or "cron"
modcloth_app_type: long-running

# Environment variable mapping written to /etc/default/{{ modcloth_app_name }}
# which is passed to `docker run` via `--env-file`
modcloth_app_env: {}

# Equivalent of `CMD` to be passed to `docker run`
modcloth_app_docker_command: ""

# Repository portion of docker image specification, e.g. "busybox",
# "quay.io/modcloth/foo"
modcloth_app_docker_repo: ""

# Tag portion of docker image specification, e.g.: "latest", "master"
modcloth_app_docker_tag: latest

# Proxy port for docker container, passed via `-p` to `docker run`
modcloth_app_docker_port: 3000

# Cron job schedule
modcloth_app_cron_schedule: "* * * * *"

# Template used for the file written to /etc/default/{{ modcloth_app_name }}
modcloth_app_etc_default_template: etc-default.j2

# Template used for the file written to /etc/init/{{ modcloth_app_name }}.conf
modcloth_app_upstart_conf_template: upstart.conf.j2

# Template used for the file written to
# /usr/local/bin/{{ modcloth_app_name }}-cron-wrapper
modcloth_app_cron_wrapper_template: cron-wrapper.sh.j2

# Use this with another process that feeds required data to your proccess over STDIN
# E.g. a query running in another container
modcloth_app_cron_stdin_command: ""

# Template used for the temptate used to set up logrotation
# with logrotated
modcloth_app_cron_logrotate_template: cron-logrotate.j2

# Addition arguments to pass to `docker run`
modcloth_app_docker_args: []

# additional conditions on the upstart service
modcloth_app_upstart_start_condition: ""

# volumes to mount into the docker container
# ensures the directory on the host will be created
modcloth_app_docker_volumes: []
```

## License

Licensed under the MIT license.  See the [LICENSE](./LICENSE) file for details.
