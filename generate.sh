#!/bin/bash

re='^[0-9]+$'
if ! [[ $1 =~ $re ]] || [[ ${#1} -ne 4 ]]; then
    echo "invalid year entry, must be 4 digit integer"
    exit 1
fi

if ! [[ $2 =~ $re ]] || [[ ${#2} -ne 2 ]] || [[ $2 -gt 25 ]]; then
    echo "invalid day entry, must be 2 digit integer, must be le 24"
    exit 1
fi

filepath="src/sln/${1}_${2}.py"

if [[ -f "$filepath" ]]; then
    echo "'$filepath' already exists, exiting"
    exit 1
fi

cat > "$filepath" << EOF
def p1(f):
    lines = f.splitlines()
    res = 0

    # Add Solution Here

    return res

def p2(f):
    lines = f.splitlines()
    res = 0

    # Add Solution Here

    return res
EOF

echo "generated file $filepath"
