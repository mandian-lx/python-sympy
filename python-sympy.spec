%define module	sympy

Summary:	Python library for symbolic mathematics

Name:		python-%{module}
Version:	0.7.5
Release:	1
Source0:	https://github.com/sympy/sympy/releases/download/%{module}-%{version}/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://sympy.googlecode.com/
Requires: 	python-numpy, python-mpmath
Suggests:	python-gmpy >= 1.03, python-pyglet
BuildRequires:	python-sphinx, python-docutils, python-mpmath
BuildArch:	noarch
BuildRequires:  python-devel
BuildRequires:  librsvg

Patch0:		sympy-0.7.5-mpmath.patch

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
    sympy/core/expr.py \
    sympy/core/sets.py \
    sympy/external/tests/test_numpy.py \
    sympy/geometry/ellipse.py \
    sympy/functions/combinatorial/numbers.py \
    sympy/functions/special/bessel.py \
    sympy/functions/special/gamma_functions.py \
    sympy/ntheory/partitions_.py \
    sympy/physics/quantum/constants.py \
    sympy/polys/domains/groundtypes.py \
    sympy/polys/domains/mpelements.py \
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

%patch0 -p1

%install
%__python setup.py install --root=%{buildroot}
%make -C doc html
%__rm -f %{buildroot}%{_bindir}/test %{buildroot}%{_bindir}/doctest %{buildroot}%{_bindir}/py.bench

%clean

%files 
%doc AUTHORS LICENSE examples/ doc/_build/html
%{_bindir}/isympy
%{_mandir}/man1/isympy.*
%dir %{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}/*
%{py_puresitedir}/%{module}-*.egg-info



