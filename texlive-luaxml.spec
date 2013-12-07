# revision 30712
# category Package
# catalog-ctan /macros/luatex/generic/luaxml
# catalog-date 2013-05-27 20:07:27 +0200
# catalog-license other-free
# catalog-version 0.0.2
Name:		texlive-luaxml
Version:	0.0.2
Release:	5
Summary:	Lua library for reading and serialising XML files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/generic/luaxml
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaxml.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaxml.doc.tar.xz
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
%{_texmfdistdir}/tex/luatex/luaxml/luaxml-mod-handler.lua
%{_texmfdistdir}/tex/luatex/luaxml/luaxml-mod-xml.lua
%{_texmfdistdir}/tex/luatex/luaxml/luaxml-selectors.lua
%{_texmfdistdir}/tex/luatex/luaxml/luaxml-stack.lua
%doc %{_texmfdistdir}/doc/luatex/luaxml/README
%doc %{_texmfdistdir}/doc/luatex/luaxml/luaxml.pdf
%doc %{_texmfdistdir}/doc/luatex/luaxml/luaxml.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
