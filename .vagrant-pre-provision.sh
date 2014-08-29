#!/bin/bash

set -e

if [[ -e /vagrant/.dockercfg ]] ; then
  cp -v /vagrant/.dockercfg /root/.dockercfg
fi
