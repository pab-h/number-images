
# Number-Images

This algorithm transforms a numerical sequence into an image. Yes, I had some free time :V 

## How does it work?
Imagine the sequence of the first 9 decimal places of pi.

`141592653`

Now, cut it into 3 parts:

`141 592 653`

Arranging string in an vector:
`141 592 653` => `[141, 592, 653]`

Normalizing values to be between 0 and 255:
```python 
def normalize(value: int) -> int:
    return value % 255

vector[0] = normalize(vector[0])
vector[1] = normalize(vector[1])
vector[2] = normalize(vector[2])
```

After all, what do we get as a result? We have a vector that represents a pixel, in RGB color, formed by a numerical sequence. With this pixel we can form images as we insert numbers into the numerical sequence.

## Application of this algorithm
I don't know. Does anyone have any ideas? My e-mail, dev.pab.2020@gmail.com, is open for discussion