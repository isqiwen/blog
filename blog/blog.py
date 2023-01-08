
import pynecone as pc

from blog.base_state import State
from blog import styles
from blog.pages import routes


"""The wangqiwen.xyz blog website"""


# from pcweb.pages import routes
# from pcweb.pages.docs.component import multi_docs

# Create the app.
app = pc.App(
    state=State,
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS,
)

# Add the pages to the app.
for route in routes:
    app.add_page(
        route.component,
        route.path,
        route.title,
        description="Write web apps in pure Python. Deploy in minutes.",
        image="preview.png",
    )

# Run the app.
app.compile()
