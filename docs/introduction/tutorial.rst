Tutorial
========

In this section, we will guide you through the process of creating your first
app using puffkit. We will create a simple app that displays a window with a
message and a button that closes the app when clicked.

.. note::

    This guide assumes you have basic knowledge of Python and object-oriented
    programming concepts. If you are new to Python, we recommend checking out
    the `Python documentation <https://docs.python.org/3/>`_.

.. note::

    This guide will use the `pdm <https://pdm-project.org/>`_ package manager
    to manage dependencies.

Setting up
----------

First, make sure you have `pdm` installed. If you don't have it yet, refer to
the :ref:`installation guide <introduction/installation:Installation>`

Creating the project
--------------------

Create a new directory for your project and navigate to it:

.. code-block:: bash

    mkdir my_first_app
    cd my_first_app

Next, initialize a new PDM project:

.. code-block:: console

    $ pdm init

Follow the prompts to set up your project. You can accept the defaults or
customize them as needed.

Installing puffkit
------------------

Now, install puffkit as a dependency:

.. code-block:: console

    $ pdm add "puffkit @ git+https://github.com/pufereq/puffkit"

Some theory
-----------

puffkit works with the concept of "containers" and "widgets".

:class:`PkApp <puffkit.app.PkApp>`
    An app is the main entry point of your application. It is responsible for
    initializing the application, creating the main window, and managing the
    event loop. The app can have multiple scenes, which are different
    screens or views within the application.

:class:`PkScene <puffkit.scene.scene.PkScene>`
    A scene is a specific screen or view within your app. It can contain
    various widgets and containers. Scenes can be switched dynamically, allowing
    you to create multi-screen applications. Each scene can have its own layout
    and behavior.

:class:`PkContainer <puffkit.container.PkContainer>`
    A container is a special object that can hold other widgets. It is used to
    organize the layout of your app. Containers can be nested, allowing you to
    create complex layouts with ease.

:class:`PkWidget <puffkit.widget.widget.PkWidget>`
    A widget is a basic building block of your app. It can be a button, label,
    text input, or any other interactive element. Widgets can be added to
    containers to create a user interface. Each widget can have its own
    properties, such as size, position, and appearance.

A simple app structure
----------------------

.. code-block:: text

    +------------------------------------------+
    | App                            _  []  X  |
    +------------------------------------------+
    |+-----------------Scene------------------+|
    ||                                        ||
    || +----Container-----+   +--Container--+ ||
    || |                  |   |             | ||
    || | +----Widget----+ |   |             | ||
    || | |              | |   |             | ||
    || | +--------------+ |   |             | ||
    || |                  |   |             | ||
    || |       +-Widget-+ |   |             | ||
    || |       |        | |   |             | ||
    || |       +--------+ |   |             | ||
    || +------------------+   +-------------+ ||
    ||                                        ||
    |+----------------------------------------+|
    +------------------------------------------+

Creating the app
----------------

Now that we have set up our project, installed puffkit, and learned some theory,
we can start creating our app.

Create a new Python file named `app.py` in your project directory and
open it in your favorite text editor. This file will contain the main code for
your app.

In this file, we will define our app and a scene that contains a label and a
button. The button will print a message to the console when clicked.

Let's start by importing the necessary classes from puffkit:

.. code-block:: python

    from puffkit.app import PkApp
    from puffkit.scene import PkScene
    from puffkit.container import PkContainer
    from puffkit.widget import PkButtonWidget, PkLabelWidget

Next, we will define our app class, which inherits from `PkApp`. This class will
initialize the app.

.. code-block:: python

    class MyFirstApp(PkApp):
        def __init__(self):
            super().__init__(
                app_name="My First App",
                app_version="0.1.0",
                display_size=(800, 600),
                display_arguments={},
                internal_screen_size=(800, 600),
                fps_limit=60,
            )

In the `__init__` method, we call the superclass constructor with the necessary
parameters to set up the app. These parameters include:

