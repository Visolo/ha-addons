#!/usr/bin/with-contenv bashio
set -e

bashio::log.info "Reading pypi packages"
PYPI=$(bashio::config 'pypi')
bashio::log.info "PYPI=${PYPI}"

bashio::log.info "Reading apk packages"
APK=$(bashio::config 'apk')
bashio::log.info "APK=${APK}"


# Cleanup old deps
bashio::log.info "Remove old deps"
rm -rf /config/deps/*

touch /config/deps/test3.txt

# Need custom apk for build?
if [ -n "${APK}" ]; then
    for dep in ${APK}; do
        bashio::log.info "Installing alpine package '${dep}'"
        # shellcheck disable=SC2086
        if ! ERROR="$(apk add --no-cache ${dep})"; then
            bashio::log.error "Can't install ${dep}!"
            bashio::log.error "${ERROR}" && exit 1
        fi
    done
fi

# Install pypi modules
bashio::log.info "Install pypi modules into deps"
export PYTHONUSERBASE=/config/deps

for dep in ${PYPI}; do
    bashio::log.info "Installing python package '${dep}'"
    
    # shellcheck disable=SC2086
    if ! ERROR="$(pip3 install --user --no-cache-dir --no-dependencies --disable-pip-version-check ${dep})"; then
        bashio::log.error "Can't install ${dep}!"
        bashio::log.error "${ERROR}" && exit 1
    fi
done

bashio::log.info "Done"
