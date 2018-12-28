#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : oslo.messaging
Version  : 9.3.0
Release  : 75
URL      : https://tarballs.openstack.org/oslo.messaging/oslo.messaging-9.3.0.tar.gz
Source0  : https://tarballs.openstack.org/oslo.messaging/oslo.messaging-9.3.0.tar.gz
Source99 : https://tarballs.openstack.org/oslo.messaging/oslo.messaging-9.3.0.tar.gz.asc
Summary  : Oslo Messaging API
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.messaging-bin = %{version}-%{release}
Requires: oslo.messaging-license = %{version}-%{release}
Requires: oslo.messaging-python = %{version}-%{release}
Requires: oslo.messaging-python3 = %{version}-%{release}
Requires: PyYAML
Requires: Sphinx
Requires: WebOb
Requires: amqp
Requires: cachetools
Requires: debtcollector
Requires: fixtures
Requires: futurist
Requires: kombu
Requires: monotonic
Requires: openstackdocstheme
Requires: oslo.config
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.middleware
Requires: oslo.serialization
Requires: oslo.service
Requires: oslo.utils
Requires: pbr
Requires: reno
Requires: six
Requires: stevedore
Requires: tenacity
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
Team and repository tags
        ========================

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
%setup -q -n oslo.messaging-9.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1544544146
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
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
