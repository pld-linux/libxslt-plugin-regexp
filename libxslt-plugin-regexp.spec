Summary:	A libxslt plugin providing regexp extension functions
Name:		libxslt-plugin-regexp
Version:	0.5
Release:	0.1
License:	MIT
Group:		Development/Libraries
Source0:	http://home.comcast.net/~joelwreed/libxslt-plugin-regexp-0.5.tar.gz
# Source0-md5:	f9e536ad72f2866e726b45770caaf474
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
