import pygame
from puffkit import PkLayout, PkScene, PkXmlLayoutLoader
from puffkit.color import PkColor
from puffkit.font import PkFont
from puffkit.geometry import PkSize
from puffkit.widget import PkButtonWidget


class _DummyApp:
    """Minimal app stub for layout tests."""

    def __init__(self) -> None:
        """Initialize the stub app with a default font."""
        self.internal_screen_size = PkSize(64, 64)
        self.fonts = {"default": PkFont(None, 12)}


class _ViewModel:
    """View model used for binding and event tests."""

    def __init__(self) -> None:
        """Initialize the view model."""
        self.title = "Hello XML"
        self.clicked = False

    def on_start(self, widget: PkButtonWidget, event: object) -> None:
        """Handle a click from the XML layout."""
        self.clicked = True


def test_xml_layout_binding_and_style() -> None:
    """Load an XML layout with bindings, styles, and events."""
    pygame.init()
    app = _DummyApp()
    scene = PkScene("test", app, lazy=True, auto_unload=False)
    view_model = _ViewModel()

    layout_xml = """
    <Layout id="root" rect="0,0,64,64">
        <Label id="title" rect="0,0,60,20" text="{Binding title}" />
        <Button id="start" rect="0,20,60,20" label="Start" on_click="on_start" style="PrimaryButton" />
    </Layout>
    """

    resources = {"PrimaryButton": {"background_color": "#112233"}}
    loader = PkXmlLayoutLoader(resources=resources)

    layout = loader.load_from_string(scene, layout_xml, view_model=view_model)
    assert isinstance(layout, PkLayout)

    title = layout.get_widget("title")
    assert title.get_text() == "Hello XML"

    button = layout.get_widget("start")
    assert button.action_on_click == view_model.on_start
    assert button.background_color == PkColor.from_value("#112233")
