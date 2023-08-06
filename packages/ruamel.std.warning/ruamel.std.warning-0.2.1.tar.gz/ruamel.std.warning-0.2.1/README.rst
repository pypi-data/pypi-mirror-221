
extend warnings.warn with callee parameter

When you have some library, with some deprecated function `X`, you can use the `stacklevel=2` parameter 
on `warnings.warn` to show the file-name and line-number of the routine calling `X`

But if you have some framework that calls the user provided code, either through plug-ins or
by explicit registering, the `stacklevel` doesn't help you to complain about return values
that are deprecated.

This library extends `warnings.warn` with a `callee` parameter. If this is provided `stacklevel` should
not be provided and the value for `callee` should be a method or function for
which the warning is raised.

The warning will usually be a `PendingDeprecationWarning`, a `DeprecationWarning` or a subclass of either.

As an example, if you have two files `p0.py` and `p2.py` both with content::

  class PlugIn:
   def status(self):
       return {'result': 'ok'}

And a file `p1.py`:

  class PlugIn:
      def status(self):
          return ['ok'] # this plug-in has been updated

And these files are in a subfolder `plug_ins` where your framework can find them. Then running::


  import sys
  from pathlib import Path
  from importlib import import_module
  import ruamel.std.warnings
  import warnings

  class DictReturnPendingDeprecationWarning(PendingDeprecationWarning):
      pass

  class Driver:
      def __init__(self):
          self.plug_ins = []

      def load_plug_ins(self):
          sys.path.append('plug_ins')
          for file_name in Path('plug_ins').glob('p*.py'):
              mod = import_module(file_name.stem) 
              self.plug_ins.append(mod.PlugIn())

      def check_status(self):
          for p in self.plug_ins:
              retval = p.status()
              if isinstance(retval, dict):
                  # assume dict
                  warnings.warn(
                     'callable should return list, not dict',
                     DictReturnPendingDeprecationWarning,
                     callee=p.status,
                  )
              else:
                  pass  # assume list

  warnings.simplefilter('once', PendingDeprecationWarning)

  def doit():
      driver = Driver()
      driver.load_plug_ins()
      for idx in range(2):
          driver.check_status()
      warnings.warn('almost done', PendingDeprecationWarning)

  doit()

will result in::

  /tmp/plug_ins/p0.py:2: DictReturnPendingDeprecationWarning: callable should return list, not dict
    def status(self):
  /tmp/plug_ins/p2.py:2: DictReturnPendingDeprecationWarning: callable should return list, not dict
    def status(self):
  /tmp/tmp_00.py:40: PendingDeprecationWarning: almost done
    warnings.warn('almost done', PendingDeprecationWarning)
