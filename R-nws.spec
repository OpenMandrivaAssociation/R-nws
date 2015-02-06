%global packname  nws
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.7.0.1
Release:          3
Summary:          R functions for NetWorkSpaces and Sleigh
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-methods 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods

%description
Provides coordination and parallel execution facilities, as well as
limited cross-language data exchange, using the netWorkSpaces server
developed by REvolution Computing

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/README*
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/bin
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/help


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.7.0.1-1
+ Revision: 774961
- Update to latest version

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.7.0.0-1
+ Revision: 774645
- Import R-nws
- Import R-nws

