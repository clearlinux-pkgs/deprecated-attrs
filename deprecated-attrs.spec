#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xAE2536227F69F181 (hs@ox.cx)
#
Name     : deprecated-attrs
Version  : 18.2.0
Release  : 32
URL      : https://files.pythonhosted.org/packages/0f/9e/26b1d194aab960063b266170e53c39f73ea0d0d3f5ce23313e0ec8ee9bdf/attrs-18.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/0f/9e/26b1d194aab960063b266170e53c39f73ea0d0d3f5ce23313e0ec8ee9bdf/attrs-18.2.0.tar.gz
Source99 : https://files.pythonhosted.org/packages/0f/9e/26b1d194aab960063b266170e53c39f73ea0d0d3f5ce23313e0ec8ee9bdf/attrs-18.2.0.tar.gz.asc
Summary  : Classes Without Boilerplate
Group    : Development/Tools
License  : MIT
Requires: deprecated-attrs-license = %{version}-%{release}
Requires: deprecated-attrs-python = %{version}-%{release}
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-core
BuildRequires : setuptools-legacypython
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://www.attrs.org/en/latest/_static/attrs_logo.png
:alt: attrs Logo

%package legacypython
Summary: legacypython components for the deprecated-attrs package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the deprecated-attrs package.


%package license
Summary: license components for the deprecated-attrs package.
Group: Default

%description license
license components for the deprecated-attrs package.


%package python
Summary: python components for the deprecated-attrs package.
Group: Default

%description python
python components for the deprecated-attrs package.


%prep
%setup -q -n attrs-18.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554305643
export MAKEFLAGS=%{?_smp_mflags}
python2 setup.py build -b py2

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/deprecated-attrs
cp LICENSE %{buildroot}/usr/share/package-licenses/deprecated-attrs/LICENSE
cp docs/license.rst %{buildroot}/usr/share/package-licenses/deprecated-attrs/docs_license.rst
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/deprecated-attrs/LICENSE
/usr/share/package-licenses/deprecated-attrs/docs_license.rst

%files python
%defattr(-,root,root,-)
