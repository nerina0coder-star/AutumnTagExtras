# Autumn(Tag Extras) - Build HTML easily right in your backend
## what is this?

This extension is made to cover Autumn's abstraction with another layer of abstraction,
taking the bare AbstractTag to create and support most of HTML tags, while maintaining the same
level of thread-safety and flexibility.

## How to install?

This extension is made available via the autumn-tag-extras python package, in PyPI.
To install this extension, run:
```shell
pip install autumn-tag-extras
```

## Getting started

You can get started by importing the branch and initializing it, then access and inherit
from varies of pre-defined tags.

```python
from typing import Any

from Autumn import new
from AutumnTagExtras import Branch

Base = new()

with Base:
    tag = Branch()

class CustomDiv(tag.div):
    def __init__(self):
        self.dynamic = True
        super().__init__()
    
    def before_build(self, **kwargs: Any) -> str | None:
        self.tags.append(tag.p(kwargs.get("text", "Hello!")))

page = Base.page.new("page").tag(CustomDiv())
```