Name:		lsscsi
Version:	0.26
Release:	1
License:	GPLv2
Group:		System/Kernel and hardware
Summary:	List SCSI devices (or hosts) and associated information
Url:		http://sg.danny.cz/scsi/lsscsi.html
Source0:	http://sg.danny.cz/scsi/%{name}-%{version}.tgz

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
%makeinstall

%files
%defattr(-,root,root)
%doc ChangeLog INSTALL README CREDITS AUTHORS COPYING
%attr(0755,root,root) %{_bindir}/*
%{_mandir}/man8/*
