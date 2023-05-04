"""The wangqiwen.xyz blog website"""


import pynecone as pc

from blog import styles
from blog.base_state import State
from blog.component_list import component_list
from blog.middleware import CloseSidebarMiddleware
from blog.pages import routes
# from blog.pages.docs.component import multi_docs


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

# for key in component_list:
#     for component_group in component_list[key]:
#         path = f"/docs/library/{key.lower()}/{component_group[0].__name__.lower()}"
#         app.add_page(
#             multi_docs(path=path, component_list=component_group).component,
#             route=path,
#             title=f"{component_group[0].__name__} | Pynecone",
#         )

# Add the middleware.
app.add_middleware(CloseSidebarMiddleware(), index=0)

# Run the app.
app.compile()
