<h1 align="center">Mathematical Concepts</h1>

1. Vectors
    - It's a object which have both magnitude and direction.
    - 2D vector is represented as $\vec{x} = (a \times \hat{i}) + (b \times \hat{j}) + (c \times \hat{k})$
        - $\hat{i}$ is the unit vector along x-axis.
        - $\hat{j}$ is the unit vector along y-axis.
        - $\hat{k}$ is the unit vector along z-axis.
        - based on the sign of $\hat{i}$, $\hat{j}$ and $\hat{k}$ we can notice the direction of the vector.
    - Magnitude, $|\vec{x}| = \sqrt{a^2 + b^2 + c^2}$
    - Unit Vector, $\hat{x} = \frac{\vec{x}}{|\vec{x}|}$
    - Vector subtraction, $\vec{AB} = \vec{OB} - \vec{OA}$

---

2. Differentiation
    - Differentiation give the slope of a curve at particular point.
    - Differentiation will calculate the slope of a tangent at particular point.
    - $\frac{d[f(x)]}{dx}$ = rate of change of f(x) with respect to x.
    - If the triangle at the tangent is very small
        - $tan\theta = \frac{y_{2} - y_{1}}{x_{2} - x_{1}}$
        - Also represent as = $lim_{h->0} \frac{f(x_{1} + h) - f(x_{1})}{(x_{1} + h) - x_{1}}$ 
    - Rules 
        1. Power Rule : If $f(x) = x^n$ then $f(x)' = n \times x^{n-1}$
        2. Product Rule : 
            - $[f(x) \times g(x)]' = (f(x) \times g(x)') + (f(x)' \times g(x))$
        3. Division Rule :
            - $\frac{Nr}{Dr} = \frac{(Dr \times Nr') - (Nr \times Dr')}{Dr^2}$ 
        - ILATE rule.

---

3. Partial Differentiation
    - If the function comprises of more than 1 variable.
    - $\frac{\partial{f(x, y)}}{\partial{x}}$ or $\frac{\partial{f(x, y)}}{\partial{y}}$ = partial differentiation with respect to any variable.
    - $\frac{\partial{f(x, y)}}{\partial{x}}$ = differentiation of f(x,y) with respect to x by keeping y as constant. or 
    - $\frac{\partial{f(x, y)}}{\partial{y}}$ = differentiation of f(x,y) with respect to y by keeping x as constant.

---

4. Gradient 
    - Partial Differentiation of a function with respect to all the variable.
    - $\delta{f} = $
    - $|\frac{\partial{f(x, y)}}{\partial{x}}|$ 
    - $|\frac{\partial{f(x, y)}}{\partial{y}}|$

---

5. Maxima Minima
    - Critical Points = The points at which slope or differentitation become 0.
    - $f(x)''$ tells the rate of change of slope.
    - There are 3 points for the univariate function.
        1. Minima :
            - $f(x)'' > 0$ i.e slope is increasing.
        2. Maxima :
            - $f(x)'' < 0$ i.e slope is decreasing.
        3. Inflection point :
            - $f(x)'' = 0$ i.e slope remains same.
    - For the bivariate function.
        - If f(x, y) is a function.
        1. Step 1:
            - $p = \frac{\partial{f(x, y)}}{\partial{x}}$
            - $q = \frac{\partial{f(x, y)}}{\partial{y}}$
        2. Step 2:
            - Find the critical points where p = 0 and q = 0.
        3. Step 3:
            - $r = \frac{\partial^2{f(x, y)}}{\partial^2{x}}$
            - $s = \frac{\partial^2{f(x, y)}}{\partial{x}\partial{y}}$
            - $t = \frac{\partial^2{f(x, y)}}{\partial^2{y}}$
        4. Step 4:
            - if $(rt - s^2) > 0$ and r > 0 then it is a local minima.
            - if $(rt - s^2) > 0$ and r < 0 then it is a local maxima.
            - if $(rt - s^2) = 0$ then test fails.
            - if $(rt - s^2) < 0$ then it is saddle point.

---