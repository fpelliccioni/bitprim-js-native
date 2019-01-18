#!/bin/bash

# for file in $(git ls-files | grep %*.cc% | sed -e 's/\(%*.cc%[^/]*\).*/\1/' | uniq); git mv $file $(echo $file | sed -e 's/%*.cc%/%*.cpp%/')

find . -name '*.cc' -exec bash -c 'file={}; git mv $file ${file/cc/cpp}' \;
