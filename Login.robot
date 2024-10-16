*** Settings ***
Suite Teardown    Close Browser
Library           Steps.py

*** Variables ***
${DUT_IP}         192.168.22.1
${URL}            http://${DUT_IP}/
${Message in Login Page}    Copyright © 2015 Buffalo Inc.
${DELAY}          20
${FILE}           C:\\Users\\kevin_kang\\Desktop\\TSB\\WSR-5400XE6 Ver.1.14\\WSR-5400XE6_CRC_update.bin

*** Test Cases ***
Valid Login
    FOR    ${i}    IN RANGE    1    11
        Open Browser To Login Page
        Input Password    password
        Submit Credentials
        Welcome Page Should Be Open
        Go to Firmware
        # Start Firmware Update
        # Close Browser
        Go To Login Page
    END

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${URL}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}

Login Page Should Be Open
    Login Page Show Message    ${Message in Login Page}

Input Username
    [Arguments]    ${username}
    Input The Username    ${username}

Input Password
    [Arguments]    ${password}
    Input The Password    ${password}

Submit Credentials
    Click OK Button to Submit

Welcome Page Should Be Open
    My LinkStation should be found

Close Browser
    Close My Browser

Go to Firmware
    Go to the Firmware

Go To Login Page
    Go Back To Login Page

Start Firmware Update
    Firmware Update    ${FILE}
