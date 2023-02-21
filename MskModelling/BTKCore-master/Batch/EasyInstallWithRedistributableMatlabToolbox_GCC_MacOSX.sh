#!/bin/bash
abspath="$(cd "${0%/*}" 2>/dev/null; echo "$PWD"/"${0##*/}")"
current_directory=`dirname "$abspath"`
"$current_directory/EasyInstall_GCC.sh" "-DBTK_WRAP_MATLAB:BOOL=1 -DBTK_WRAP_MATLAB_REDISTRIBUTABLE_MEX_FILES:BOOL=1" "-DCMAKE_INSTALL_PREFIX:CHAR=/Applications/BTK"