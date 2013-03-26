#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
_list=(zlib berkeley-db nspr nss popt readline elfutils rpm) # lua
trap 'echo Toolchain build failed...;touch ${FAILURE};exit 1' ERR
for i in ${_list[@]}; do
	[ -f ${FAILURE} ] && (printf "Tool chain: Error exiting script \n";exit 0)
	if [ -e ${i}.done ]; then
		echo "${i} --> Already Built"
	else
		[ -e ${i}.log ] && unlink ${i}.log
		echo "Building---> ${i}"
		( ./${i}.sh |& tee "${i}.log" ) || false
		echo "Build ---> ${i} completed"
		touch ${i}.done
	fi
done