- `app_name`: The name of the app.
- `app_version`: The version of the app.
- `display_size`: The size of the window in pixels.
- `display_arguments`: Additional arguments for the display, currently unused.
- `internal_screen_size`: The size of the internal screen, which is the same as
  the display size in this case.
- `fps_limit`: The maximum frames per second for the app, which is set to 60.
  0 means no limit.

.. note::

    Now, you may think what's the difference between `display_size` and
    `internal_screen_size`. The `display_size` is the size of the window that will
    physically appear on the screen, while the `internal_screen_size` is the size of
    the internal screen that the app will use for rendering. This can be useful if
    you want to render at a different resolution than the one displayed on the
    screen, for example, to achieve a retro look.

If you run this code, you will see a window with the title "My First App" and
the specified size. However, it will not do much yet, displaying a blank
checkerboard pattern. If you fiddle with the window, you will see that it
can't be closed, as we haven't set up any event handling yet.

.. note::

    If you want to close the app, you must trigger a ``KeyboardInterrupt``
    (press Ctrl+C in the terminal).

Handling close event
--------------------

To allow the app to be closed properly, we need to handle the "QUIT" event.

We can do this by adding an event handler that will call the `quit()` method of
the app when the event is triggered. This will close the app gracefully.

.. code-block:: python

        self.event_manager.add_handler("QUIT", lambda _: self.quit())

The `event_manager` is responsible for managing events in the app, and
the "QUIT" event is triggered when the user tries to close the window.
The lambda function is needed here, as the `add_handler` method expects
a callable that takes an event (`PkEvent <../ref/modules/puffkit.event.event.html#puffkit.event.event.PkEvent>`_)
as an argument, and we don't need to use the event data in this case.

Next, we will create a scene for our app. A scene is a specific screen or view
within the app, and it can contain various widgets and containers.

We will create a scene class that inherits from `PkScene`.

.. code-block:: python

    class MyFirstScene(PkScene):
        def __init__(self, app: PkApp):
            super().__init__("MyFirstScene", app, lazy=True, auto_unload=True)

In the `__init__` method, we call the superclass constructor with the scene
name, the app instance, and some additional parameters:

- `lazy`: If set to `True`, the scene will not be loaded immediately when added
  to the scene manager. Instead, it will be loaded when it is set as the current
  scene.
- `auto_unload`: If set to `True`, the scene will be automatically unloaded when
  it is no longer the current scene. This can help manage memory usage by
  unloading scenes that are not currently needed.

.. warning::

    Auto unloading scenes can lead to undesirable behavior, especially if you
    have scenes that need to keep their state or if you have widgets that
    reference objects in the scene.

    Use this feature with caution and ensure that your scenes can be safely
    unloaded without losing important data.

Implementing the scene
----------------------

In this state, the scene does not do anything yet. We need to add the
container and widgets to display content in the scene.

The first instinct might be to include the container and widgets in the
`__init__` method, but **WILL** lead to unexpected behavior.

Instead, the `on_load` method should be used to set up the scene when it is
loaded. Let's override the `on_load` method to create a container and add
widgets to it.

.. code-block:: python

    def on_load(self):
        self.container = PkContainer(
            self.app,
            self.surface,
            "MyFirstContainer",
            rect=(10, 10, 780, 580),
        )

        self.container.add_widget(
            PkLabelWidget(
                "MyFirstLabel",
                self.container,
                text="Hello, puffkit!",
                rect=(10, 10, 760, 30),
                text_align="center",
                vertical_align="middle",
            )
        )

        self.container.add_widget(
            PkButtonWidget(
                "MyFirstButton",
                self.container,
                label="Click Me!",
                rect=(10, 50, 200, 40),
                on_click=lambda: print("Button clicked!"),
            )
        )

In the `on_load` method, we create a `PkContainer` instance that will hold our
widgets. The `PkContainer` needs the app instance, the surface to render on,
which usually is the scene's surface, a unique name for the container, and a
rectangle defining its position and size on the screen.

