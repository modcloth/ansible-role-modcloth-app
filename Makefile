.PHONY: deps
deps: library/docker_pull

library/docker_pull: library
	curl -o $@ -Ls https://raw.githubusercontent.com/modcloth-labs/ansible-module-docker-pull/master/docker_pull

library:
	mkdir -p $@
