#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB9069B1335700CDC (infra-root@openstack.org)
#
Name     : oslo.messaging
Version  : 5.19.0
Release  : 57
URL      : http://tarballs.openstack.org/oslo.messaging/oslo.messaging-5.19.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.messaging/oslo.messaging-5.19.0.tar.gz
Source99 : http://tarballs.openstack.org/oslo.messaging/oslo.messaging-5.19.0.tar.gz.asc
Summary  : Oslo Messaging API
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.messaging-bin
Requires: oslo.messaging-python
Requires: PyYAML
Requires: WebOb
Requires: amqp
Requires: cachetools
Requires: debtcollector
Requires: futures
Requires: futurist
Requires: kombu
Requires: monotonic
Requires: oslo.config
Requires: oslo.context
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.middleware
Requires: oslo.serialization
Requires: oslo.service
Requires: oslo.utils
Requires: pbr
Requires: pika
Requires: pika-pool
Requires: six
Requires: stevedore
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
========================
Team and repository tags
========================
.. image:: http://governance.openstack.org/badges/oslo.messaging.svg
:target: http://governance.openstack.org/reference/tags/index.html

%package bin
Summary: bin components for the oslo.messaging package.
Group: Binaries

%description bin
bin components for the oslo.messaging package.


%package python
Summary: python components for the oslo.messaging package.
Group: Default

%description python
python components for the oslo.messaging package.


%prep
%setup -q -n oslo.messaging-5.19.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1490883911
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1490883911
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/oslo-messaging-send-notification
/usr/bin/oslo-messaging-zmq-broker
/usr/bin/oslo-messaging-zmq-proxy

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
