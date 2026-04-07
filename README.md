# RDCalc

A recursive descent based calculator made in python, which uses a three-walk interpreter to solve expressions.

The code's structure is based on the code from the book "Crafting Interpreters" by Robert Nystrom.


## Requirements
- python >= 3.12, but something older might work just fine.

## Usage

The entry point is main.py, so it's as simple as running the file.
It accepts one optional arguments, --ast, which enables the AST representation for each input.

``` bash
    python main.py [--ast]
```

The program is a REPL, so it prints the result immediatly after each input.

To stop excecution, type CTRL+C.

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