Title: How to Format Code Blocks
Date: 17-08-2022 18:10
Category: examples
Tags: pelican, python, code
Slug: code-blocks

This post contains some examples of code blocks, and demonstrates how syntax highlighting works.

First, some python without line numbers:

    :::python
    for i in range(5):
        print(i)

And now with the line numbers:

    #!python
    print("This is the first line.")
    print("And this is the second.")
    # Here's an example of looping over a list.
    my_list = [1, 2, 3]
    for number in my_list:
        print(number)

What about some JavaScript?

    :::javascript
    // This function is pretty pointless.
    function test(number){
      return 1 + number
    }


