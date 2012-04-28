%define gemname sprockets

Summary:	Sprockets is a Rack-based asset packaging system
Name:		ruby-%{gemname}2.1
Version:	2.1.3
Release:	1
Source0:	http://rubygems.org/downloads/%{gemname}-%{version}.gem
License:	MIT
Group:		System/Servers
Url:		http://www.rubyonrails.org/
BuildArch:	noarch
BuildRequires:	ruby-RubyGems
#Provides:       rubygem(%{gemname}) = %{version}

%description
Sprockets is a Rack-based asset packaging system that concatenates 
and serves JavaScript, CoffeeScript, CSS, LESS, Sass, and SCSS.

%prep
%setup -c

%build

%install
gem install -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/cache

%files
%defattr(-,root,root)
%{ruby_gemdir}/gems/%{gemname}-%{version}
%{ruby_gemdir}/specifications/%{gemname}-%{version}.gemspec
%doc %{ruby_gemdir}/doc/%{gemname}-%{version}
