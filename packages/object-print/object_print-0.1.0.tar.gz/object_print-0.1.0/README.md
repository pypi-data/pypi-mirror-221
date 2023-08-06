# object_print - a slightly different take on `pprint`

I didn't like the way `pprint.pprint` was handling some deep but narrow tree, so I wrote this instead.

## Usage

After you `pip install object-print`, you can write:

```python
from object_print import object_print

object_print(['a', 'b', 'c'])
```