import pynecone as pc

from blog import styles
from blog.templates import webpage
from blog.components.utils import coming_soon


@webpage(path="/about")
def about() -> pc.Component:
    """Get the about page."""
    return pc.box(
        coming_soon("About")
    )
