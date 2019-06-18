#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xFC43F0EE211DFED8 (infra-root@openstack.org)
#
Name     : oslo.messaging
Version  : 9.7.2
Release  : 84
URL      : https://tarballs.openstack.org/oslo.messaging/oslo.messaging-9.7.2.tar.gz
Source0  : https://tarballs.openstack.org/oslo.messaging/oslo.messaging-9.7.2.tar.gz
Source99 : https://tarballs.openstack.org/oslo.messaging/oslo.messaging-9.7.2.tar.gz.asc
Summary  : Oslo Messaging API
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.messaging-bin = %{version}-%{release}
Requires: oslo.messaging-license = %{version}-%{release}
Requires: oslo.messaging-python = %{version}-%{release}
Requires: oslo.messaging-python3 = %{version}-%{release}
Requires: PyYAML
Requires: WebOb
Requires: amqp
Requires: cachetools
Requires: debtcollector
Requires: futurist
Requires: kombu
Requires: monotonic
Requires: oslo.config
Requires: oslo.log
Requires: oslo.middleware
Requires: oslo.serialization
Requires: oslo.service
Requires: oslo.utils
Requires: pbr
Requires: six
Requires: stevedore
BuildRequires : PyYAML
BuildRequires : WebOb
BuildRequires : amqp
BuildRequires : buildreq-distutils3
BuildRequires : cachetools
BuildRequires : debtcollector
BuildRequires : futurist
BuildRequires : kombu
BuildRequires : monotonic
BuildRequires : oslo.config
BuildRequires : oslo.log
BuildRequires : oslo.middleware
BuildRequires : oslo.serialization
BuildRequires : oslo.service
BuildRequires : oslo.utils
BuildRequires : pbr
BuildRequires : six
BuildRequires : stevedore

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/oslo.messaging.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

%package bin
Summary: bin components for the oslo.messaging package.
Group: Binaries
Requires: oslo.messaging-license = %{version}-%{release}

%description bin
bin components for the oslo.messaging package.


%package license
Summary: license components for the oslo.messaging package.
Group: Default

%description license
license components for the oslo.messaging package.


%package python
Summary: python components for the oslo.messaging package.
Group: Default
Requires: oslo.messaging-python3 = %{version}-%{release}

%description python
python components for the oslo.messaging package.


%package python3
Summary: python3 components for the oslo.messaging package.
Group: Default
Requires: python3-core

%description python3
python3 components for the oslo.messaging package.


%prep
%setup -q -n oslo.messaging-9.7.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1560866815
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oslo.messaging
cp LICENSE %{buildroot}/usr/share/package-licenses/oslo.messaging/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/oslo-messaging-send-notification

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oslo.messaging/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
