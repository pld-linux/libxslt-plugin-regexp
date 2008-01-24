Summary:	A libxslt plugin providing regexp extension functions
Name:		libxslt-plugin-regexp
Version:	0.3
Release:	0.2
License:	MIT
Group:		Development/Libraries
Source0:	ftp://xmlsoft.org/libxml2/plugins/%{name}-%{version}.tar.gz
# Source0-md5:	7e394d4b6cb1d51d91e14d3fbac78cb7
BuildRequires:	libxslt-devel >= 1.1.13
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		plugindir	%(xslt-config --plugins 2>/dev/null)

%description
A libxslt plugin providing the extension functions regexp:test,
regexp.match, and regexp:replace. This plugin uses PCRE
<http://www.pcre.org>.

These functions are documented at <http://www.exslt.org/regexp/>.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	pkglibdir=%{plugindir} \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{plugindir}/exslt_org_regular_expressions.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{plugindir}/exslt_org_regular_expressions.so
