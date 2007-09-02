Summary:	OpenSync Plugin for syncing with Mozilla Calendar / Sunbird
Summary(pl.UTF-8):	Wtyczka OpenSync do synchronizacji z kalendarzem Mozilla Calendar / Sunbird
Name:		libopensync-plugin-sunbird
Version:	0.22
Release:	1
License:	LGPL 2.1
Group:		Libraries
Source0:	http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.bz2?format=raw
# Source0-md5:	c23d0cc6c128831c8a129d0b21aa4fe9
URL:		http://www.opensync.org/
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libopensync-devel >= %{version}
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	neon-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync Plugin for syncing with Mozilla Calendar / Sunbird.

%description -l pl.UTF-8
Wtyczka OpenSync do synchronizacji z kalendarzem Mozilla Calendar /
Sunbird.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/opensync/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/opensync/plugins/sunbird_sync.so
%{_datadir}/opensync/defaults/sunbird-sync
