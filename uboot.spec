Summary:	Das U-Boot -- the Universal Boot Loader
Summary(pl.UTF-8):	Das U-Boot - uniwersalny bootloader
Name:		uboot
Version:	2021.07
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	https://ftp.denx.de/pub/u-boot/u-boot-%{version}.tar.bz2
# Source0-md5:	7afbe0ef070dc0e8e970c57a08e3f336
Patch0:		rpi-Enable-using-the-DT-provided-by-the-Raspberry-Pi.patch
Patch1:		%{name}-pbp_usb_hang.patch
URL:		https://www.denx.de/wiki/U-Boot
%ifarch aarch64
BuildRequires:	arm-trusted-firmware-armv8
%endif
BuildRequires:	bison
BuildRequires:	dtc
BuildRequires:	flex
BuildRequires:	openssl-devel
BuildRequires:	rpmbuild(macros) >= 2.007
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		common_configs	tools-only

%ifarch %{armv6}
%define		arch_configs	rpi_0_w rpi_2
%endif
%ifarch %{armv7}
%define		arch_configs	rpi_2
%endif
%ifarch aarch64
%define		arch_configs	pinebook-pro-rk3399
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

%package image-pinebook-pro
Summary:	U-Boot firmware images for Pinebook Pro
Summary(pl.UTF-8):	Obrazy firmware'u U-Boot dla urządzeń Pinebook Pro
Group:		Applications/System

%description image-pinebook-pro
U-Boot firmware images for Pinebook Pro.

%description image-pinebook-pro -l pl.UTF-8
Obrazy firmware'u U-Boot dla urządzeń Pinebook Pro.

%package image-raspberry-pi-2
Summary:	U-Boot firmware image for Raspberry Pi 2
Summary(pl.UTF-8):	Obrazy firmware'u U-Boot dla urządzeń Raspberry Pi 2
Group:		Applications/System

%description image-raspberry-pi-2
U-Boot firmware image for Raspberry Pi 2.

%description image-raspberry-pi-2 -l pl.UTF-8
Obrazy firmware'u U-Boot dla urządzeń Raspberry Pi 2.

%package image-raspberry-pi-zero
Summary:	U-Boot firmware image for Raspberry Pi Zero
Summary(pl.UTF-8):	Obrazy firmware'u U-Boot dla urządzeń Raspberry Pi Zero
Group:		Applications/System

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
%ifarch %{arm} aarch64
%patch0 -p1
%endif
%ifarch aarch64
%patch1 -p1
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
		STRIP=: \
		HOSTCFLAGS="%{rpmcflags}" \
		HOSTLDFLAGS="%{rpmldflags}" \
		V=1 \
		O=build/$config
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{imagedir}}

for config in %configs; do
	if [ "$config" = "tools-only" ]; then
		install build/$config/tools/mkimage $RPM_BUILD_ROOT%{_bindir}
	elif echo ' %rk3399_configs ' | grep -q " $config "; then
		install -d $RPM_BUILD_ROOT%{imagedir}/$config
		cp -p build/$config/{idbloader.img,u-boot.itb} $RPM_BUILD_ROOT%{imagedir}/$config
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
%files image-pinebook-pro
%defattr(644,root,root,755)
%{imagedir}/pinebook-pro-rk3399
%endif

%ifarch %{armv6} %{armv7}
%files image-raspberry-pi-2
%defattr(644,root,root,755)
%{imagedir}/rpi_2
%endif

%ifarch %{armv6}
%files image-raspberry-pi-zero
%defattr(644,root,root,755)
%{imagedir}/rpi_0_w
%endif

%files mkimage
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mkimage
