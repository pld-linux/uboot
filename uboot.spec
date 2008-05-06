Summary:	Das U-Boot -- the Universal Boot Loader
Name:		uboot
Version:	1.3.2
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.denx.de/pub/u-boot/u-boot-%{version}.tar.bz2
# Source0-md5:	78b1c2722d3907b5fae2cd219dbaf927
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
ln -s ../lib_generic/crc32.c tools

%build
cd tools
%{__cc} %{rpmcflags} -DUSE_HOSTCC -c crc32.c -o crc32.o
%{__cc} %{rpmcflags} -I../include -c mkimage.c -o mkimage.o
%{__cc} %{rpmldflags} -o mkimage crc32.o mkimage.o

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
