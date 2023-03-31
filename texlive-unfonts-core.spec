Name:		texlive-unfonts-core
Version:	56291
Release:	2
Summary:	TrueType version of Un-fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/unfonts-core
License:	gpl2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unfonts-core.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unfonts-core.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Un-fonts come from the HLaTeX as type1 fonts in 1998 by
Koaunghi Un, he made type1 fonts to use with Korean TeX
(HLaTeX) in the late 1990's and released it under the GPL
license. They were converted to TrueType with the FontForge
(PfaEdit) by Won-kyu Park in 2003. Core families (9 fonts):
UnBatang, UnBatangBold: serif UnDotum, UnDotumBold: sans-serif
UnGraphic, UnGraphicBold: sans-serif style UnPilgi,
UnPilgiBold: script UnGungseo: cursive, brush-stroke

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/truetype/public/unfonts-core
%doc %{_texmfdistdir}/doc/fonts/unfonts-core

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
