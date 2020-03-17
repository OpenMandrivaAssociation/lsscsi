Name:		lsscsi
Version:	0.31
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


%changelog
* Fri Feb 24 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.26-1
+ Revision: 780123
- version update 0.26

* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 0.24-1
+ Revision: 645289
- update to new version 0.24

* Mon Aug 23 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.23-1mdv2011.0
+ Revision: 572376
- fix license
- use %%configure2_5x
- correct use of %%buildroot
- update to 0.23
- fix warnings about mixed-use-of-spaces-and-tabs
- cleaning buildroot at install

* Sun May 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2010.0
+ Revision: 373947
- new version

* Fri Jan 23 2009 Jérôme Soyer <saispo@mandriva.org> 0.21-1mdv2009.1
+ Revision: 332762
- New upstream release

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 0.19-4mdv2009.0
+ Revision: 251497
- rebuild

* Thu Jan 03 2008 Olivier Blin <blino@mandriva.org> 0.19-2mdv2008.1
+ Revision: 140933
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

