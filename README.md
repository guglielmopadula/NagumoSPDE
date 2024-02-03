# Nagumo SPDE

## Dataset

A set of trajectory from the Nagumo SPDE
$$du=u_{x x}+u(1-u)(u+1)ds+\int_{0}^{1}dW(t)$$
with 
$$t\in [0,1]$$
$$x\in [0,20]$$
$$u(0,x,\omega)=(1+\exp (-(2-x) / \sqrt{2}))^{-1}$$
$$u(t,0,\omega)=u(t,20,\omega)=0$$
and $W(t)$ is the $Q$ -Wiener process on  $L^2(0, 20)$ with kernel 
$$q(x, y)=\mathrm{e}^{-|x-y|}.$$
This is the example 10.30 of [this book](https://www.cambridge.org/core/books/an-introduction-to-computational-stochastic-pdes/01A784303F5C86644A25BFB138923090). The code for generating the dataset is also taken from the book.
