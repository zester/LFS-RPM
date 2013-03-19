#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
_list=(zlib berkeley-db elfutils nspr nss popt readline rpm)
trap 'echo Toolchain build failed...;touch ${FAILURE};exit 1' ERR
for i in ${_list[@]}; do
	[ -f ${FAILURE} ] && (printf "Tool chain: Error exiting script \n";exit 0)
	pushd ${i}  > /dev/null 2>&1
	if [ -e ${i}.done ]; then
		echo "${i} --> Already Built"
	else
		unlink ${i}.log
		echo "Building---> ${i}"
		( ./${i}.sh |& tee "${i}.log" ) || false
		echo "Build ---> ${i} completed"
		touch ${i}.done
	fi
	popd > /dev/null 2>&1
done
