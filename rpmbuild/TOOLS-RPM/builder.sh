#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
list="zlib berkeley-db nspr nss popt readline elfutils rpm"
trap 'echo Toolchain build failed...;touch ${FAILURE};exit 1' ERR
die(){
	touch ${FAILURE}
	printf "Tool chain: die: exiting script \n"
	exit 1
}
for i in ${list}; do
	[ -f ${FAILURE} ] && die
	if [ -e DONE/${i} ]; then
		echo "${i} --> Already Built"
	else
		[ -e LOGS/${i} ] && unlink LOGS/${i}
		echo "Building---> ${i}"
		( ./${i}.sh |& tee LOGS/${i} ) || die 
		echo "Build ---> ${i} completed"
		touch DONE/${i}
	fi
done
