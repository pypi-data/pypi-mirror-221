# A small rich TQDM clone

The goal of this small package is to turn the [rich package](https://rich.readthedocs.io/en/stable/introduction.html) into a clone of [tqdm](https://tqdm.github.io/).

For now, only basics are here:

```python

from quickbar import Quickbar

for item in Quickbar.track(iterator):
	# do fancy stuff
	print("I exist !")
```

This is the big upside of TQDM over rich: a less cool bar, but one line is enough !
