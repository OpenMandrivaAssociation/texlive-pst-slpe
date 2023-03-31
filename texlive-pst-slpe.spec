Name:		texlive-pst-slpe
Version:	24391
Release:	2
Summary:	Sophisticated colour gradients
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-slpe
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-slpe.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-slpe.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-slpe.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This PStricks package covers all the colour gradient
functionality of pst-grad (part of the base pstricks
distribution), and provides the following facilities: - it
permits the user to specify an arbitrary number of colours,
along with the points at which they are to be reached; - it
converts between RGB and HSV behind the scenes; - it provides
concentric and radial gradients; - it provides a command
\psBall that generates bullets with a three-dimensional
appearance; and - uses the xkeyval package for the extended key
handling.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-slpe/pst-slpe.pro
%{_texmfdistdir}/tex/generic/pst-slpe/pst-slpe.tex
%{_texmfdistdir}/tex/latex/pst-slpe/pst-slpe.sty
%doc %{_texmfdistdir}/doc/generic/pst-slpe/Changes
%doc %{_texmfdistdir}/doc/generic/pst-slpe/README
%doc %{_texmfdistdir}/doc/generic/pst-slpe/pst-slpe.pdf
#- source
%doc %{_texmfdistdir}/source/generic/pst-slpe/Makefile
%doc %{_texmfdistdir}/source/generic/pst-slpe/pst-slpe.dtx
%doc %{_texmfdistdir}/source/generic/pst-slpe/pst-slpe.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
