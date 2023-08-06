`unit-syntax` adds support for physical units to the Python language:

```python
>>> speed = 5 meters/second
>>> (2 seconds) * speed
10 meter
```

Why? I often use Python as an interactive calculator for physical problems, and wished it had the type safety of explicit units along with the readability of normal notation.

Where? `unit-syntax` currently supports Jupyter notebooks and the IPython interpreter; support for standalone scripts is planned.

How? A syntax transformer based on the official Python grammar turns these expression into calls to the excellent [Pint](https://pint.readthedocs.io/) units library.

## Getting Started

Install the package:

```shell
$ pip install unit-syntax
```

To enable unit-syntax in a Jupyter/IPython session run:

```python
import unit_syntax
unit_syntax.enable_ipython()
```

Tip: In Jupyter this must be run in its own cell before any units expressions are evaluated.

## Usage

[An interactive notebook to play around with units](https://colab.research.google.com/drive/1PInyLGZHnUzEuUVgMsLrUUNdCurXK7v1#scrollTo=JszzXmATY0TV)

Units can be applied to any "simple" expression:

- number: `1 meter`
- variables: `x parsec`, `y.z watts`, `area[id] meters**2`
- lists and tuples: `[1., 37.] newton meters`
- unary operators: `-x dBm`
- power: `x**2 meters`

To apply units within a more complex expression, use parentheses:

```python
one_lux = (1 lumen)/(1 meter**2)
```

Units can be used in other places where Python allows expressions like:

- function arguments: `area_of_circle(radius=1 meter)`
- list comprehensions: `[x meters for x in range(10)]`

Quantities can be converted to another measurement system:

```python
>>> (88 miles / hour) furlongs / fortnight
236543.5269120001 furlong / fortnight
>>> (0 degC) degF
31.999999999999936 degree_Fahrenheit
```

Compound units (e.g. `newtons/meter**2`) are supported and follow the usual precedence rules.

Units _may not_ begin with parentheses (consider the possible
interpretations of `x (meters)`). Parentheses are allowed anywhere else:

```python
# parsed as a function call, will result in a runtime error
x (newton meters)/(second*kg)
# a-ok
x newton meters/(second*kg)
```

## Why only allow units on simple expressions?

The rule for applying units only to "simple" expressions rather than treating it as a typical operator is to avoid unintentional error. Imagine units were instead parsed as operator with high precedence and you wrote this reasonable looking expression:

```python
ppi = 300 pixels/inch
y = x inches * ppi
```

`inches * ppi` would be parsed as the unit, leading to (at best) a runtime error sometime later and at worst an incorrect calculation. This could be avoided by parenthesizing the expression (e.g. `(x inches) * ppi`, but in general it's too error prone to allow free intermixing of operators and units. (Note: This is not a hypoethical concern, I hit this within 10 minutes of first trying out the idea)

## Help!

If you're getting an unexpected result, try using `unit_syntax.enable_ipython(debug_transform=True)`. This will log the transformed Python code to the console.

If you're stuck, feel free to open an issue.

## How does it work?

The parser is derived from the official Python grammar using the same parser generator ([pegen](https://github.com/we-like-parsers/pegen)) as Python itself. The transformer hooks into IPython/Jupyter using [custom input transformers](https://ipython.readthedocs.io/en/stable/config/inputtransforms.html).

## Prior Art

The immediate inspriration of `unit-syntax` is a language called [Fortress](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.180.6323&rep=rep1&type=pdf) from Sun Microsystems. Fortress was intended as a modern Fortran, and had first-class support for units in both the syntax and type system.

F# (an OCaml derivative from Microsoft) also [has first class support for units](https://en.wikibooks.org/wiki/F_Sharp_Programming/Units_of_Measure).

The Julia package [Unitful.jl](http://painterqubits.github.io/Unitful.jl/stable/)

A [long discussion on the python-ideas mailing list](https://lwn.net/Articles/900739/) about literal units in Python.

## Development

To regenerate the parser:

`python -m pegen grammar.txt -o unit_syntax/parser.py`

Running tests:

```
$ poetry install --with dev
$ poetry run pytest
```

## Future work and open questions

- Test against various ipython and python versions
- Support standalone scripts through sys.meta_path
- Check units at parse time
- Unit type hints, maybe checked with [@runtime_checkable](https://docs.python.org/3/library/typing.html#typing.runtime_checkable). More Pint typechecking [discussion](https://github.com/hgrecco/pint/issues/1166)
- Expand the demo Colab notebook
- Typography of output
- make it work with numba
- understand how numpy interop works
- fail more clearly when units are used in an invalid location
