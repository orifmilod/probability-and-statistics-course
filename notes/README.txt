pzccal README
~~~~~~~~~~~~~~

:Date:      2011-03-28
:Copyright: © 2011 Günter Milde <milde@users.berlios.de>

:Licence:   This work may be distributed and/or modified under the
            conditions of the `LaTeX Project Public License`_, either
            version 1.3 of this license or (at your option) any later version.

:Abstract: Set up the Zapf Chancery font as script (calligraphic) math
           alphabet.

           **Obsoleted by the urwchancal_ package.**


Versions
========

:0.1:  2011-02-03  first published version
:0.2:  2011-03-28  documentation update: deprecated by urwchancal_

Introduction
============

The `pzccal` package sets up the Zapf Chancery font (pzcmi7t) as
script (calligraphic) math alphabet ``\mathpzc``. It provides options
to scale the font and to configure the alias command name. By default,
`pzccal` overwrites the predefined math alphabet command ``\mathcal``.

The urwchancal_ package (developed independently and published less
than a month after pzcal.sty) provides not only a style file but also
virtual fonts solving problems with accents and spacing.  Like
`pzcal`, it provides both lowercase and capital Latin math script
letters. It is highly recommended to use ``urwchancal.sty`` instead of
``pzcal.sty``.

Files
=====

====================  =====================================
README.txt            Requirements, Installation, Usage
README.html           browser friendly README

pzccal.sty            literate source (LaTeX package)
pzccal.sty.txt        literate source (Documentation)
pzccal.sty.pdf        literate source (Documentation, PDF)
pzccal.sty.html       literate source (Documentation, HTML)

pzccal-test.tex       Test example (source)
pzccal-test.pdf       Test example (PDF output)
====================  =====================================

The bidirectional text <-> code converter PyLit_ can convert between
``pzccal.sty`` and ``pzccal.sty.txt``.

The Python Docutils_ and pdflatex were used to generate the HTML and PDF
documentation from the reStructuredText_ sources.


Requirements
============

This package uses fonts from the PSNFSS bundle.
It also requires kvoptions_.


Installation
============

* Unpack pzccal.zip (preferably in a TDS_ documentation folder).

* Make sure LaTeX can find pzccal.sty:

  Copy/Move/Link it to a suitable place in the TDS_ and run ``texhash``
  or place it in the current working directory (e.g. for testing).


Usage
=====

It is highly recommended to use urwchancal_::

  \usepackage{urwchancal}

instead of ::

  \usepackage{pzccal}

Option descriptions in the literate source.


.. References
   ==========

.. _LaTeX Project Public License: http://www.latex-project.org/lppl.txt
.. _PyLit: http://pylit.berlios.de
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Docutils: http://docutils.sourceforge.net/rst.html

.. _kvoptions: http://mirror.ctan.org/help/Catalogue/entries/kvoptions.html
.. _urwchancal: http://mirror.ctan.org/help/Catalogue/entries/urwchancal.html

.. _TDS: http://www.tex.ac.uk/cgi-bin/texfaq2html?label=tds
