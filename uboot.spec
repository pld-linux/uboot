Summary:	Das U-Boot -- the Universal Boot Loader
Summary(pl.UTF-8):	Das U-Boot - uniwersalny bootloader
Name:		uboot
Version:	2013.07
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	ftp://ftp.denx.de/pub/u-boot/u-boot-%{version}.tar.bz2
# Source0-md5:	8445162690052e6afd4b8f87af2bb557
URL:		http://www.denx.de/wiki/U-Boot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Das U-Boot (Universal Bootloader, German for "the submarine") is a
boot loader for a number of different computer architectures,
including PPC, ARM, AVR32, MIPS, x86, 68k, Nios, and MicroBlaze.

%description -l pl.UTF-8
Das U-Boot (Universal Bootloader lub "łódź podwodna" po niemiecku) to
bootloader dla wielu różnych architektur komputerów, w tym PPC, ARM,
AVR32, MIPS, x86, 68k, Nios i MicroBlaze.

%package mkimage
Summary:	Generate kernel image for U-Boot
Summary(pl.UTF-8):	Generowanie obrazu jądra dla U-Boota
Group:		Applications/System

%description mkimage
This package contains the mkimage utility, which encapsulates a
compressed "uImage" Linux kernel image with header information, CRC32
checksum, etc., for use with the U-Boot bootloader.

mkimage can also be used to create ramdisk images for use with U-Boot,
either separated from the Linux kernel image, or combined into one
file. mkimage encapsulates the images with a 64 byte header containing
information about target architecture, operating system, image type,
compression method, entry points, time stamp, CRC32 checksums, etc.

%description mkimage -l pl.UTF-8
Ten pakiet zawiera narzędzie mkimage, łączące skompresowany obraz
jądra Linuksa "uImage" w nagłówkiem, sumą kontrolną CRC32 itp. do
wykorzystania przez bootloader U-Boot.

mkimage może być używane także do tworzenia obrazów ramdysków do
wykorzystania przez U-Boota - osobnych w stosunku do obrazu jądra
lub połączonych w jeden plik. mkimage obudowuje obrazy w 64-bajtowy
nagłówek zawierający informacje o architekturze docelowej, systemie
operacyjnym, rodzaju obrazu, metodzie kompresji, punktach wejściowych,
czasie utworzenia, sumach kontrolnych CRC32 itp.

%prep
%setup -q -n u-boot-%{version}

%build
%{__make} tools \
	HOSTCC="%{__cc}" \
	HOSTSTRIP=: \
	HOST_CFLAGS="%{rpmcflags}" \
	HOST_LDFLAGS="%{rpmldflags}" \
	BIN_FILES="bmp_logo gen_eth_addr img2srec mkimage"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install tools/mkimage $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING contains some extra note
%doc COPYING CREDITS MAINTAINERS README

%files mkimage
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mkimage
