#!/bin/bash

set -e

function do_doc () {
    swagger-codegen generate \
        --input-spec swagger/${1}_client/swagger.yaml \
        --lang dynamic-html \
        --output docs/${1}
}

for CLIENT in $(ls -1 swagger | cut -d_ -f1)
do
    do_doc $CLIENT
done
