%global short_name ordered-set
%global dir_name ordered_set

Name:           python-%{short_name}
Version:        2.0.2
Release:        4%{?dist}
Summary:        A Custom MutableSet that remembers its order

License:        MIT
URL:            https://github.com/LuminosoInsight/ordered-set
Source0:        https://pypi.python.org/packages/source/o/%{short_name}/%{short_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
#test
BuildRequires:  python3-nose

%description
An OrderedSet is a custom MutableSet that remembers its order, so that every\
entry has an index that can be looked up.

%package     -n python3-%{short_name}
Summary:        A Custom MutableSet that remembers its order

%description -n python3-%{short_name}
An OrderedSet is a custom MutableSet that remembers its order, so that every
entry has an index that can be looked up.


%prep
%setup -q -n %{short_name}-%{version}

%build
%py3_build

%install
%py3_install


%check
%{__python3} setup.py nosetests

%files -n python3-%{short_name} 
%doc README
%license MIT-LICENSE
%{python3_sitelib}/%{dir_name}.py
%{python3_sitelib}/*egg-info/
%{python3_sitelib}/__pycache__/*


%changelog
* Tue Jun 05 2018 Petr Viktorin <pviktori@redhat.com> - 2.0.2-4
- Remove the Python 2 subpackage
  https://bugzilla.redhat.com/show_bug.cgi?id=1585973

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Troy Dawson <tdawson@redhat.com> - 2.0.2-2
- Cleanup spec file conditionals

* Mon Aug 21 2017 Miroslav Suchý <msuchy@redhat.com> 2.0.2-1
- add license

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.0-8
- Python 2 binary package renamed to python2-ordered-set
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.0.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Feb 09 2016 Miroslav Suchý <miroslav@suchy.cz> 2.0.0-3
- fix BR condition

* Tue Feb 09 2016 Miroslav Suchý <miroslav@suchy.cz> 2.0.0-2
- add BR python-nose for test

* Tue Feb 09 2016 Miroslav Suchý <miroslav@suchy.cz> 2.0.0-1
- rebase to 2.0.0

* Tue Sep 22 2015 Miroslav Suchý <msuchy@redhat.com> 1.3.1-4
- add missing BR on el6
- add missing macro on el6

* Mon Sep 07 2015 Miroslav Suchý <msuchy@redhat.com> 1.3.1-3
- include egg-info again
- fix typo

* Mon Sep 07 2015 Miroslav Suchý <msuchy@redhat.com> 1.3.1-2
- exclude __pycache__/ from filelist

* Mon Sep 07 2015 Miroslav Suchý <msuchy@redhat.com> 1.3.1-1
- new package

