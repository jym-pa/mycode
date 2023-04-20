# Class Shortcuts!
## The 'make executable' and 'run' two-step
### Description
Contained within `.bash_aliases` is a function that will accept the input of a file name and:
1. mark it as executable
2. run it

The function is aliased to '**pyrun**'.
### Usage
1. Copy `.bash_aliases` to your home directory

`cp .bash_aliases ~/`

2. Source your `.bashrc` file

`source ~/.bashrc`

3. Use `pyrun` with a `.py` file after you've created it - *note:* for files that are in the `pwd` you'll need to add `./` to the filename resulting in `./<filename>.py`

`pyrun ./exercise.py`
