Installation
============

puffkit is not yet published on PyPI, so you will need to install it
directly from the source repository.

Most python depedency managers support installing packages directly
from a Git repository, so you can use the following instead of the
usual PyPI package name:

.. code-block:: text

    git+https://github.com/pufereq/puffkit.git

uv (recommended)
----------------

We recommend using `uv <https://docs.astral.sh/uv/>`_ for managing your project's
dependencies.

.. note::
    If you don't have uv installed, see the `uv installation
    guide <https://docs.astral.sh/uv/getting-started/installation/>`_.

You can add puffkit to your project by running the following command:

.. code-block:: bash

    uv add "git+https://github.com/puferq/puffkit.git"

PDM
---

If you prefer `PDM <https://pdm-project.org/>`_, you can add puffkit to your
project directly from the GitHub repository using the following command:

.. note::
    If you don't have PDM installed, see the `pdm installation
    guide <https://pdm-project.org/en/latest/#installation>`_.

.. code-block:: bash

    pdm add "puffkit @ git+https://github.com/pufereq/puffkit"

This will add puffkit to your project and allow you to use it in your code.

pip
---

You can also install puffkit using `pip <https://pip.pypa.io/en/stable/>`_.
Pip is the default package manager for Python and is included with
most Python installations.

.. code-block:: bash

    pip install "git+https://github.com/pufereq/puffkit.git"

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

