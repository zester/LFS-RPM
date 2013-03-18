#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
_list=(zlib berkeley-db elfutils nspr nss popt readline rpm) # lua
trap 'echo Toolchain build failed...;touch ${FAILURE};exit 1' ERR
for i in ${_list[@]}; do
	[ -f ${FAILURE} ] && (printf "Tool chain: Error exiting script \n";exit 0)
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
