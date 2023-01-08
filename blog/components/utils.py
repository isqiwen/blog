import pynecone as pc

from blog import constants, styles


def coming_soon(subject_name : str = "") -> pc.Component:
    if subject_name == "":
        show_txt = "COMING SOON!"
    else:
        show_txt = subject_name.upper() + " IS COMING SOON!"

    return pc.container(
        pc.vstack(
            pc.box(
                pc.text(
                    show_txt,
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
