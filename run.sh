PATH=/usr/local/texlive/2021/bin/x86_64-linux:$PATH
PATH=$PATH:/usr/local/texlive/2021/bin/x86_64-linux
export PATH
MANPATH=$MANPATH:/usr/local/texlive/2021/texmf/doc/man
export MANPATH
INFOPATH=$INFOPATH:/usr/local/texlive/2021/texmf/doc/info
export INFOPATH
manim --version
manim -pql graph.py GraphExample