Name:           libnetfilter_cthelper
Version:        1.0.0
Release:        8%{?dist}
Summary:        User-space infrastructure for connection tracking helpers
Group:          System Environment/Libraries
License:        GPLv2
URL:            http://www.netfilter.org/projects/libnetfilter_cthelper/index.html
Source0:        http://www.netfilter.org/projects/libnetfilter_cthelper/files/libnetfilter_cthelper-%{version}.tar.bz2
BuildRequires:  libmnl-devel >= 1.0.0, pkgconfig, kernel-headers

%description
This library provides the infrastructure for the user-space helper
infrastructure available since the Linux kernel 3.6.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libmnl-devel >= 1.0.0
Requires:       kernel-headers

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -type f -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc COPYING README
%{_libdir}/*.so.*

%files devel
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/libnetfilter_cthelper
%{_includedir}/libnetfilter_cthelper/*.h
%{_libdir}/*.so

%changelog
* Wed Oct 14 2015 Paul Wouters <pwouters@redhat.com> - 1.0.0-8
- Resolves: rhbz#1233222 (do not include examples/ as these become arch specific)

* Wed Jun 10 2015 Paul Wouters <pwouters@redhat.com> - 1.0.0-7
- Resolves: rhbz#1233222 Add libnetfilter_cthelper package to RHEL-7
