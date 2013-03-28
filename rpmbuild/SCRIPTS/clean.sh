#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
find . -name '*.done'	-delete
find . -name "*.log"	-delete
find . -name "*~"		-delete
find . -name "*.rpm"	-delete
find . -name "*.srpm"	-delete
