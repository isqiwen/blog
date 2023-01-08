import pynecone as pc

from blog import styles
from blog.templates import webpage
from blog.components.utils import coming_soon


@webpage(path="/tool")
def tool() -> pc.Component:
    """Get the tool page."""
    return pc.box(
        coming_soon("Tool")
    )
