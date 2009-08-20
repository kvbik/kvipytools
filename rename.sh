#!/bin/bash

C=$( cd $( dirname $0 ); pwd )

D=$( mktemp -d )
mv .git ${D}

${C}/rename.py "$@"

mv ${D}/.git .
rmdir ${D}

git ls-files -z --deleted | git update-index -z --remove --stdin
git add -A


git commit -F - <<EOF
automatic rename via rename.py

params:
"$@"
EOF

