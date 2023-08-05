from __future__ import annotations

import pytest

import mknodes


@pytest.mark.parametrize(
    "a,b,result",
    [
        (0, 0, 0),
        (1, 1, 2),
        (3, 2, 5),
    ],
)
def test_resolved_path(a: int, b: int, result: int):
    nav = mknodes.MkNav()
    subnav = nav.add_nav("subsection")
    subsubnav = subnav.add_nav("subsubsection")
    assert subsubnav.resolved_parts == ("subsection", "subsubsection")


def test_creating_module_document():
    nav = mknodes.MkNav()
    subnav = nav.add_nav("subsection")
    module_docs = subnav.add_doc(pytest)
    klasses = list(module_docs.iter_classes())
    assert klasses
