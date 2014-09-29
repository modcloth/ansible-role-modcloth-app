.PHONY: deps
deps: library/docker_pull README.md roles/modcloth.rsyslog-file/README.md

library/docker_pull: library
	curl -o $@ -Ls https://raw.githubusercontent.com/modcloth-labs/ansible-module-docker-pull/master/docker_pull

library:
	mkdir -p $@

roles/modcloth.rsyslog-file/README.md: roles
	ansible-galaxy install -p $(PWD)/roles modcloth.rsyslog-file

roles:
	mkdir -p $@
