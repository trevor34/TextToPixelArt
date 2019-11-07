# TextToPixelArt v1.1.0

## How to use
### Text file arguments (Case Sensitive)

#### Top Line Arguments (Manipulates Output / Variable Assignments)
`mirror`: Mirror the text file's output across the vertical axis. Cuts down on space used by text file

`auto`: Automatically positions pixel art to the center of the turtle window

`size:<number>`: Sets size of turtle's brush.

`<CV>:<Hex color value>`: Color assignments. Replace `<CV>` with any valid string. Accepts all colors in range of #00000 to #fffff.

`x:` or `y:`: Sets the starting coordinates for the turtle. Does not work when `auto` is set.

`bg:<Hex color value>`: Changes the color of the turtle window's background. Defaults to `#fff`

#### Art Arguments (Output)

`<X>,<CV>`: Print `X` number of pixels of `<CV>` color

`<X>,TP`: Stands for 'Transparent Pixel'. Prints `X` times. Put in for future plans. 

`r<X>`: Stands for 'Repeat'. Repeats previous line `X` times, not including the previous line

Each New Line represents a row in the final art output. 
