import pynecone as pc

from blog import styles
from blog.templates import webpage
from blog.components.utils import coming_soon


@webpage(path="/essay")
def essay() -> pc.Component:
    """Get the essay page."""
    return pc.box(
        coming_soon("Essay")
    )
