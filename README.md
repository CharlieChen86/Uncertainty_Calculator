# Uncertainty_Calculator

## Description
Use python to calculate uncertainty according to the following rules
- Addition/Subtraction: add uncertainty
- Multiplication/Division: add relative uncertainty (uncertainty/number)
- Power: multiply relative uncertainty by the power
- Trignometry: uncertainty=sin(number + uncertainty) - sin(number)
## Method
Redefine __add__, __sub__, __mul__, __truediv__ of the class unit then add instances of unit directly. 
Functions sin() and cos() are used to fulfill the calculation of uncertainty in trignometry
## Instructions
- type in the number of variable, noting that constant act as variable with no uncertainty
- type in the number and uncertainty respectively
- type in the expression following the rule that:
	* name variables from var[0] to var[n-1] (n is the number of variables)
	* addition +, subtraction -, multiplication *, division /, power **, cos cos(), sin sin()
- redo the last step i.e. In each running time, data can only be recorded once while expressions are allowed to enter several times