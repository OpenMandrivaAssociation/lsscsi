%define name    lsscsi
%define version 0.19
%define release %mkrel 2

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License:	GPL
Group:		System/Kernel and hardware
Summary: 	List SCSI devices (or hosts) and associated information
Source0:	http://www.torque.net/scsi/%{name}-%{version}.tgz
Url:		http://www.torque.net/scsi/lsscsi.html
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Uses information provided by the sysfs pseudo file system in Linux kernel
2.6 series to list SCSI devices or all SCSI hosts. Includes a "classic"
option to mimic the output of "cat /proc/scsi/scsi" that has been widely
used prior to the lk 2.6 series.

%prep
%setup -q

%build

%configure 
%make

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog INSTALL README CREDITS AUTHORS COPYING
%attr(0755,root,root) %{_bindir}/*
%{_mandir}/man8/*




