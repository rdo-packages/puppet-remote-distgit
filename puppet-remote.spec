%{!?upstream_version: %global upstream_version %{commit}}
Name:           puppet-remote
Version:        v0.0.1
Release:        1%{?alphatag}%{?dist}
Summary:        Remote Puppet Module
License:        Apache-2.0

URL:            https://github.com/paramite/puppet-remote

Source0:        http://github.com/paramite/puppet-remote/archive/%{version}.tar.gz

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
* Fri Sep 16 2016 Haikel Guemar <hguemar@fedoraproject.org> v0.0.1-1.35cc557.git
- Newton update v0.0.1 (35cc5571593d21408d625bd8ee35217345ec502a)

