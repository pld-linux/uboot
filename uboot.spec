Summary:	Das U-Boot -- the Universal Boot Loader
Summary(pl.UTF-8):	Das U-Boot - uniwersalny bootloader
Name:		uboot
Version:	2024.10
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	https://ftp.denx.de/pub/u-boot/u-boot-%{version}.tar.bz2
# Source0-md5:	d83e3cf2e605e5647b6bd93545484d2b
Source1:	https://github.com/hardkernel/u-boot/archive/travis/odroidc4-189/odroid-189.tar.gz
# Source1-md5:	dd117b6180ad5c9abb3303b31e57e7b4
Patch2:		odroid-n2-binutils-2.39.patch
Patch3:		hardkernel-uboot-gcc5.patch
Patch4:		hardkernel-uboot-werror.patch
Patch5:		hardkernel-uboot-arm_cross.patch
Patch6:		hardkernel-uboot-no_stdint.patch
Patch7:		hardkernel-uboot-x86_64_bin.patch
Patch8:		hardkernel-uboot-acs.patch
Patch9:		hardkernel-uboot-uboot_payload.patch
Patch10:	hardkernel-uboot-gcc14.patch
URL:		https://www.denx.de/wiki/U-Boot
BuildRequires:	bison
BuildRequires:	dtc
BuildRequires:	flex
BuildRequires:	gnutls-devel
BuildRequires:	libuuid-devel
BuildRequires:	openssl-devel
BuildRequires:	python3
BuildRequires:	python3-elftools
BuildRequires:	python3-libfdt
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRequires:	rpmbuild(macros) >= 2.007
%ifarch aarch64
BuildRequires:	arm-trusted-firmware-armv8
BuildRequires:	box64
BuildRequires:	crossarm-gcc
BuildRequires:	qemu-user
BuildConflicts:	libfdt-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		common_configs	tools-only

%ifarch %{armv6}
%define		arch_configs	qemu_arm rpi_0_w rpi_2
%endif
%ifarch %{armv7}
%define		arch_configs	qemu_arm rpi_2
%endif
%ifarch aarch64
%define		arch_configs	odroid-n2 pinebook-pro-rk3399 qemu_arm64 rpi_arm64
%endif
%ifarch %{ix86}
%define		arch_configs	qemu-x86
%endif
%ifarch %{x8664}
%define		arch_configs	qemu-x86_64
%endif

%define		configs %{common_configs} %{?arch_configs}

%define		rk3399_configs pinebook-pro-rk3399

%define		imagedir	%{_datadir}/uboot

%description
Das U-Boot (Universal Bootloader, German for "the submarine") is a
boot loader for a number of different computer architectures,
including PPC, ARM, AVR32, MIPS, x86, 68k, Nios, and MicroBlaze.

%description -l pl.UTF-8
Das U-Boot (Universal Bootloader lub "łódź podwodna" po niemiecku) to
bootloader dla wielu różnych architektur komputerów, w tym PPC, ARM,
AVR32, MIPS, x86, 68k, Nios i MicroBlaze.

%package image-odroid-n2
Summary:	U-Boot firmware images for Odroid N2/N2+
Summary(pl.UTF-8):	Obrazy firmware'u U-Boot dla urządzeń Odroid N2/N2+
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description image-odroid-n2
U-Boot firmware images for Odroid N2/N2+.

%description image-odroid-n2 -l pl.UTF-8
Obrazy firmware'u U-Boot dla urządzeń Odroid N2/N2+.

%package image-pinebook-pro
Summary:	U-Boot firmware images for Pinebook Pro
Summary(pl.UTF-8):	Obrazy firmware'u U-Boot dla urządzeń Pinebook Pro
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description image-pinebook-pro
U-Boot firmware images for Pinebook Pro.

%description image-pinebook-pro -l pl.UTF-8
Obrazy firmware'u U-Boot dla urządzeń Pinebook Pro.

%package image-qemu
Summary:	U-Boot firmware images for QEMU
Summary(pl.UTF-8):	Obrazy firmware'u U-Boot dla QEMU
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description image-qemu
U-Boot firmware images for QEMU.

%description image-qemu -l pl.UTF-8
Obrazy firmware'u U-Boot dla QEMU.

%package image-raspberry-pi-arm64
Summary:	U-Boot firmware image for 64-bit Raspberry Pi boards
Summary(pl.UTF-8):	Obrazy firmware'u U-Boot dla 64-bitowych urządzeń Raspberry Pi
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description image-raspberry-pi-arm64
U-Boot firmware image for 64-bit Raspberry Pi boards.

%description image-raspberry-pi-arm64 -l pl.UTF-8
Obrazy firmware'u U-Boot dla 64-bitowych urządzeń Raspberry Pi

%package image-raspberry-pi-2
Summary:	U-Boot firmware image for Raspberry Pi 2
Summary(pl.UTF-8):	Obrazy firmware'u U-Boot dla urządzeń Raspberry Pi 2
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description image-raspberry-pi-2
U-Boot firmware image for Raspberry Pi 2.

