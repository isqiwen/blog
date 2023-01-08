import asyncio
from datetime import datetime

import pynecone as pc
from email_validator import EmailNotValidError, validate_email
from sqlmodel import Field

from blog import constants, styles
from blog.base_state import State
from blog.templates import webpage

from blog.templates.docpage import (
    doclink,
    doccode,
)

background_style = {
    "background_size": "cover",
    "background_repeat": "no-repeat",
    "background_image": "bg.svg",
}

link_style = {
    "color": "black",
    "font_weight": styles.BOLD_WEIGHT,
    "_hover": {"color": styles.ACCENT_COLOR},
}


class Confetti(pc.Component):
    """Confetti component."""

    library = "react-confetti"
    tag = "ReactConfetti"


confetti = Confetti.create


class Waitlist(pc.Model, table=True):
    email: str
    date_created: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class IndexState(State):
    """Hold the state for the home page."""

    # Whether to show the call to action.
    show_c2a: bool = True

    # The waitlist email.
    email: str

    # Whether the user signed up for the waitlist.
    signed_up: bool = False

    # Whether to show the confetti.
    show_confetti: bool = False

    def close_c2a(self):
        """Close the call to action."""
        self.show_c2a = False

    def signup(self):
        """Sign the user up for the waitlist."""
        # Check if the email is valid.
        try:
            validation = validate_email(self.email, check_deliverability=True)
            self.email = validation.email
        except EmailNotValidError as e:
            # Alert the error message.
            return pc.window_alert(str(e))

        # Check if the user is already on the waitlist.
        with pc.session() as session:
            user = session.query(Waitlist).filter(Waitlist.email == self.email).first()
            if user is None:
                # Add the user to the waitlist.
                session.add(Waitlist(email=self.email))
                session.commit()

        self.signed_up = True
        return self.start_confetti

    def start_confetti(self):
        """Start the confetti."""
        self.show_confetti = True
        return self.stop_confetti

    async def stop_confetti(self):
        """Stop the confetti."""
        await asyncio.sleep(5)
        self.show_confetti = False


def container(*children, **kwargs):
    kwargs = {"max_width": "1440px", "padding_x": ["1em", "2em", "3em"], **kwargs}
    return pc.container(
        *children,
        **kwargs,
    )


def landing():
    return pc.container(
        pc.cond(
            IndexState.show_confetti,
            confetti(),
        ),
        pc.vstack(
            pc.box(
                pc.text(
                    "Welcome to Wang QiWen's blog!",
                    font_size=styles.H2_FONT_SIZE,
                    font_weight=500,
                    font_family=styles.TEXT_FONT_FAMILY,
                    background_image="linear-gradient(271.68deg, #EE756A 25%, #756AEE 50%)",
                    background_clip="text",
                ),
                text_align="center",
                line_height="12.2",
            ),
            spacing="2em",
        ),
        margin_y="5em",
    )


def c2a():
    return pc.box(
        pc.button_group(
            pc.button(
                pc.link(
                    pc.box(
                        "Star on GitHub",
                        pc.icon(
                            tag="StarIcon",
                            color="#eec600",
                            margin_bottom="0.3em",
                            margin_left="0.2em",
                        ),
                        width="100%",
                        height="100%",
                    ),
                    href=constants.GITHUB_URL,
                    _hover={},
                ),
                bg=styles.ACCENT_COLOR,
                color="white",
                border_color=styles.ACCENT_COLOR_DARK,
                _hover={"bg": styles.ACCENT_COLOR_DARK},
            ),
            pc.button(
                pc.icon(tag="CloseIcon", color="white", height=".5em", width=".5em"),
                on_click=IndexState.close_c2a,
                bg=styles.ACCENT_COLOR,
                color="white",
                _hover={"bg": styles.ACCENT_COLOR_DARK},
            ),
            opacity="0.95",
            backdrop_filter="blur(6px)",
            is_attached=True,
            variant="outline",
            box_shadow="xl",
        ),
        z_index="50",
        display="flex",
        justify_content="center",
        position="fixed",
        bottom="2em",
        left="0",
        right="0",
    )

@webpage(path="/")
def index() -> pc.Component:
    """Get the main page."""
    return pc.box(
        landing(),
        pc.cond(
            IndexState.show_c2a,
            c2a(),
        ),
    )
