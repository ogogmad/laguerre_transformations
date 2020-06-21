# laguerre_transformations
A library for visualising the mathematical transformations known as
Laguerre transformations.

Laguerre transformations act on oriented lines in the plane. They don't
act on points.

Laguerre transformations are analogous to the Moebius transformations.
Both are representable by 2x2 matrices. The difference being that 
Moebius transformations are representable by complex-numbered matrices,
while Laguerre transformations are representable by *dual-numbered*
matrices.

The library requires Sympy and PIL.

Examples:

```python
from laguerre_transformations import *

circle1 = make_circle((100,100),100,nlines=50)
circle2 = make_circle((50,50),-100,nlines=50)

transformation = dual_matrix(3,5,-1,3,9,-6,4,2)

animate_transformation(transformation,
                       circle1 + circle2,
                       "transformation_animation.gif",
                       offset=(200,200))
```

This snippet interpolates between the identity matrix and the given
transformation (represented as a dual number matrix), applies this sequence
of interpolated transformations to two circles, and then saves the result as a
GIF animation.

Another example:

```python
from laguerre_transformations import *

grid = make_grid()

transformation = dual_matrix(3,5,-1,3,9,-6,4,2)

animate_transformation(transformation,
                       grid,
                       "transformation_animation.gif",
                       offset=(200,200))
```

This time, the same sequence of transformations are applied to a square grid.
