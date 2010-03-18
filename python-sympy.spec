%define module	sympy
%define name	python-%{module}
%define version	0.6.7
%define release	%mkrel 1

Summary:	Python library for symbolic mathematics
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://sympy.googlecode.com/files/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://sympy.googlecode.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: 	python-numpy
Suggests:	python-gmpy >= 1.03, python-pyglet
BuildRequires:	python-sphinx, python-docutils
BuildArch:	noarch
%py_requires -d

%description
SymPy is a Python library for symbolic mathematics. It aims to become
a full-featured computer algebra system (CAS) while keeping the code
as simple as possible in order to be comprehensible and easily
extensible. SymPy is written entirely in Python and does not require
any external libraries, except optionally for plotting support.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot}
%make -C doc html
%__rm -f %{buildroot}%{_bindir}/test %{buildroot}%{_bindir}/doctest %{buildroot}%{_bindir}/py.bench

%clean
%__rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc AUTHORS README LICENSE TODO examples/ doc/_build/html
%_bindir/isympy
%_mandir/man1/isympy.*
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*
%{py_sitedir}/%{module}-*.egg-info

