%global tl_name pst-slpe
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.31
Release:	%{tl_revision}.1
Summary:	Sophisticated colour gradients
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-slpe
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-slpe.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-slpe.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-slpe.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This PStricks package covers all the colour gradient functionality of
pst-grad (part of the base PSTricks distribution), and provides the
following facilities: it permits the user to specify an arbitrary number
of colours, along with the points at which they are to be reached; it
converts between RGB and HSV behind the scenes; it provides concentric
and radial gradients; it provides a command \psBall that generates
bullets with a three-dimensional appearance; and uses the xkeyval
package for the extended key handling.

