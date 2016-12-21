Name:           tripleo-ansible-modules
Version:        0.1
Release:        1%{?dist}
Summary:        Ansible modules for TripleO

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://wiki.openstack.org/wiki/TripleO
Source0:        https://github.com/redhat-openstack/tripleo-ansible-modules

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-d2to1
BuildRequires:  python-pbr

Requires: ansible

%description

Tripleo-ansible-modules is a set of Ansible modules for TripleO Openstack
installer. It provide modules for handling the TripleO composable upgrade

%prep
%setup -q


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install 


%files
%doc README*
%license LICENSE



%changelog
