*** Settings ***
Library     BuiltIn
Library     Process
Library     RequestsLibrary
Library     Collections
Library     OperatingSystem


*** Variables ***
${APP_ROOT}=    C:\\ProyectosPython\\flask\\factory_method
${HOST}=        127.0.0.1
${PORT}=        5555
${HEADERS}=     {'Content-Type': 'application/json', 'x-api-key':'1111', 'x-api-version': '1'}

*** Test Case ***
Plytix_001
    [Documentation]              Initialize Api server and launch sequence DELETE | POST | GET
    log to console               ${APP_ROOT}
    start process                cd ${APP_ROOT} && python wsgi.py    shell=True    cwd=${APP_ROOT}   stdout=out.log    stderr=error.log

    create session               plytix     http://${HOST}:${PORT}/      headers=${HEADERS}

    ${resp_reset}=               delete on session    plytix      words/reset
    should be equal              ${resp_reset.status_code}    ${205}

    &{body}=                     create dictionary      word=calle      position=3
    ${resp_insert}=              post on session    plytix        words/    json=${body}
    should be equal              ${resp_insert.status_code}   ${201}
    ${json_insert}=              set variable   ${resp_insert.json()}
    should be equal as strings   ${json_insert['word']}         calle
    should be equal as strings   ${json_insert['position']}     3

    ${resp_get}=                 get on session       plytix      words/
    ${json_get}=                 set variable   ${resp_get.json()}
    should be equal              ${resp_get.status_code}    ${200}
    should be equal as strings   ${json_get['data']}     ['calle']

    terminate all processes
