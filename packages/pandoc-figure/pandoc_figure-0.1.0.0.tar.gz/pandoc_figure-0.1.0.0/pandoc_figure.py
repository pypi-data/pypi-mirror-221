#!/usr/bin/env python

"""
Pandoc filter for adding complex figures.
"""

from panflute import (  # type: ignore
    Caption,
    Div,
    Figure,
    Plain,
    convert_text,
    debug,
    run_filter,
)


# pylint: disable=broad-exception-caught,unused-argument
def figure(elem, doc):
    """
    Transform a div element into a figure element.

    Arguments
    ---------
    elem
        The pandoc element
    doc
        The pandoc document

    Returns
    -------
        Figure or None.
    """
    if (
        isinstance(elem, Div)
        and "figure" in elem.classes
        and "caption" in elem.attributes
    ):
        try:
            caption = convert_text(elem.attributes["caption"])
            del elem.attributes["caption"]
            elem.classes.remove("figure")
            return Figure(
                *elem.content,
                caption=Caption(Plain(*caption[0].content)),
                identifier=elem.identifier,
                classes=elem.classes,
                attributes=elem.attributes,
            )
        except Exception as error:  # noqa: B902
            debug(f"[WARNING] pandoc-figure: {error}")
    return None


def main(doc=None):
    """
    Convert the pandoc document.

    Arguments
    ---------
    doc
        The pandoc document

    Returns
    -------
        The modified pandoc document
    """
    return run_filter(figure, doc=doc)


if __name__ == "__main__":
    main()
