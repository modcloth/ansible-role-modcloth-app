# ModCloth App

[![Build Status](https://travis-ci.org/modcloth/ansible-role-modcloth-app.svg?branch=master)](https://travis-ci.org/modcloth/ansible-role-modcloth-app)

Application deployment bits for ModCloth

## Requirements &amp; Dependencies

The [`docker_pull`](
https://github.com/modcloth-labs/ansible-module-docker-pull) module is used to
pull docker containers.

## Role Variables

``` yaml
---
# Application name used in file paths, service actions, etc.
modcloth_app_name: app

# The type of application to be deployed, either "long-running" or "cron"
# 'cron' should be used for applications that should run on a schedule (e.g. a rake task)
#   A cron entry will be inserted to run this task (as root)
# 'long-running' should be used for applications that behave as services and should always be up
#   An upstart job will be created to run your service (as root)
modcloth_app_type: long-running

# Environment variable mapping written to /etc/default/{{ modcloth_app_name }}
# which is passed to `docker run` via `--env-file`
modcloth_app_env: {}

# Template used for the file written to /etc/default/{{ modcloth_app_name }}
modcloth_app_etc_default_template: etc-default.j2

# Equivalent of `CMD` to be passed to `docker run`
modcloth_app_docker_command: ""

# Repository portion of docker image specification, e.g. "busybox",
# "quay.io/modcloth/foo"
modcloth_app_docker_repo: ""

# Tag portion of docker image specification, e.g.: "latest", "master"
modcloth_app_docker_tag: latest

# Proxy port for docker container, passed via `-p` to `docker run`
modcloth_app_docker_port: 3000
# Also valid:
# modcloth_app_docker_port:
# - { host: 3000, container: 80 }
# - { host: 8080, container: 9292, ip: 127.0.0.1 }
# - { container: 22, ip: 127.0.0.1 }
# Invalid (must at least specify container ip):
# - { host: 22, ip: 127.0.0.1 }

# volumes to mount into the docker container
# ensures the directory on the host will be created
modcloth_app_docker_volumes: []
# Example:
# - { host: /var/lib/redis, container: /var/lib/redis, directory: yes }

# adds the --link option for `docker run` to the templates
modcloth_app_docker_link: []
# Example:
# - { name: style-gallery, alias: style-gallery }
# # note: alias, if not provided, defaults to the same value as name

# Cron job schedule
modcloth_app_cron_schedule: "* * * * *"

# Template used for the file written to
# /usr/local/bin/{{ modcloth_app_name }}-cron-wrapper
modcloth_app_cron_wrapper_template: cron-wrapper.sh.j2

# Use this with another process that feeds required data to your proccess over STDIN
# E.g. a query running in another container
modcloth_app_cron_stdin_command: ""

# Template used for the temptate used to set up logrotation
# with logrotated
modcloth_app_cron_logrotate_template: cron-logrotate.j2

# additional conditions on the upstart service
modcloth_app_upstart_start_condition: ""

# Name of the application in NewRelic (for deployment notifications)
modcloth_app_new_relic_app_name: "[{{env}}] {{modcloth_app_name}}"

# Template used for the file written to /etc/init/{{ modcloth_app_name }}.conf
modcloth_app_upstart_conf_template: upstart.conf.j2

# Whether to notify NewRelic of app deployments
modcloth_app_notify_new_relic: false

# Whether or not to ship logs using the modcloth.rsyslog-file role (see meta/main.yml)
modcloth_app_ship_logs: true
```

## External Dependency Variables

```yaml
---
# Github API token
github_token: "{{ github_api_token | default('') }}"

# HipChat API token
hipchat_token: "{{ hipchat_api_token | default('') }}"

# HipChat room id
hipchat_room: "{{ hipchat_team_room | default('') }}"

# NewRelic API token (for deployment notifications)
new_relic_api_token: "{{ new_relic_api_token | default('') }}"
```

## License

Licensed under the MIT license.  See the [LICENSE](./LICENSE) file for details.
