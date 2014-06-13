# revision 29799
# category Package
# catalog-ctan /macros/latex/contrib/unamthesis
# catalog-date 2013-04-10 00:46:21 +0200
# catalog-license lppl1.3
# catalog-version 2.02
Name:		texlive-unamthesis
Version:	2.02
Release:	6
Summary:	Style for Universidad Nacional Autonoma de Mexico theses
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/unamthesis
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unamthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unamthesis.doc.tar.xz
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
%{_texmfdistdir}/bibtex/bst/unamthesis/UNAMThesis.bst
%{_texmfdistdir}/tex/latex/unamthesis/UNAMThesis.sty
%doc %{_texmfdistdir}/doc/latex/unamthesis/Escudo-IBT.eps
%doc %{_texmfdistdir}/doc/latex/unamthesis/Escudo-IBT.pdf
%doc %{_texmfdistdir}/doc/latex/unamthesis/Escudo-UNAM.eps
%doc %{_texmfdistdir}/doc/latex/unamthesis/Escudo-UNAM.pdf
%doc %{_texmfdistdir}/doc/latex/unamthesis/LEEME
%doc %{_texmfdistdir}/doc/latex/unamthesis/License
%doc %{_texmfdistdir}/doc/latex/unamthesis/README
%doc %{_texmfdistdir}/doc/latex/unamthesis/Thesis-Universidad_Nacional_Autonoma_de_Mexico.shl
%doc %{_texmfdistdir}/doc/latex/unamthesis/UNAMThesis.cst
%doc %{_texmfdistdir}/doc/latex/unamthesis/UNAMThesis.pdf
%doc %{_texmfdistdir}/doc/latex/unamthesis/UNAMThesis.tex
%doc %{_texmfdistdir}/doc/latex/unamthesis/UNAMThesisSWP.tex
%doc %{_texmfdistdir}/doc/latex/unamthesis/testBib.bib

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
