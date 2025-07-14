Summary:	A libxslt plugin providing regexp extension functions
Summary(pl.UTF-8):	Wtyczka libxslt udostępniająca funkcje wyrażeń regularnych
Name:		libxslt-plugin-regexp
Version:	0.5
Release:	0.1
License:	MIT
Group:		Libraries
Source0:	http://home.comcast.net/~joelwreed/%{name}-%{version}.tar.gz
# Source0-md5:	f9e536ad72f2866e726b45770caaf474
Patch0:		%{name}-DESTDIR.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libxslt-devel >= 1.1.13
BuildRequires:	pcre-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		plugindir	%(xslt-config --plugins 2>/dev/null)

%description
A libxslt plugin providing the extension functions regexp:test,
regexp.match, and regexp:replace. This plugin uses PCRE
<http://www.pcre.org/>.

These functions are documented at <http://www.exslt.org/regexp/>.

%description -l pl.UTF-8
Wtyczka libxslt udostępniająca funkcje rozszerzające regexp:test,
regexp.match i regexp.replace. Wykorzystuje PCRE
<http://www.pcre.org/>.

Funkcje są opisane pod adresem <http://www.exslt.org/regexp/>.

%prep
%setup -q
%patch -P0 -p1

%{__sed} -i -e 's,\r$,,' *.xml *.xsl

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	pkglibdir=%{plugindir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.xsl *.xml
%attr(755,root,root) %{plugindir}/exslt_org_regular_expressions.so
