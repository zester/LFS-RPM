#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
export FAILURE=$(pwd)'/FAILURE'
export MAKEFLAGS='-j2'
export CFLAGS="-march=i486 -mtune=i686 -O2 -pipe"
export CXXFLAGS="-march=i486 -mtune=i686 -O2 -pipe"
export LDFLAGS="-Wl,-O1,--sort-common,--as-needed,-z,relro"
_list=(berkeley-db elfutils lua nspr nss popt rpm)
trap 'echo Base package build failed...;touch ${FAILURE};exit 1' ERR
for i in ${_list[@]}; do
	if [ -e ${FAILURE} ]; then
		printf "Base package build: Error exiting script \n"
		exit 0
	fi
	pushd ${i}  > /dev/null 2>&1
	if [ -e DONE ]; then
		echo "${i} --> Already Built"
	else
		rm -rf pkg src *.log
		echo "Building---> ${i}"
		( ./build.sh |& tee build.log ) || false
		echo "Build ---> ${i} completed"
		touch DONE
	fi
	popd > /dev/null 2>&1
done
