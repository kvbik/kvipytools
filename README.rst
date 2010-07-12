
KviPyTools
==========

some usefull scripts for various purpouses

:rename:
	do recursive rename of files, directories and all its content (does not work on ms windows)
:run:
	run specified command in multiple directories

rename
------

call ``rename.sh`` wrapper for git repositories, it moves ``.git`` dir away,
performs all renames, moves ``.git`` dir back and creates commit::

  ./scripts/rename.sh \
    djangobaselibrary=yournewsupercoollibrary \
    django-base-library=your-new-super-cool-library \
    "Django Base Library=You New Super Cool Library"

each param is one rename pattern.

run
---

you can either pass arguments directly::

  ./scripts/run 'git checkout master' ./first-repo/ /tmp/second-repo/ ~/third-repo/

or define some replacements in ``runcommand.py``,
which will be evaluated. it is found in actual directory::

  # beginnig of runcommand.py
  import os.path

  MY_DIRS = (
      './first-repo',
      '/tmp/second-repo',
      os.path.expanduser('~/third-repo/'),
  )

  my_command = 'git checkout master'

  # end of runcommand.py

than call::

  ./scripts/run my_command MY_DIRS

you can define as many variables as you want,
and there are two special names ``_cmd`` and ``_ALL``,
which are taken if no params are given::

  # beginnig of runcommand.py
  import os.path

  MY_DIRS = (
      './first-repo',
      '/tmp/second-repo',
      os.path('~/third-repo/'),
  )

  my_command = 'git checkout master'

  _ALL = MY_DIRS
  _cmd = my_command

  # end of runcommand.py

so, if you now call::

  ./scripts/run

now all three script calls are equivalent

