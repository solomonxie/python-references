_inject_envfile() {
    local fpath
    fpath=$1
    if [[ -e "$fpath" ]];then
        export $(grep -v '^#' $fpath | xargs) > /dev/null
        echo "injected env: ${fpath}"
    fi
}

_inject_envfile envfile
_inject_envfile envfile-local
