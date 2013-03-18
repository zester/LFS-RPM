#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
sed -i 's|optflags: i386 -O2 -g -march=i386 -mtune=i686|optflags: i386 -O2 -g -march=i486 -mtune=i686 -pipe|'	/usr/lib/rpm/rpmrc
sed -i 's|optflags: i486 -O2 -g -march=i486|optflags: i486 -O2 -g -march=i486 -mtune=generic -pipe|'		/usr/lib/rpm/rpmrc
sed -i 's|optflags: i586 -O2 -g -march=i586|optflags: i586 -O2 -g -march=i586 -mtune=generic -pipe|'		/usr/lib/rpm/rpmrc
sed -i 's|optflags: i686 -O2 -g -march=i686|optflags: i686 -O2 -g -march=i486 -mtune=generic -pipe|'		/usr/lib/rpm/rpmrc
sed -i 's|optflags: athlon -O2 -g -march=athlon|optflags: athlon -O2 -g -march=athlon -mtune=generic -pipe|'	/usr/lib/rpm/rpmrc
