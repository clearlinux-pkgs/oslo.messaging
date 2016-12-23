#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oslo.messaging
Version  : 5.12.0
Release  : 51
URL      : http://tarballs.openstack.org/oslo.messaging/oslo.messaging-5.12.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.messaging/oslo.messaging-5.12.0.tar.gz
Summary  : Oslo Messaging API
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.messaging-bin
Requires: oslo.messaging-python
BuildRequires : Babel-python
BuildRequires : Jinja2-python
BuildRequires : PyYAML-python
BuildRequires : Pygments-python
BuildRequires : Sphinx-python
BuildRequires : WebOb-python
BuildRequires : aioeventlet-python
BuildRequires : amqp-python
BuildRequires : anyjson-python
BuildRequires : configparser-python
BuildRequires : coverage-python
BuildRequires : debtcollector-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : eventlet-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fasteners-python
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : futures-python
BuildRequires : greenlet-python
BuildRequires : hacking-python
BuildRequires : imagesize-python
BuildRequires : iso8601-python
BuildRequires : kombu-python
BuildRequires : linecache2-python
BuildRequires : markupsafe-python
BuildRequires : mccabe-python
BuildRequires : monotonic-python
BuildRequires : mox3-python
BuildRequires : msgpack-python-python
BuildRequires : netaddr-python
BuildRequires : netifaces-python
BuildRequires : oslo.concurrency-python
BuildRequires : oslo.config-python
BuildRequires : oslo.context-python
BuildRequires : oslo.i18n-python
BuildRequires : oslo.log-python
BuildRequires : oslo.middleware-python
BuildRequires : oslo.serialization-python
BuildRequires : oslo.service-python
BuildRequires : oslo.utils-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pep8-python
BuildRequires : pip
BuildRequires : pyflakes-python
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python-mock
BuildRequires : python-subunit-python
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : pyzmq-python
BuildRequires : qpid-python-python
BuildRequires : redis-python
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : stevedore-python
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testscenarios-python
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : traceback2-python
BuildRequires : trollius-python
BuildRequires : unittest2-python
BuildRequires : wrapt-python

%description
Oslo Messaging Library
======================
.. image:: https://img.shields.io/pypi/v/oslo.messaging.svg
:target: https://pypi.python.org/pypi/oslo.messaging/
:alt: Latest Version

%package bin
Summary: bin components for the oslo.messaging package.
Group: Binaries

%description bin
bin components for the oslo.messaging package.


%package python
Summary: python components for the oslo.messaging package.
Group: Default
Requires: PyYAML-python
Requires: WebOb-python
Requires: amqp-python
Requires: debtcollector-python
Requires: eventlet-python
Requires: futures-python
Requires: greenlet-python
Requires: kombu-python
Requires: monotonic-python
Requires: oslo.context-python
Requires: oslo.i18n-python
Requires: oslo.log-python
Requires: oslo.middleware-python
Requires: oslo.serialization-python
Requires: oslo.service-python
Requires: oslo.utils-python
Requires: six-python

%description python
python components for the oslo.messaging package.


%prep
%setup -q -n oslo.messaging-5.12.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

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
