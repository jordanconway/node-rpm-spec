%define ver  0.8.17
%define rel  1
%define jobs 2

Name:          nodejs
Version:       %{ver}
Release:       %{rel}
Summary:       Node.js programs
Group:         Applications/Internet
License:       Copyright Joyent, Inc. and other Node contributors.
URL:           http://nodejs.org

Source0:       http://nodejs.org/dist/node-v%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python >= 2.6, openssl-devel, gcc-c++

Provides: nodejs
Obsoletes: nodejs

%description
Node.js is a server-side JavaScript environment that uses an asynchronous
event-driven model. This allows Node.js to get excellent performance based on
the architectures of many Internet applications.

%prep
%setup -q -n node-v%{version}

%build
export JOBS=%{jobs}
python ./configure --prefix=/usr
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog LICENSE README.md

/usr/bin/node
/usr/bin/npm
/usr/bin/node-waf
/usr/include/node
/usr/share/man/man1/node.1.gz
/usr/lib/node
/usr/lib/node_modules
/usr/lib/dtrace/node.d

%changelog
* Wed Jan 18 2012 Jordan Conway <jordan@jordanconway.com> 0.8.17-1
- RPM using upstream v0.8.16
* Wed Dec 19 2012 Jordan Conway <jordan@jordanconway.com> 0.8.16-1
- RPM using upstream v0.8.16
- Forked spec on github
- Updated changed python26 to python for CentOS 6.3

* Wed Oct 31 2012 Andre von Deetzen <vondeetzen@mgail.com> 0.8.14-1
- RPM using upstream v0.8.14

* Thu Apr 12 2012 Vibol Hou <vibol@hou.cc> 0.6.15-1
- RPM using upstream v0.6.15

* Thu Apr 14 2011 Chris Abernethy <cabernet@chrisabernethy.com> 0.4.6-1
- Initial rpm using upstream v0.4.6
