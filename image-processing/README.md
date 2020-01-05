Installation
============

Warnings
--------

.. warning:: Pillow and PIL cannot co-exist in the same environment. Before installing Pillow, please uninstall PIL.

.. warning:: Pillow >= 1.0 no longer supports "import Image". Please use "from PIL import Image" instead.

.. warning:: Pillow >= 2.1.0 no longer supports "import _imaging". Please use "from PIL.Image import core as _imaging" instead.

Basic Installation
------------------

.. note::

    The following instructions will install Pillow with support for
    most common image formats. See :ref:`external-libraries` for a
    full list of external libraries supported.

Install Pillow with :command:`pip`::

    python -m pip install pip
    python -m pip install Pillow or pip3 install pillow


Windows Installation
^^^^^^^^^^^^^^^^^^^^

We provide Pillow binaries for Windows compiled for the matrix of
supported Pythons in both 32 and 64-bit versions in wheel, egg, and
executable installers. These binaries have all of the optional
libraries included except for raqm and libimagequant::

    python -m pip install pip
    python -m pip install Pillow


macOS Installation
^^^^^^^^^^^^^^^^^^

We provide binaries for macOS for each of the supported Python
versions in the wheel format. These include support for all optional
libraries except libimagequant.  Raqm support requires libraqm,
fribidi, and harfbuzz to be installed separately::

    python -m pip install pip
    python -m pip install Pillow

Linux Installation
^^^^^^^^^^^^^^^^^^

We provide binaries for Linux for each of the supported Python
versions in the manylinux wheel format. These include support for all
optional libraries except libimagequant. Raqm support requires
libraqm, fribidi, and harfbuzz to be installed separately::

    python -m pip install pip
    python -m pip install Pillow

Most major Linux distributions, including Fedora, Debian/Ubuntu and
ArchLinux also include Pillow in packages that previously contained
PIL e.g. ``python-imaging``.

Using with CMD
------------------
### For Python 3 version -

In this project folder, open CMD and run :
```python3 JPGtoPNG.py stock/ anyfolder/```
