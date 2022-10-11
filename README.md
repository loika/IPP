# IPP

"Integral and processor parallelization".
- [![Generic badge](https://img.shields.io/badge/with--made-python-informational.svg)](https://shields.io/)

## Introduction

the objective is to compute the approximation of an integral with or without parallelization to compare for each method. The function to integrate is $f(x) = \cos(x^2)\dfrac{\exp(\frac{-x^2}{2})}{\sqrt{2\pi}}$. we have 

$$I(A,B) = \int_A^B\,f(x)d\,x \approx \sum_{i = 1}^N f(x_i)d_{w_i}\qquad ,A \leq x_i \leq B \quad d_{w_i} \in \mathbb{R}$$
For the calculation of the integral with parallelization, we will use the formula of charles :

$$I(A,B) = \sum_{j = 1}^M I(A_j,B_j) $$



### Notation
- $A,B$  the bounds of the integration interval
- $N$ the number of subintervals of the subdivision
- $M$ number of cpu cores 
- $[A_j,B_j]$ subintervals of $[A,B]$
- $x_i$ points
- $d_{w_i}$ pounds

subject to :

- $N \geq M > 0$
- $-\sqrt{\frac{\pi}{2}} \leq A < B \leq  \sqrt{\frac{\pi}{2}}$

### methode

For the approximation of the integral, we use Gaussian quadrature with the three-point Gaussian-lengender formula:

$$I(-1,1) \approx \dfrac{5}{9}f\left(-\sqrt{\frac{3}{5}}\right) + \dfrac{8}{9}f(0) + \dfrac{5}{9}f\left(\sqrt{\frac{3}{5}}\right)$$

The approximation calculation of $I(A_j,B_j)$ is done with a change of variable


<!-- - [![shield](http://img.shields.io/badges/made with-r-informational)](http://forthebadge.com) -->
<!-- - [![shield](http://img.shields.io/badges/made with-matlab-informational)](http://forthebadge.com) -->



<!-- --> 
## to get started

change $N,A,B$ in `program.py`.
```python 
if __name__ == '__main__'
```



## pre-requisites


- [![Generic badge](https://img.shields.io/badge/python-3.7.3-brightgreen.svg)](https://shields.io)

the use of program progmanopt requires :  

- [![Generic badge](https://img.shields.io/badge/numpy-1.6-brithtgreen.svg)](https://shields.io)
- [![Generic badge](https://img.shields.io/badge/time--brithtgreen.svg)](https://shields.io)
- [![Generic badge](https://img.shields.io/badge/multiprocessing--brithtgreen.svg)](https://shields.io)


if the packages are not installed. you can install them the command :

```
pip install -r requirements.txt
```


if the command did not work, you can install the packages one by one with the command  
```
pip install [package]
```

## Contibutor

- **Loik johan ACAKPO-ADDRA** _alias_ [@loik77360](https://github.com/loik77360/PSD)

## Links

### packages

- **[numpy](https://numpy.org/)**
- **[time](https://docs.python.org/3/library/time.html)**
- **[multiprocessing](https://docs.python.org/3/library/multiprocessing.html)**



### Documentation
- **[numerical integrale](https://en.wikipedia.org/wiki/Numerical_integration)**
- **[Gaussian quadrature](https://en.wikipedia.org/wiki/Gaussian_quadrature)**
- **[Monte Carlo integration](https://en.wikipedia.org/wiki/Monte_Carlo_integration)**
- **[Rejection sampling](https://en.wikipedia.org/wiki/Rejection_sampling)**





