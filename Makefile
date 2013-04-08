LFS	:= /mnt/lfs
PART	:= /dev/sdd5
all:
	echo " make [ adduser | clean | install ]"
adduser:
	groupadd lfs
	useradd -s /bin/bash -g lfs -m -k /dev/null lfs
	passwd lfs
	chown -v lfs:lfs $(LFS)/tools
	chown -v -R lfs:lfs /home/lfs
	chown -R -v root.root $(LFS)/rpmbuild/SOURCES
	chown -R -v root.root $(LFS)/rpmbuild/SPECS
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
	touch adduser
	
clean:
	find . -name '*.done'	-delete
	find . -name "*.log"	-delete
	find . -name "*~"	-delete
	find . -name "*.rpm"	-delete
	rpmbuild/SCRIPTS/umount.kernel.filesystem.sh
	# this needs to be rm -rf $lfs/path
	#for i in 'bin boot dev etc home lib lib64 media mnt opt proc root run sbin srv sys tmp usr var'; do
	#	rm -vrf $(LFS)/"${i}" || true
	#done
	rm -rf /tools/*
install:
	mkfs.ext3 $(PART)
	mount $(PART) $(LFS)
	install -vdm 777 $(LFS)/tools
	rm -rf /tools || true
	ln -vs $(LFS)/tools /
	cp -var ../../DEVELOPMENT $(LFS)
	ln -vs /DEVELOPMENT/LFS-RPM.git/rpmbuild $(LFS)
unmount:
	#if [ mountpoint $(LFS)/sys ];	  then umount -v $(LFS)/sys; fi
	#if [ mountpoint $(LFS)/proc ];	  then umount -v $(LFS)/proc fi
	#if [ mountpoint $(LFS)/dev/shm ]; then umount -v $(LFS)/dev/shm fi
	#if [ mountpoint $(LFS)/dev/pts ]; then umount -v $(LFS)/dev/pts fi
	#if [ mountpoint $(LFS)/dev ];	  then umount -v $(LFS)/dev fi

.phony: adduser clean install unmount
