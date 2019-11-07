# TextToPixelArt

## How to use
### Text file arguments (Case Sensitive)

#### Top Line Arguments (Manipulates Output)
`mirror`: Mirror the text file's output across the vertical axis. Cuts down on space used by text file

`auto`: Automatically positions pixel art to the center of the turtle window

`size:<number>`: Sets size of turtle's brush.

`c<number>:<Hex color value >`: Color assignments, starts with `c` for color. Accepts all colors in range of #00000 to #fffff.

`x:` or `y:`: Sets the starting coordinates for the turtle. Does not work when `auto` is set.

#### Art Arguments (Output)

`<X>,c<Y>`: Print `X` number of pixels of `c<Y>` color

`<X>,TP`: Stands for Transparent Pixel. Put in for future plans. Prints `X` times.

`r<X>`: Stands for 'Repeat'. Repeats previous line `X` time, not including the previous line

Each New Line represents a row in the final art output. 

