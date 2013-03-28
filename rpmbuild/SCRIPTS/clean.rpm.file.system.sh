#!/bin/bash
#set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
LFS=/mnt/lfs
SCRIPTS/umount.kernel.filesystem.sh
LIST=('bin' 'boot' 'dev' 'etc' 'home' 'lib' 'lib64' 'media' 'mnt' 'opt' 'proc' 'root' 'run' 'sbin' 'srv' 'sys' 'tmp' 'usr' 'var')
for i in ${LIST[@]}; do
	 rm -vrf "${LFS}/${i}" || true
done
rm -vrf "RPMS/*" "BUILD/*"
