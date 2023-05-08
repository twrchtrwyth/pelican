---
Title: C
Date: 2023-05-02 18:40
Author: Wil Ifan
Category: programming
Tags: c, linux
Slug: c
Status: hidden
Summary: A primer in the C programming language.
---

These are my notes on the C programming language, which I decided to start learning in May 2023.

## The C compiler

C programs need to be compiled into an executable before they can be run. A widely used compiler is `gcc`, which I'm pretty sure comes installed as standard on most Linux distros. The `-o` flag used below to assign a specific name to the executable isn't strictly necessary, but the default name of `a.out`.

```shell
gcc program.c -o programName
```

## Obligatory Hello World

Here is an extremely simple example of a C program. Note the `main()` function, the contents of which are wrapped in curly braces `{}`. The `#include <stdio.h>` statement is required in order to access the `printf()` function. Each statement in C must be followed by a semicolon. It seems to be customary to begin a program in c with its name as a comment.

```c
// hello.c
#include <stdio.h>

int main() {
	// this is a comment
	printf("Hello World!\n");
	return 0;
}
```

## Variables and Types

The four most common variable types encountered in C are `int`, `float`, `double`, and `char`. In C a variable's type must be declared before it is assigned a value (though it is possible to do both in the same line of code). Variable names follow the same conventions as in Python.

Floats and doubles both store decimals, but to differing numbers of decimal places. Floats can store to 6 decimal places, doubles to 15. As such doubles take up twice as much memory (8 bytes vs. 4 bytes). However, they run faster than floats--so it's a trade-off for speed at the cost of greater memory usage. Finally, values stored in either get rounded, which leads to a greater chance of errors when using floats due to their lower precision. Doubles should be used whenever accuracy is important, for example in scientific, medical or financial applications.

```c
// variableTypes.c
#include <stdio.h>

int main() {
	/* Here are some examples of the main variable types.
	Apparently the f after the value of the float is
	needed otherwise C thinks it's a double? */
	int integer;
	char letter_or_number;

	integer = 1;
	letter = 'A';
	float life = 42.42f;  // same line declaration and assignment
	double more_decimals = 42.42424242;
	
	printf("Here is the output.")
	return 0;
}
```

## Substituting Values

To substitute variables into a string, a different letter must be used for each type.

```c
// variableTypes.c
#include <stdio.h>

int main() {
  int i = 1, j = 2;  // can assign multiple per line
  char letter = 'A';
  float life = 42.42f;
	
  // substitution values
  printf("Integer: %d\n", i);
  printf("Character: %c\n", letter);
  printf("Float: %.2f\n", life);  // the .2f limits to 2 decimal places
  return 0;
}
```

## Constants

These are declared with the `const` keyword before the `type` is declared. It is usual practice to name constant variables using all upper-case letters.

## Casting (Changing) Types

