.. radioSphere documentation master file, created by
   sphinx-quickstart on Mon May 24 14:59:01 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to radioSphere's documentation!
=======================================

RadioSphere is a set of tools to process radiographs of spherical particles and find their 3d positions. This is a multi-step process, involving (1) :ref:`Calibration of the geometry and attenuation parameters<Attenuation calibration>`, (2) :ref:`Initial single-pixel precision 3D location with tomopack<Sphere detection>`, and (3) :ref:`Sub-pixel resolution via optimisation<Position optimisation>`. A complete description of the radioSphere technique can be found in a `blog post on Medium
<https://medium.com/@RadioSphere/inside-radiosphere-72159ee0c21d>`_.

You can also `find more information, including presentations and the original journal paper
<https://medium.com/@RadioSphere/4-useful-links-to-delve-into-the-technique-bfd4a3d827ec>`_.

See below for two jupyter notebooks with examples of how radioSphere can be used on real and artifical data:

.. toctree::
   :maxdepth: 1
   
   notebooks/Running radioSphere on artificial data
   notebooks/Running radioSphere on experimental data

The package contains the following modules:

.. toctree::

   modules



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
