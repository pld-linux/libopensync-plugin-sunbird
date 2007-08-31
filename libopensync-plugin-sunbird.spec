Summary:	OpenSync Plugin for syncing with Mozilla Calendar / Sunbird
Name:		libopensync-plugin-sunbird
Version:	0.22
Release:	1
License:	LGPL 2.1
Group:		Libraries
Source0:	http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.bz2?format=raw
# Source0-md5:	c23d0cc6c128831c8a129d0b21aa4fe9
URL:		http://www.opensync.org/
BuildRequires:	libopensync-devel >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync Plugin for syncing with Mozilla Calendar / Sunbird.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/opensync/plugins/*.so
%{_libdir}/opensync/plugins/*.la
%{_datadir}/opensync/defaults/*
