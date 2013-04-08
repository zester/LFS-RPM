#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
list="binutils-pass-1 gcc-pass-1 linux-api-headers glibc libstdc binutils-pass-2 gcc-pass-2 tcl expect dejagnu check ncurses bash bzip2 coreutils diffutils file findutils gawk gettext grep gzip m4 make patch perl sed tar texinfo xz"
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
		( ./${i}.sh |& tee "LOGS/${i}" ) || die
		echo "Build ---> ${i} completed"
		touch DONE/${i}
	fi
	su -c 'rm -rf /tools/{,share}/{info,man,doc}'
done
