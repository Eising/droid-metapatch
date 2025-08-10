#!/usr/bin/env bash
# This script confirms that the version that a version given in the git tag
# matches the pyproject version.

# Required environment variables:
# GITHUB_REF_TYPE, must be 'tag'
# GITHUB_REF_NAME: Must be v.*.*.*

FAIL="❌"
CHECK="✅"

#  '\e[%d;%dm%-12s\e[0m'
_fail() {
    printf '\e[0;31m%s\e[0m %s\n' "${@}" "${FAIL}" 1>&2
    exit 1
}

_ok() {
    printf '\e[0;32m%s\e[0m %s\n' "${@}" "${CHECK}"
}

[[ "${GITHUB_REF_TYPE:?'Error: GITHUB_REF_TAG not set!'}" == 'tag' ]] || _fail "Error: This script must run from a workflow triggered by a release tag"

version_tag="${GITHUB_REF_NAME:?'Error: GITHUB_REF_NAME not set'}"

[[ "${version_tag::1}" == "v" ]] || _fail "Malformed version tag"

project_version=$(uv version --short)

printf "Checking if tagged version %s matches version set in pyproject.toml: %s\n" "${version_tag:1}" "${project_version}"

[[ "${project_version}" == "${version_tag:1}" ]] || _fail "Tag version doesn't match project version" && _ok "Project version matches git tag"
