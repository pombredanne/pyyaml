#!/bin/bash

set -e
set -x


if [[ "${TOXENV}" = pypy* ]]; then
    PYENV_ROOT="$HOME/.pyenv"
    PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"
fi


tox
