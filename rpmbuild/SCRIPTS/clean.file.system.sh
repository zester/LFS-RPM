#!/bin/bash
#set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
LFS=/mnt/lfs
LIST=('bin' 'boot' 'dev' 'etc' 'home' 'lib' 'lib64' 'media' 'mnt' 'opt' 'proc' 'root' 'run' 'sbin' 'srv' 'sys' 'tmp' 'usr' 'var' '/tools/bin')
for I in ${LIST[@]}; do
	 rm -vrf ${LFS}/${I} || true
done
