Name:		texlive-luaxml
Version:	72858
Release:	1
Summary:	Lua library for reading and serialising XML files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/generic/luaxml
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaxml.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaxml.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a redistribution of a pure lua xml library, LuaXML. The
library was originally distributed as part of the odsfile
package, but is made available separately in the hope that it
can be useful for other projects.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/luatex/luaxml
%doc %{_texmfdistdir}/doc/luatex/luaxml

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
