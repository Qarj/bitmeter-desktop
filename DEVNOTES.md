# Dev notes

## See what versions of wxPython are available

```sh
pip install wxpython==random
.
ERROR: Could not find a version that satisfies the requirement wxpython==random (from versions: 4.0.0a1, 4.0.0a2, 4.0.0a3, 4.0.0b1, 4.0.0b2, 4.0.0, 4.0.1, 4.0.2, 4.0.3, 4.0.4, 4.0.5, 4.0.6, 4.0.7, 4.0.7.post1, 4.0.7.post2, 4.1.0, 4.1.1, 4.2.0, 4.2.1, 4.2.2)
ERROR: No matching distribution found for wxpython==random
```

## wxPython Version 4.2.2

Version 4.2.2 installs very quickly.

```sh
time pip install wxpython
.
Collecting wxpython
  Using cached wxPython-4.2.2-cp312-cp312-linux_x86_64.whl
Collecting six (from wxpython)
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: six, wxpython
Successfully installed six-1.17.0 wxpython-4.2.2

real	0m4.718s
user	0m3.503s
sys	0m1.163s
```

However it throws errors constantly

```sh
(bitmeter) test@testub24:~/git/bitmeter-desktop$ python main.py

(main.py:6328): Gtk-CRITICAL **: 11:29:18.625: gtk_widget_get_scale_factor: assertion 'GTK_IS_WIDGET (widget)' failed
Traceback (most recent call last):
  File "/home/test/git/bitmeter-desktop/main.py", line 298, in OnIdle
    self.InitBuffer()
  File "/home/test/git/bitmeter-desktop/main.py", line 308, in InitBuffer
    self.DrawLines(dc)
  File "/home/test/git/bitmeter-desktop/main.py", line 345, in DrawLines
    dc.DrawLine(x, y0, x, yUl)
TypeError: DC.DrawLine(): arguments did not match any overloaded call:
  overload 1: argument 1 has unexpected type 'float'
  overload 2: argument 1 has unexpected type 'float'
```

In Python 3.10, methods that accept integers will no longer accept floats. https://discuss.wxpython.org/t/float-values-no-longer-accepted-in-wxpython-4-1-2a1-dev5259/35731

## Testing wxPython

```sh
python wx_test.py
python scratch.py
```
