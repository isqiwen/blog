"""Logic for the sidebar component."""

from __future__ import annotations

import inspect

import pynecone as pc
from pynecone.base import Base

from blog import styles
from blog.component_list import component_list
from blog.route import Route

# Sidebar styles.
heading_style = {
    "color": styles.DOC_REG_TEXT_COLOR,
    "font_weight": "500",
}
heading_style2 = {
    "font_size": styles.TEXT_FONT_SIZE,
    "color": styles.DOC_REG_TEXT_COLOR,
    "font_weight": "500",
}
heading_style3 = {
    "font_weight": styles.DOC_SECTION_FONT_WEIGHT,
    "font_size": styles.H3_FONT_SIZE,
    "color": styles.DOC_HEADER_COLOR,
    "margin_bottom": "0.5em",
    "margin_left": "1.1em",
}


class SidebarItem(Base):
    """A single item in the sidebar."""

    # The name to display in the sidebar.
    name: str

    # The link to navigate to when the item is clicked.
    link: str = ""

    # The children items.
    children: list[SidebarItem] = []


def create_item(route: Route, children=None):
    """Create a sidebar item from a route."""
    if children is None:
        name = route.title.split(" | Pynecone")[0]
        return SidebarItem(name=name, link=route.path)
    return SidebarItem(
        name=inspect.getmodule(route).__name__.split(".")[-1].replace("_", " ").title(),
        children=list(map(create_item, children)),
    )


def sidebar(url=None, **props) -> pc.Component:
    """Render the sidebar."""
    return pc.text("empty")
