# ModCloth App

Application deployment bits for ModCloth

## Requirements &amp; Dependencies

The [`docker_pull`](
https://github.com/modcloth-labs/ansible-module-docker-pull) module is used to
pull docker containers.

## Variables

``` yaml
---
# Equivalent of `CMD` to be passed to `docker run`
modcloth_app_docker_command:

# Repository portion of docker image specification, e.g. "busybox",
# "quay.io/modcloth/foo"
modcloth_app_docker_repo:

# Tag portion of docker image specification, e.g.: "latest", "master"
modcloth_app_docker_tag: latest

# Proxy port for docker container, passed via `-p` to `docker run`
modcloth_app_docker_port: 3000

# Environment variable mapping written to /etc/default/{{ modcloth_app_name }}
# which is passed to `docker run` via `--env-file`
modcloth_app_env: {}

# Template used for the file written to /etc/default/{{ modcloth_app_name }}
modcloth_app_etc_default_template: etc-default.j2

# Application name used in file paths, service actions, etc.
modcloth_app_name: app

# Template used for the file written to /etc/init/{{ modcloth_app_name }}.conf
modcloth_app_upstart_conf_template: upstart.conf.j2
```

## License

Licensed under the MIT license.  See the [LICENSE](./LICENSE) file for details.
