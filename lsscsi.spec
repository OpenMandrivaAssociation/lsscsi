Name:		lsscsi
Version:	0.23
Release:	%mkrel 1
License:	GPLv2
Group:		System/Kernel and hardware
Summary:	List SCSI devices (or hosts) and associated information
Url:		http://sg.danny.cz/scsi/lsscsi.html
Source0:	http://sg.danny.cz/scsi/%{name}-%{version}.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Uses information provided by the sysfs pseudo file system in Linux kernel
2.6 series to list SCSI devices or all SCSI hosts. Includes a "classic"
option to mimic the output of "cat /proc/scsi/scsi" that has been widely
used prior to the lk 2.6 series.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc ChangeLog INSTALL README CREDITS AUTHORS COPYING
%attr(0755,root,root) %{_bindir}/*
%{_mandir}/man8/*
