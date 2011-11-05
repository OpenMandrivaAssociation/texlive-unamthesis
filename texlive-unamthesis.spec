# revision 22500
# category Package
# catalog-ctan /macros/latex/contrib/unamthesis
# catalog-date 2011-05-16 15:49:49 +0200
# catalog-license lppl1.3
# catalog-version 2.01
Name:		texlive-unamthesis
Version:	2.01
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides a customisable format to typeset Theses
according to the Universidad Nacional Autonoma de Mexico
guidelines. Support for use in Scientific Workplace (SWP) 3.x
is also provided. The bundle also includes an appropriate
bibliographic style which enables the use of author-year
schemes using the natbib package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
