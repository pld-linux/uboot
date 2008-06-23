Summary:	Das U-Boot -- the Universal Boot Loader
Name:		uboot
Version:	1.3.3
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.denx.de/pub/u-boot/u-boot-%{version}.tar.bz2
# Source0-md5:	6ee26954bb548ad90392cd329ab5cc4c
URL:		http://www.denx.de/wiki/UBoot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Das U-Boot (Universal Bootloader, German for "the submarine") is a
boot loader for a number of different computer architectures,
including PPC, ARM, AVR32, MIPS, x86, 68k, Nios, and MicroBlaze.

%package mkimage
Summary:	Generate kernel image for U-Boot
Group:		Applications/System

%description mkimage
This package contains the mkimage utility, which encapsulates a
compressed "uImage" Linux kerel image with header information, CRC32
checksum, etc, for use with the U-Boot bootloader.

mkimage can also be used to create ramdisk images for use with U-Boot,
either separated from the Linux kernel image, or combined into one
file. mkimage encapsulates the images with a 64 byte header containing
information about target architecture, operating system, image type,
compression method, entry points, time stamp, CRC32 checksums, etc.

%prep
%setup -q -n u-boot-%{version}

%build
touch include/config.mk include/config.h

%{__make} tools \
	HOSTSTRIP=echo \
	BIN_FILES="bmp_logo gen_eth_addr img2srec mkimage"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install tools/mkimage  $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG CHANGELOG-before-U-Boot-1.1.5 CREDITS MAINTAINERS README
# COPYING contains some extra note
%doc COPYING

%files mkimage
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mkimage
