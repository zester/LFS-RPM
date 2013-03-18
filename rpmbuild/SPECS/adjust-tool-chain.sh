#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
function adjust() {
#	filespec=`dirname $(gcc --print-libgcc-file-name)`/specs
	mv -v /tools/bin/{ld,ld-old}
	mv -v /tools/$(gcc -dumpmachine)/bin/{ld,ld-old}
	mv -v /tools/bin/{ld-new,ld}
	ln -sv /tools/bin/ld /tools/$(gcc -dumpmachine)/bin/ld
	gcc -dumpspecs | sed -e 's@/tools@@g' \
		-e '/\*startfile_prefix_spec:/{n;s@.*@/usr/lib/ @}' \
		-e '/\*cpp:/{n;s@$@ -isystem /usr/include@}' > \
		`dirname $(gcc --print-libgcc-file-name)`/specs
	touch /tools/TOOL.CHAIN.ADJ
}
function test.tool.chain() {
	echo 'main(){}' > dummy.c
	cc dummy.c -v -Wl,--verbose &> dummy.log
	readelf -l a.out | grep ': /lib'
	grep -o '/usr/lib.*/crt[1in].*succeeded' dummy.log
	grep -B1 '^ /usr/include' dummy.log
	grep 'SEARCH.*/usr/lib' dummy.log |sed 's|; |\n|g'
	grep "/lib.*/libc.so.6 " dummy.log
	grep found dummy.log
	rm -v dummy.c a.out dummy.log
}
if [ -e /tools/TOOL.CHAIN.ADJ ]; then
	echo "Tools chain already adjusted --> Skipping"
else
	printf "Adjusting tool chain\n"
	adjust		|& tee "adjust.log"
	test.tool.chain	|& tee "test.log"
fi
