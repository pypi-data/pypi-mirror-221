# A rich version of TQDM

Just a small package that lets you do:

```python
from quickbar import Quickbar

for item in Quickbar.track(iterable):
	# do things
	print(item)
```

Nothing major yet, will implement nested calls if needed.
