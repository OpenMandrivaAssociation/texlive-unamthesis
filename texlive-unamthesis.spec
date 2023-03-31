Name:		texlive-unamthesis
Version:	43639
Release:	2
Summary:	Style for Universidad Nacional Autonoma de Mexico theses
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/unamthesis
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unamthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unamthesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a customisable format to typeset Theses
according to the Universidad Nacional Autonoma de Mexico
guidelines. Support for use in Scientific Workplace (SWP) 3.x
is also provided. The bundle also includes an appropriate
bibliographic style which enables the use of author-year
schemes using the natbib package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/unamthesis
%{_texmfdistdir}/tex/latex/unamthesis
%doc %{_texmfdistdir}/doc/latex/unamthesis

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
