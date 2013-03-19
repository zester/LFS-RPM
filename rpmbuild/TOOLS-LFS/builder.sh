#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
_list=(binutils-pass-1 gcc-pass-1 linux-api-headers glibc binutils-pass-2 gcc-pass-2 tcl expect dejagnu check ncurses bash bzip2 coreutils diffutils file findutils gawk gettext grep gzip m4 make patch perl sed tar texinfo xz)
trap 'echo Toolchain build failed...;touch ${FAILURE};exit 1' ERR
for i in ${_list[@]}; do
	[ -f ${FAILURE} ] && (printf "Tool chain: Error exiting script \n";exit 0)
	#pushd "${i}"  > /dev/null 2>&1
	if [ -e ${i}.done ]; then
		echo "${i} --> Already Built"
	else
		[ -e ${i}.log ] && unlink ${i}.log
		echo "Building---> ${i}"
		( ./${i}.sh |& tee "${i}.log" ) || false
		echo "Build ---> ${i} completed"
		touch ${i}.done
	fi
	#popd > /dev/null 2>&1
	rm -rf /tools/{,share}/{info,man,doc}
done
