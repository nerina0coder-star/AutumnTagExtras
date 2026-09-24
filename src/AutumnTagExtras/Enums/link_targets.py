

import enum


class LinkTargets(enum.Enum):
    """
    Contains opening targets when opening a URL.
    """

    REPLACE_SELF = "_self"
    """
    The opened URL replaces the current page.
    """

    NEW_PAGE = "_blank"
    """
    The URL opens in a new tab.
    """

    PARENT_FRAME = "_parent"
    """
    The opened URL replaces the parent page(A page that embeds this page).
    """

    FULL = "_top"
    """
    Opens the URL in the full body of the window
    """

    def __str__(self) -> str:
        return self.value