We then add a `PkLabelWidget` and a `PkButtonWidget` to the container. The label
displays a message, and the button has an `on_click` event that prints a message
to the console when clicked. Again we use a lambda function to define the
behavior of the button click, as a bare ``on_click=print("Button clicked!")``
would not work as expected, since the `print` function would be called immediately
instead of being assigned as a callback.

Update and render methods
-------------------------

The layout is set up, but we still need to handle input and rendering in the
scene. We will override the `on_update` and `on_render` methods to handle
input and rendering.

.. code-block:: python

    def on_update(self, delta_time: float):
        self.container.input(**self._input)
        self.container.update(delta_time)

    def on_render(self):
        self.surface.fill("#aaaaaa")
        self.container.render()

In the `on_update` method, we call the `input` method of the container to
process any input events, such as mouse clicks or keyboard presses. We also
call the `update` method of the container to update its state.

In the `on_render` method, we fill the scene's surface with a nice gray
background color to get rid of the default checkerboard pattern, and then we
render the container, which will draw all its widgets on the surface.

Adding the scene to the app
---------------------------

Finally, we need to add the scene to the app's scene manager and set it as the
current scene.

.. code-block:: python

        self.scene_manager.add_scene(MyFirstScene(self))
        self.scene_manager.set_scene("MyFirstScene")

The `add_scene` method adds the scene to the scene manager, and the
`set_scene` method sets it as the current scene, which will trigger the
`on_load` method of the scene, initializing it and displaying it on the screen.

The internal calls differ based on the laziness of the scene.

Lazy scenes
^^^^^^^^^^^

If the scene is lazy, it will be loaded only when it is set as the current scene.
`add_scene` will only add the scene to the scene manager.
When the scene is set as the current scene, the `on_load` method will be called,
and the scene will be initialized.

Non-lazy scenes
^^^^^^^^^^^^^^^

If the scene is not lazy, it will be loaded immediately when added to the scene
manager. The `on_load` method will be called right after the scene is added,
initializing it and displaying it on the screen.
The `set_scene` method will only set the scene as the current scene without
triggering the `on_load` method again.


Final touches
-------------

Now that we have everything set up, we can create an instance of our app and run it.

.. code-block:: python

    if __name__ == "__main__":
        app = MyFirstApp()
        app.run()

Running the app
---------------

To launch your app, you can run the `app.py` file using the PDM environment:

.. code-block:: console

    $ pdm run python app.py


Final code
----------

.. code-block:: python

    from puffkit.app import PkApp
    from puffkit.scene import PkScene
    from puffkit.container import PkContainer
    from puffkit.widget import PkButtonWidget, PkLabelWidget


    class MyFirstApp(PkApp):
        def __init__(self):
            super().__init__(
                app_name="My First App",
                app_version="0.1.0",
                display_size=(800, 600),
                display_arguments={},
                internal_screen_size=(800, 600),
                fps_limit=60,
            )

            self.event_manager.add_handler("QUIT", lambda _: self.quit())

            self.scene_manager.add_scene(MyFirstScene(self))
            self.scene_manager.set_scene("MyFirstScene")


    class MyFirstScene(PkScene):
        def __init__(self, app: PkApp):
            super().__init__("MyFirstScene", app, lazy=True, auto_unload=True)

        def on_load(self):
            self.container = PkContainer(
                self.app,
                self.surface,
                "MyFirstContainer",
                rect=(10, 10, 780, 580),
            )

            self.container.add_widget(
                PkLabelWidget(
                    "MyFirstLabel",
                    self.container,
                    text="Hello, puffkit!",
                    rect=(10, 10, 760, 30),
                    text_align="center",
                    vertical_align="middle",
                )
            )

            self.container.add_widget(
                PkButtonWidget(
                    "MyFirstButton",
                    self.container,
                    label="Click Me!",
                    rect=(10, 50, 200, 40),
                    on_click=lambda: print("Button clicked!"),
                )
            )

        def on_update(self, delta_time: float):
            self.container.input(**self._input)
            self.container.update(delta_time)

        def on_render(self):
            self.surface.fill("#aaaaaa")
            self.container.render()


    if __name__ == "__main__":
        app = MyFirstApp()
        app.run()
