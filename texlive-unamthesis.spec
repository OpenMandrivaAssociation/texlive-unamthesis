%global tl_name unamthesis
%global tl_revision 43639

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Style for Universidad Nacional Autonoma de Mexico theses
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/unamthesis
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unamthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unamthesis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a customisable format to typeset Theses according
to the Universidad Nacional Autonoma de Mexico guidelines. Support for
use in Scientific Workplace (SWP) 3.x is also provided. The bundle also
includes an appropriate bibliographic style which enables the use of
author-year schemes using the natbib package.

