#!/bin/bash

set -e

if ! docker version ; then
  curl -sL https://get.docker.io | bash
fi