%description image-raspberry-pi-2 -l pl.UTF-8
Obrazy firmware'u U-Boot dla urządzeń Raspberry Pi 2.

%package image-raspberry-pi-zero
Summary:	U-Boot firmware image for Raspberry Pi Zero
Summary(pl.UTF-8):	Obrazy firmware'u U-Boot dla urządzeń Raspberry Pi Zero
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description image-raspberry-pi-zero
U-Boot firmware image for Raspberry Pi Zero.

%description image-raspberry-pi-zero -l pl.UTF-8
Obrazy firmware'u U-Boot dla urządzeń Raspberry Pi Zero.

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
wykorzystania przez U-Boota - osobnych w stosunku do obrazu jądra lub
połączonych w jeden plik. mkimage obudowuje obrazy w 64-bajtowy
nagłówek zawierający informacje o architekturze docelowej, systemie
operacyjnym, rodzaju obrazu, metodzie kompresji, punktach wejściowych,
czasie utworzenia, sumach kontrolnych CRC32 itp.

%prep
%setup -q -n u-boot-%{version}
%ifarch aarch64
install -d build/hardkernel-uboot-odroid
tar xf %{SOURCE1} -C build/hardkernel-uboot-odroid
mv build/hardkernel-uboot-odroid/u-boot*/* build/hardkernel-uboot-odroid
cd build/hardkernel-uboot-odroid
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
cd ../..
%endif

%build
for config in %configs; do
	if echo ' %rk3399_configs ' | grep -q " $config "; then
		mkdir -p build/$config
		cp -p /usr/share/arm-trusted-firmware/rk3399/* build/$config
	fi
	%{__make} ${config}_defconfig \
		CC="%{__cc}" \
		HOSTCC="%{__cc}" \
		STRIP=: \
		HOSTCFLAGS="%{rpmcflags}" \
		HOSTLDFLAGS="%{rpmldflags}" \
		V=1 \
		O=build/$config
	%{__make} \
		$(test "$config" = "tools-only" && echo tools-only) \
		CC="%{__cc}" \
		HOSTCC="%{__cc}" \
		DTC=/usr/bin/dtc \
		STRIP=: \
		HOSTCFLAGS="%{rpmcflags}" \
		HOSTLDFLAGS="%{rpmldflags}" \
		V=1 \
		O=build/$config \
		BL31=bl31.elf
done
%ifarch aarch64
cd build/hardkernel-uboot-odroid
%{__make} odroidn2_defconfig \
	V=1
%{__make} \
	CROSS_COMPILE= \
	ARM_CROSS_COMPILE=arm-linux-gnueabi- \
	UBOOT_PAYLOAD=$(pwd)/../odroid-n2/u-boot.bin \
	X86_64_DYNAMIC_WRAPPER=/usr/bin/box64 \
	X86_64_STATIC_WRAPPER=/usr/bin/qemu-x86_64 \
	V=1
cd ../..
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{imagedir}}

for config in %configs; do
	if [ "$config" = "tools-only" ]; then
		install build/$config/tools/mkimage $RPM_BUILD_ROOT%{_bindir}
	elif echo ' %rk3399_configs ' | grep -q " $config "; then
		install -d $RPM_BUILD_ROOT%{imagedir}/$config
		cp -p build/$config/{idbloader.img,u-boot.itb} $RPM_BUILD_ROOT%{imagedir}/$config
	elif [ $config = "odroid-n2" ]; then
		install -d $RPM_BUILD_ROOT%{imagedir}/$config
		cp -p build/hardkernel-uboot-odroid/sd_fuse/u-boot.bin $RPM_BUILD_ROOT%{imagedir}/$config
	else
		install -d $RPM_BUILD_ROOT%{imagedir}/$config
		cp -p build/$config/u-boot.bin $RPM_BUILD_ROOT%{imagedir}/$config
	fi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc MAINTAINERS README
%dir %{imagedir}

%ifarch aarch64
%files image-odroid-n2
%defattr(644,root,root,755)
%{imagedir}/odroid-n2

%files image-pinebook-pro
%defattr(644,root,root,755)
%{imagedir}/pinebook-pro-rk3399

%files image-qemu
%defattr(644,root,root,755)
%{imagedir}/qemu_arm64

%files image-raspberry-pi-arm64
%defattr(644,root,root,755)
%{imagedir}/rpi_arm64
%endif

%ifarch %{armv6} %{armv7}
%files image-qemu
%defattr(644,root,root,755)
%{imagedir}/qemu_arm

%files image-raspberry-pi-2
%defattr(644,root,root,755)
%{imagedir}/rpi_2
%endif

%ifarch %{armv6}
%files image-raspberry-pi-zero
%defattr(644,root,root,755)
%{imagedir}/rpi_0_w
%endif

%ifarch %{ix86}
%files image-qemu
%defattr(644,root,root,755)
%{imagedir}/qemu-x86
%endif

%ifarch %{x8664}
%files image-qemu
%defattr(644,root,root,755)
%{imagedir}/qemu-x86_64
%endif

%files mkimage
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mkimage
