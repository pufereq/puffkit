Installation
============

puffkit is not yet published on PyPI, so you will need to install it
directly from the source repository.

PDM (recommended)
-----------------

If you want to use puffkit in your project, it is recommended to use
`PDM <https://pdm-project.org/>`_ to manage your dependencies.

.. note::
    If you don't have PDM installed, see the `pdm installation
    guide <https://pdm-project.org/en/latest/#installation>`_.

.. code-block:: bash

    pdm add "puffkit @ git+https://github.com/pufereq/puffkit"

This will add puffkit to your project and allow you to use it in your code.

pip
---

If you prefer to use `pip`, you also need to clone the repository.

.. code-block:: bash

    git clone https://github.com/pufereq/puffkit.git

Then, navigate to the cloned directory:

.. code-block:: bash

    cd puffkit

And install puffkit using pip:

.. code-block:: bash

    pip install .

This will install puffkit and its dependencies system-wide, allowing you to
use it in your projects.

.. note::

    If you are using Linux, you may run into the following error:

    .. code-block:: text

        error: externally-managed-environment

    This is because pip is trying to install puffkit in a system-wide
    environment, which is not allowed by default. To fix this, you can either:

    - Use a virtual environment (recommended)
    - Use the ``--break-system-packages`` flag to allow pip to install
      packages in a system-wide environment, but this is not recommended
      as it can lead to conflicts with system packages.

If you want to use a virtual environment, you can create one using the
`venv <https://docs.python.org/3/library/venv.html>`_ module:

.. code-block:: bash

    python -m venv venv

Then, activate the virtual environment:

.. code-block:: bash

    source venv/bin/activate  # On Linux and macOS
    venv\Scripts\activate     # On Windows

After activating the virtual environment, you can install puffkit using pip as shown above.

