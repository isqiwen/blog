import pynecone as pc

from blog import styles
from blog.templates import webpage
from blog.components.utils import coming_soon


@webpage(path="/cv")
def cv() -> pc.Component:
    """Get the CV page."""
    return pc.box(
        coming_soon("CV")
    )
