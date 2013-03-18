#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h			# disable hashall
shopt -s -o pipefail

LFS=/mnt/lfs
groupadd lfs
useradd -s /bin/bash -g lfs -m -k /dev/null lfs
passwd lfs
chown -v lfs:lfs $LFS/tools
chown -v -R lfs:lfs /home/lfs
chown -R -v root.root $LFS/rpmbuild/SOURCES
chown -R -v root.root $LFS/rpmbuild/SPECS

cat > /home/lfs/.bash_profile <<- "EOF"
	exec env -i HOME=$HOME TERM=$TERM PS1='\u:\w\$ ' /bin/bash
EOF

cat > /home/lfs/.bashrc <<- "EOF"
	set +h
	umask 022
	LFS=/mnt/lfs
	LC_ALL=POSIX
	LFS_TGT=$(uname -m)-lfs-linux-gnu
	PATH=/tools/bin:/bin:/usr/bin
	export LFS LC_ALL LFS_TGT PATH
EOF
