# PyXor
<a href="https://pypi.org/project/PyXor/" target="_blank">
  <img alt="Install" src="https://img.shields.io/badge/ModulePage-pypi-brightgreen.svg" />
  
## Langage
  Python 3.9.4

## Install

```sh
pip install pyXor
```
  
## How To Use
  `XorEncode(key,string)`
  
  `XorDecode(key,string)`
  
## Encode
  ```python
  import pyXor
  print(pyXor.XorEncode("I'm A Key","I'm A String"))
  ```
  <br>
  <p>Output:</p>
  <br>

  ```
  110101001110110010100011101110111101110011101101100101001011111011101111101000011010010010100001
  ```
## Decode
  ```python
  import pyXor
  print(pyXor.XorDecode("I'm A Key","110101001110110010100011101110111101110011101101100101001011111011101111101000011010010010100001"))
  ```
  <br>
  <p>Output:</p>
  <br>
  
  ```
  I'm A String
  ```
