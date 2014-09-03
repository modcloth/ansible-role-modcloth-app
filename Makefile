.PHONY: deps
deps: library/docker_pull README.md

library/docker_pull: library
	curl -o $@ -Ls https://raw.githubusercontent.com/modcloth-labs/ansible-module-docker-pull/master/docker_pull

library:
	mkdir -p $@

README.md: .README.head.md .README.tail.md
	cat .README.head.md defaults/main.yml .README.tail.md > $@
