# Running Python Scripts

[realpython.com](https://realpython.com/run-python-scripts/)

## Scripts vs. Modules

A script is a plain text sequence of code that is compiled and run by some kind of interpreter (like shell). These are directly executed by the user.

A module is a plain text file contiaining python code intended to be imported and used from another python file.

## Python Interpreter

The interpreter is a layer of software that works between your program and your computer hardware to get your code running.

Depending on the Python implementation you use, the interpreter can be:

- A program written in C, like `CPython`, which is the core implementation of the language
- A program written in Java, like `Jython`
- A program written in Python itself, like `PyPy`
- A program implemented in .NET, like `IronPython`

The interpreter is able to run Python code in two different ways:

1. As a script or module
2. As a piece of code typed into an interactive session

## How to Run Python code Interactiely

A widely used way to run Python code is through an interactive session. To start a Python interactive session, just open a command-line or terminal and then type in `python`, or `python3` depending on your Python installation, and then hit `Enter`.

An example for Linux:

``` py
$ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17)
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

`>>>` is the standard prompt for interactive mode.

You can write and run Python as you wish from here but when you close the session the code will be gone.

In Interactive Mode every expression and statement you type is evaluated and executed immediately.

To exit Interactive Mode, execute `quit()` or `exit()`.

## How does the Interpretor Run Python Script?

1. **Process the statements of your script in a sequential fashion**

2. **Compile the source code to an intermediate format known as bytecode**

    This bytecode is a translation of the code into a lower-level language that’s platform-independent. Its purpose is to optimize code execution. So, the next time the interpreter runs your code, it’ll bypass this compilation step.

    Strictly speaking, this code optimization is only for modules (imported files), not for executable scripts.

3. **Ship off the code for execution**

    At this point, something known as a Python Virtual Machine (PVM) comes into action. The PVM is the runtime engine of Python. It is a cycle that iterates over the instructions of your bytecode to run them one by one.

    The PVM is not an isolated component of Python. It’s just part of the Python system you’ve installed on your machine. Technically, the PVM is the last step of what is called the Python interpreter.

The whole process to run Python scripts is known as the Python Execution Model.

>Note: This description of the Python Execution Model corresponds to the core implementation of the language, that is, CPython. As this is not a language requirement, it may be subject to future changes.

## How to Run Python Scripts Using the Command Line

Python scripts described here are saved plain text files using the `.py` extension. This can be `.pyw` on windows machines.

Example:

```py
#!/usr/bin/env python3

print('Hello World!')
```

## Using the Python Command

To run Python sripts through command-line, type the word `python` or `python3` (depending on your version) followed by the path to your script.

Example:

```sh
$ python3 hello.py
```

If this doesn't work, you may need to double check your system PATH or type in the entire file path to the script you intend to run.

## Redirecting the Output

If you want to save the output of a shell session:

```sh
$ python3 hello.py > output.txt
```

This redirects the output of your script to `output.txt` rather than to the standard system output `stdout`. The process is commonly known as **stream redirection** and is available on both Windows and Unix-like systems.

If `output.txt` doesn't exist then it will be created. If it does exist, then it will be replaced. The output file will be made in the current directory unless otherwise specified by typing the filepath as part of the output file name. 

Example:

```sh
$ python3 hello.py > /Users/matthewgimpelevich/Documents/Programming/Python/output.txt
```

If you want to add the output of consecutive executions to the end of `output.txt`, use two angle brackets `>>` instead of one.

```sh
$ python3 hello.py >> output.txt
```

## Running Modules with the -m Option

Python offers a series of command-line options that you can use according to your needs. For example, if you want to run a Python module, you can use the command python `-m` `<module-name>`.

The `-m` option searches `sys.path` for the module name and runs its content as `__main__`:

```sh
$ pythong3 -m hello
```

## Using the Script Filename

On recent versions of Windows, it is possible to run Python scripts by simply entering the name of the file containing the code at the command prompt:

```sh
C:\devspace> hello.py
Hello World!
```

This is possible because Windows uses the system registry and the file association to determine which program to use for running a particular file.

On Unix-like systems, such as GNU/Linux, you can achieve something similar. You’ll only have to add a first line with the text `#!/usr/bin/env python`, just as you did with hello.py.

*For Python, this is a simple comment, but for the operating system, this line indicates what program must be used to run the file.*

This line begins with the `#!` character combination, which is commonly called **hash bang** or **shebang**, and continues with the path to the interpreter.

There are two ways to specify the path to the interpreter:

1. `#!/usr/bin/python`: writing the absolute path
2. `#!/usr/bin/env python`: using the operating system env command, which locates and executes Python by searching the PATH environment variable

This last option is useful if you bear in mind that not all Unix-like systems locate the interpreter in the same place.

Finally, to execute a script like this one, you need to assign **execution permissions** to it and then type in the filename at the command-line.

Here’s an example of how to do this:

```sh
$ # Assign execution permissions
$ chmod +x hello.py
$ # Run the script by using its filename
$ ./hello.py
Hello World!
```

With execution permissions and the shebang line properly configured, you can run the script by simply typing its filename at the command-line.

Finally, you need to note that if your script isn’t located at your current working directory, you’ll have to use the file path for this method to work correctly.

## How to Run Python Script Interactively

It's possible to run Python scripts and modules from an interactive session.

### Taking Advantage of `import`

When you import a module, you are loading its contents for later access and use. `import` runs the code as its final step.

When the module contains only classes, functions, variables, and constants definitions, you probably won’t be aware that the code was actually run, but when the module includes calls to functions, methods, or other statements that generate visible results, then you’ll witness its execution.

This provides another option to run Python scripts:

```py
>>> import hello
```

This option works only once per session. Subsequent import executions will do nothing, even if you modify the contents of the module. This is because `import` operations are expensive and therefore run only once.

Requirements for this method to work:

- The file with the Python code must be located in your current working directory.
- The file must be in the Python Module Search Path (PMSP), where Python looks for the modules and packages you import.

To know your current PMSP, run the following:

```py
>>> import sys
>>> for path in sys.path:
...     print(path)
...
/usr/lib/python36.zip
/usr/lib/python3.6
/usr/lib/python3.6/lib-dynload
/usr/local/lib/python3.6/dist-packages
/usr/lib/python3/dist-packages
```

This is where Python searches the modules you import.

### Using `importlib` and `imp`

In the Python Standard Library, you can find `importlib`, which is a module that provides `import_module()`.

With `import_module()`, you can emulate an import operation and execute any module or script.

Example:

```py
>>> import importlib
>>> importlib.import_module('hello')
Hello World!
<module 'hello' from '/home/username/hello.py'>
```

Once you've imported a module for the first time, you won't be able to continue using `import` to run it. You can, however, use `importlib.reload()` to force the interpeter to re-import the module again.

Example:

```py
>>> import hello  # First import
Hello World!
>>> import hello  # Second import, which does nothing
>>> import importlib
>>> importlib.reload(hello)
Hello World!
<module 'hello' from '/home/username/hello.py'>
```

>Note: The argument of `reload()` needs to be the name of a module, not a string. This is true of `import_module()` as well. Committing this error results in a `TypeError` exception.

If you are using Python 2.x, then you'll have `imp`, which is a module that provides a function called `imp.reload()` that works similarly to `importlib.reload()`. Currently `imp` is being phased out in favor of `importlib`.

### Using `unpy.run_module()` and `runpy.run_path()`

The Standard Library includes a module called `runpy` that contains the `run)module()` function, which allows you to run modules without importing them first. This function returns the `globals` dictionary of the executed module.

Example:

```py
>>> runpy.run_module(mod_name='hello')
Hello World!
{'__name__': 'hello',
    ...
'_': None}}
```

The module is located using a standard import mechanism and then executed on a fresh module namespace.

The first argument of `run_module()` must be a string with the absolute name of the module (without the `.py` extension).

`runpy` also provides `run_path()`, which will allow you to run a module by providing its location in the filesystem:

```py
>>> import runpy
>>> runpy.run_path(path_name='hello.py')
Hello World!
{'__name__': '<run_path>',
    ...
'_': None}}
```

This also returns the `globals` dictionary of the executed module.

The `path_name` parameter must be a string and can refer to the following:

- The location of a Python source file
- The location of a compiled bytecode file
- The value of a valid entry in the sys.path, containing a __main__ module (__main__.py file)

### Hacking `exec()`

The previous methods were the most commonly used ways to run Python scripts. Next, we'll see how to do all that using `exec()`, a built in funtion that supports the dynamic execution of Python code.

`exec()` provides an alternate way for running your scripts:

```py
>>> exec(open('hello.py').read())
'Hello World!'
```

The statement opens `hello.py`, reads out its content, and sends it to `exec()`, which finally runs the code.

## How to Run Python from an IDE or Text Editor

Most programs offer the possibility of running your scripts from inside the environment itself using a *run* or *build* command.

Python installations include IDLE as the default IDE, which allows you to write, debug, modify, and run your modules and scripts.

## How to Run Python Scripts from a File Manager

Running a script by double-clicking on its icon in a file manager is another possible way to run your Python scripts. This option may not be widely used in the development stage, but it may be used when you release your code for production.

In order to be able to run your scripts with a double-click, you must satisfy some conditions that will depend on your operating system.

Windows, for example, associates the extensions .py and .pyw with the programs python.exe and pythonw.exe respectively. This allows you to run your scripts by double-clicking on them.

When you have a script with a command-line interface, it is likely that you only see the flash of a black window on your screen. To avoid this annoying situation, you can add a statement like input('Press Enter to Continue...') at the end of the script. This way, the program will stop until you press Enter.

This trick has its drawbacks, though. For example, if your script has any error, the execution will be aborted before reaching the input() statement, and you still won’t be able to see the result.

On Unix-like systems, you’ll probably be able to run your scripts by double-clicking on them in your file manager. To achieve this, your script must have execution permissions, and you’ll need to use the shebang trick you’ve already seen. Likewise, you may not see any results on screen when it comes to command-line interface scripts.

Because the execution of scripts through double-click has several limitations and depends on many factors (such as the operating system, the file manager, execution permissions, file associations), it is recommended that you see it as a viable option for scripts already debugged and ready to go into production.