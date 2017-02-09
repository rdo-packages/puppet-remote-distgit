%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-remote
%global commit 2d3a47780b95b337b8e84558fe11977ea033d051
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-remote
Version:        0.0.1
Release:        2%{?alphatag}%{?dist}
Summary:        Remote Puppet Module
License:        ASL 2.0

URL:            https://github.com/paramite/puppet-remote

Source0:        http://github.com/paramite/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet >= 2.7.0

%description
This Puppet Module provides types and providers for managing
remote resources.

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/remote/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/remote/



%files
%{_datadir}/openstack-puppet/modules/remote/


%changelog
* Thu Feb 09 2017 Alfredo Moralejo <amoralej@redhat.com> 0.0.1-2.2d3a477git
- Ocata update 0.0.1 (2d3a47780b95b337b8e84558fe11977ea033d051)

