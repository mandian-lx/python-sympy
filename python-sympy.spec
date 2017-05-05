%define module	sympy

Summary:	Python library for symbolic mathematics

Name:		python-%{module}
Version:	1.0
Release:	1
Source0:	https://github.com/sympy/sympy/releases/download/%{module}-%{version}/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://sympy.googlecode.com/
BuildArch:	noarch

BuildRequires:  imagemagick
BuildRequires:  librsvg
BuildRequires:	python-sphinx
BuildRequires:	python-docutils
BuildRequires:  python-devel
BuildRequires:	python-setuptools

Requires: 	python-numpy

%description
SymPy is a Python library for symbolic mathematics. It aims to become
a full-featured computer algebra system (CAS) while keeping the code
as simple as possible in order to be comprehensible and easily
extensible. SymPy is written entirely in Python and does not require
any external libraries, except optionally for plotting support.

%prep
%setup -q -n %{module}-%{version}

%install

%{__python} setup.py install --root=%{buildroot}
mv %{buildroot}%{_bindir}/isympy %{buildroot}%{_bindir}/python2-isympy
mv %{buildroot}%{_mandir}/man1/isympy.1 \
   %{buildroot}%{_mandir}/man1/python2-isympy.1

%{__python} setup.py install --root=%{buildroot}
%make -C doc html
rm -f %{buildroot}%{_bindir}/test %{buildroot}%{_bindir}/doctest %{buildroot}%{_bindir}/py.bench

%files 
%doc AUTHORS LICENSE examples/
%{_bindir}/isympy
%{_mandir}/man1/isympy.*
%dir %{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}/*
%{py_puresitedir}/%{module}-*.egg-info

