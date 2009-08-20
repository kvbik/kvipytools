#!/bin/bash

# currdir
C=$( cd $( dirname $0 ); pwd )
# tmpdir
D=$( mktemp -d )

# exclude .git dir
mv .git ${D}

# do rename with all params
${C}/rename.py "$@"

# return .git dir here
mv ${D}/.git .
rmdir ${D}

# remove deleted files and add new ones
git ls-files -z --deleted | git update-index -z --remove --stdin
git add -A

# write nice commit message
git commit -F - <<EOF
automatic rename via rename.py

params:
"$@"
EOF

