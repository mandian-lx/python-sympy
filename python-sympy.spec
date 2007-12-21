%define module sympy
%define name python-%{module}
%define version 0.5.8
%define release %mkrel 1

Summary: Python library for symbolic mathematics
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{module}-%{version}.tar.bz2
License: BSD
Group: Development/Python
Url: http://code.google.com/p/sympy/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: python-devel

%description
SymPy is a Python library for symbolic mathematics. It aims to become
a full-featured computer algebra system (CAS) while keeping the code
as simple as possible in order to be comprehensible and easily
extensible. SymPy is written entirely in Python and does not require
any external libraries, except optionally for plotting support.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%__python setup.py install --root=%{buildroot} --record=INSTALLED_FILES
%__sed -ie 's/isympy\.1/isympy\.1\.lzma/' INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README LICENSE TODO examples/

