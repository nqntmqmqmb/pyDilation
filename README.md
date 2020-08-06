# pyDilation
A script for calculating the temporal dilation caused by an object in the universe considering metric of Schwarzschild

# Preview
<p align="center"><img src="https://image.prntscr.com/image/TrjmWMcHT7OQoG4ocEavSw.png"/></p>

# Wolfram Alpha code
The WolframAlpha code is available to check the calculations

# Based on
The script is based on these tests : 

Example for VY CANIS MAJORIS : <br/>
Mass : 3,381 × 10^31 kg<br/>
RS = 2GM/c²<br/>
`= 2 * 6.6743 * 10^-11 * 3.381 * 10^31 / 300000000^2`<br/>
`= 50146.24066666666666666666666666666666666666666666666666666m`<br/>
`= sqrt((1 - 50146.24 / (7 * 10^8)) * 1^2 - (1 - 50146.24 / 7 * 10^8)^-1*0^2 - (7 * 10^8)^2 (0 + sin^2 (0) * 0^2)))`<br/>
`= 0.99996418062`<br/>
`365*24*3600-365*24*3600*0.99996418062`<br/>
`= 1129.59996768s`<br/>
<br/>
Example for Mars:<br/>
Mass = 6,39 × 10^23 kg<br/>
RS = 2GM/c²<br/>
`= 2 * 6.6743 * 10^-11 * 6.39 * 10^23 / 300000000^2`<br/>
`= 0.0009477506m`<br/>
`ds² = (1-Rs/r) dt² - (1-Rs/r)^-1 dr²- r²(dθ² + sin² θ dφ²)`<br/>
`= (1 - 0.0009477506m / 7 × 10^8) × 1² - (1 - 0.0009477506m / 7 × 10^8)^-1× 0² - (7 × 10^8)² (0 + sin² (0) × 0²)`<br/>
`= sqrt((1 - 0.0009477506 / (7 * 10^8)) * 1^2 - (1 - 0.0009477506 / 7 * 10^8)^-1× 0^2 - (7 × 10^8)^2 (0 + sin^2 (0) × 0^2)))`<br/>
`= 0.999999999999323035`<br/>
`365 * 24 * 3600 - 365 * 24 * 3600 * 0.999999999999323035`<br/>
`= 0.00002134876824s`<br/>

# Module
You can use PyDilation as a module by putting `dilation.py` it the same folder as your script.<br>
`dilation.Schwarzschild()` or `Schwarzschild()` is used to calculate the <a href="https://en.wikipedia.org/wiki/Schwarzschild_radius">Schwarzschild Radius</a><br>
`dilation.time_Space()` or `time_Space()` is used to calculate the distance of time space at the surface of the object<br>
`dilation.Shift()` or `Shift()` is used to calculate the Shift between the object and a distant observer.

`dilation.Schwarzschild()` two arguments : `mass` which is the solar mass of your object and `details`*
`dilation.time_Space()` two arguments : `SR` which is the Schwarzschild Radius of your object and `details`*
`dilation.Shift()` two arguments : `time_space` which is the distance of time space at the surface of the object and `details`*

*`details` is an additional parameter to print (or not) more informations about the calculation.
