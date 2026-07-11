%global tl_name luaxml
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2c
Release:	%{tl_revision}.1
Summary:	Lua library for reading and serialising XML files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/generic/luaxml
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luaxml.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luaxml.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LuaXML is a pure Lua library for reading and serializing XML files. The
current release is aimed mainly at support for the odsfile package. The
documentation was created by automatic conversion of original
documentation in the source code.

