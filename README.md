# RDCalc

A recursive descent calculator made in python

## Grammar
```
sum_sub   => mul_div (("+" | "-") mul_div)*
mul_div   => neg (("*" | "/") neg)*
neg       => ("-" neg) | power
power     => factorial ("^" power)?
factorial => grouping "!"*
grouping  => "(" sum_sub ")" | number
number    => NUMBER
```