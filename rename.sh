#!/bin/bash

C=$( cd $0; pwd )

D=$( mktemp -d )
mv .git ${D}

${C}/bin/rename.py "$@"

mv ${D}/.git .
rmdir ${D}

git ls-files -z --deleted | git update-index -z --remove --stdin
git add -A


git commit -F - <<EOF
automatic rename via rename.py

params:
"$@"
EOF

