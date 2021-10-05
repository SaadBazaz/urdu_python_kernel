urdu_python_kernel
===========
>> Run UrduPython code in Jupyter Notebook

``urdu_python_kernel`` is a simple wrapper over Jupyter's IPython kernel. It simply translates the code from Urdu to English before passing it on to IPython.

You can learn more about wrapper kernels here:

http://jupyter-client.readthedocs.io/en/latest/wrapperkernels.html

Installation
------------
To install ``urdu_python_kernel`` from this repository::

    git clone <LINK TO THIS REPO>
    cd urdu_python_kernel
    pip install -e .
    python setup.py install
    python -m urdu_python.install

Using the UrduPython kernel
---------------------
**Notebook**: The *New* menu in the notebook should show an option for an UrduPython notebook.

**Console frontends**: To use it with the console frontends, add ``--kernel urdupython`` to
their command line arguments.
