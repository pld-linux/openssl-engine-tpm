Summary:	TPM engine for OpenSSL
Summary(pl.UTF-8):	Silnik TPM dla OpenSSL-a
Name:		openssl-engine-tpm
Version:	0.4.2
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/trousers/openssl_tpm_engine-%{version}.tar.gz
# Source0-md5:	5bc8d66399e517dde25ff55ce4c6560f
URL:		http://trousers.sourceforge.net/
BuildRequires:	openssl-devel >= 0.9.8
BuildRequires:	trousers-devel
Requires:	openssl >= 0.9.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir	/%{_lib}

%description
This package contains 2 sets of code, a command-line utility used to
generate a TSS key blob and write it to disk and an OpenSSL engine
which interfaces with the TSS API.

%description -l pl.UTF-8
Ten pakiet składa się z dwóch elementów: narzędzia linii poleceń
służącego do generowania klucza TSS i zapisu go na dysk oraz silnika
OpenSSL, który współpracuje z API TSS.

%prep
%setup -q -n openssl_tpm_engine-%{version}

%build
%configure
	
%{__make} \
	openssl_enginedir=%{_libdir}/engines

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	openssl_enginedir=%{_libdir}/engines

rm -f $RPM_BUILD_ROOT%{_libdir}/engines/libtpm.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README openssl.cnf.sample
%attr(755,root,root) %{_bindir}/create_tpm_key
%attr(755,root,root) %{_libdir}/engines/libtpm.so*
