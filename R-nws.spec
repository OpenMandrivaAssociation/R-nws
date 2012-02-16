%global packname  nws
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.7.0.0
Release:          1
Summary:          R functions for NetWorkSpaces and Sleigh
Group:            Sciences/Mathematics
License:          GPL Version 2 or later
URL:              http://cran.r-project.org/web/packages/nws/index.html
Source0:          http://cran.r-project.org/src/contrib/Archive/nws/nws_1.7.0.0.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-methods 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods

%description
Provides coordination and parallel execution facilities, as well as
limited cross-language data exchange, using the netWorkSpaces server
developed by REvolution Computing.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
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
