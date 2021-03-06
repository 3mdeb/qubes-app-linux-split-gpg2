Name:           split-gpg2-dom0
Version:        0.1
Release:        1%{dist}
Summary:        split-gpg2 Qubes RPC Policy for dom0

Group:          Qubes
License:        GPLv2+

Source:         .

%define _builddir %(pwd)

%description
split-gpg2 allows you to run the gpg2 client in a different Qubes-Domain than
the gpg-agent.

This package contains the Qubes RPC policy for split-gpg2.

%prep

%build

%install
install -D qubes.Gpg2.policy $RPM_BUILD_ROOT/etc/qubes-rpc/policy/qubes.Gpg2

%post

%preun

%files
%config(noreplace) %attr(0664,root,qubes) /etc/qubes-rpc/policy/qubes.Gpg2
