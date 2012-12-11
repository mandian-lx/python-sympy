%define module	sympy
%define name	python-%{module}
%define version	0.7.1
%define release	%mkrel 2

Summary:	Python library for symbolic mathematics
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://sympy.googlecode.com/files/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://sympy.googlecode.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: 	python-numpy, python-mpmath
Suggests:	python-gmpy >= 1.03, python-pyglet
BuildRequires:	python-sphinx, python-docutils, python-mpmath
BuildArch:	noarch
%py_requires -d

# http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/dev-python/sympy/files/sympy-0.7.1-mpmath.patch?revision=1.1
Patch0:		sympy-0.7.1-mpmath.patch

%description
SymPy is a Python library for symbolic mathematics. It aims to become
a full-featured computer algebra system (CAS) while keeping the code
as simple as possible in order to be comprehensible and easily
extensible. SymPy is written entirely in Python and does not require
any external libraries, except optionally for plotting support.

%prep
%setup -q -n %{module}-%{version}

# Use python-mpmath package
# http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/dev-python/sympy/sympy-0.7.1.ebuild?revision=1.2&view=markup
rm -rf sympy/mpmath/*
sed -i \
    -e "s:sympy\.mpmath:mpmath:g" \
    -e "s:from sympy import mpmath:import mpmath:g" \
    sympy/core/function.py \
    sympy/core/numbers.py \
    sympy/core/tests/test_sets.py \
    sympy/core/tests/test_evalf.py \
    sympy/core/tests/test_sympify.py \
    sympy/core/tests/test_numbers.py \
    sympy/core/power.py \
    sympy/core/evalf.py \
    sympy/core/sets.py \
    sympy/external/tests/test_numpy.py \
    sympy/functions/combinatorial/numbers.py \
    sympy/functions/special/bessel.py \
    sympy/functions/special/gamma_functions.py \
    sympy/ntheory/partitions_.py \
    sympy/physics/quantum/constants.py \
    sympy/polys/domains/groundtypes.py \
    sympy/polys/numberfields.py \
    sympy/polys/rootoftools.py \
    sympy/polys/polytools.py \
    sympy/printing/repr.py \
    sympy/printing/str.py \
    sympy/printing/latex.py \
    sympy/simplify/simplify.py \
    sympy/solvers/solvers.py \
    sympy/solvers/tests/test_numeric.py \
    sympy/statistics/distributions.py \
    sympy/statistics/tests/test_statistics.py \
    sympy/utilities/lambdify.py \
    sympy/utilities/tests/test_lambdify.py \
    || exit 1

%patch0 -p0

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



%changelog
* Tue Nov 08 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.7.1-2mdv2012.0
+ Revision: 729011
- Import gentoo patch to use external python-mpmath.

* Sun Jul 31 2011 Lev Givon <lev@mandriva.org> 0.7.1-1
+ Revision: 692497
- Update to 0.7.1.

* Tue Jun 28 2011 Lev Givon <lev@mandriva.org> 0.7.0-1
+ Revision: 687772
- Update to 0.7.0.

* Wed Nov 03 2010 Paulo Andrade <pcpa@mandriva.com.br> 0.6.7-2mdv2011.0
+ Revision: 593036
+ rebuild (emptylog)

* Thu Mar 18 2010 Lev Givon <lev@mandriva.org> 0.6.7-1mdv2010.1
+ Revision: 524789
- Update to 0.6.7.

* Mon Dec 21 2009 Lev Givon <lev@mandriva.org> 0.6.6-1mdv2010.1
+ Revision: 480821
- Update to 0.6.6.
  Build and include docs.

* Sat Jul 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.5-1mdv2010.0
+ Revision: 397068
- update to new version 0.6.5

* Sun Apr 05 2009 Lev Givon <lev@mandriva.org> 0.6.4-1mdv2009.1
+ Revision: 364174
- Update to 0.6.4.

* Thu Nov 20 2008 Lev Givon <lev@mandriva.org> 0.6.3-1mdv2009.1
+ Revision: 305300
- Update to 0.6.3.

* Sun Aug 24 2008 Lev Givon <lev@mandriva.org> 0.6.2-1mdv2009.0
+ Revision: 275521
- Update to 0.6.2.

* Wed Jul 23 2008 Lev Givon <lev@mandriva.org> 0.6.1-1mdv2009.0
+ Revision: 243813
- Update to 0.6.1.

* Fri Jul 11 2008 Lev Givon <lev@mandriva.org> 0.6.0-1mdv2009.0
+ Revision: 233907
- Update to 0.6.0.

* Sun May 25 2008 Lev Givon <lev@mandriva.org> 0.5.15-1mdv2009.0
+ Revision: 211252
- Update to 0.5.15.
- Update to 0.5.14.

* Fri Mar 07 2008 Lev Givon <lev@mandriva.org> 0.5.13-1mdv2008.1
+ Revision: 181392
- Update to 0.5.13.

* Mon Jan 28 2008 Lev Givon <lev@mandriva.org> 0.5.12-1mdv2008.1
+ Revision: 159158
- Update to 0.5.12.

* Wed Jan 09 2008 Lev Givon <lev@mandriva.org> 0.5.11-1mdv2008.1
+ Revision: 147008
- Update to 0.5.11.

* Mon Dec 24 2007 Lev Givon <lev@mandriva.org> 0.5.9-1mdv2008.1
+ Revision: 137572
- Update to 0.5.9.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Dec 07 2007 Lev Givon <lev@mandriva.org> 0.5.8-1mdv2008.1
+ Revision: 116294
- Update to 0.5.8.

* Sun Nov 18 2007 Lev Givon <lev@mandriva.org> 0.5.7-1mdv2008.1
+ Revision: 109762
- Update to 0.5.7.

* Wed Nov 07 2007 Lev Givon <lev@mandriva.org> 0.5.6-1mdv2008.1
+ Revision: 106758
- import python-sympy


* Sun Nov 4 2007 Lev Givon <lev@mandriva.org> 0.5.6-1mdv2008.0
- Package for Mandriva.
