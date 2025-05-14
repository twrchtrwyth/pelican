---
Title: The Mandelbrot Set
Date: 2023-04-29
Author: Wil Ifan
Category: maths
Tags: mandelbrot, c, python, fractals, complex numbers
Slug: mandelbrot
Status: published
Summary: A simple description of the Mandelbrot set.
Image: mandelbrotc.png
Caption: The Mandelbrot Set created using C
---

The **Mandelbrot Set** or **M-set** is a set of complex numbers[^compnum]. A complex number *c* is in the M-set if, upon repeatedly passing successive values of a second complex number *z* through the following equation, *z* never diverges towards infinity[^diverge].

<p>
z<sub>n+1</sub> = z<sub>n</sub><sup>2</sup> + c
</p>

The first value of *z* used is referred to as *z*<sub>0</sub> and is equal to 0. The above is often represented using function notation as *f(z) = z*<sup>2</sup> + *c*, and the process of repeatedly passing the value through the function is referred to as *iteration*. This sequence of iterations can be expressed algebraically as follows:

<p>
f(0), f(f(0)), f(f(f(0)))\.\.\.
</p>

## Visualising the set

To visualise the set using a computer, we take the real and imaginary parts of *c* to represent coordinates on a complex plane[^compplane]. We then iterate over all pixels corresponding to each value of *c* on this plane of coordinates, and colour each according to how rapidly the output of the function exceeds an arbitrarily[^arbval] chosen value.

A very simple visualisation, written in C, where any pixels in the set are black and all other values are white, is shown above.

This has a strange, insectoid beauty of its own, but to truly appreciate the complexity that can emerge the pixels should be coloured according to how rapidly each corresponding value of *c* diverges towards infinity. Below is an example I generated using Python:

![Mandelbrot Set Python]({static}/images/mandelbrotpython.png)


[^compnum]: Complex numbers are of general format *a + bi*, where *i* represents *&radic;-1*. They are so named because they are a complex of both a *real* and an *imaginary* component. In this example *a* represents the *real* and *bi* represents the *imaginary* component.

[^diverge]: That is, the number does not continue to indefinitely increase. The opposite of this is *convergence*--all members of the M-set will *converge* towards 0.

[^compplane]: Imagine a plane of Cartesian coordinates, except instead of an *x* and *y* axis there is instead, respectively, a *real* and *imaginary* axis.

[^arbval]: The value must in fact exceed 2, because -2 is the complex number with the largest magnitude within the set. Other than this, though, the value does not matter.
