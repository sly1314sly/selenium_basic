*** Settings ***
Documentation   User Login
Library         SeleniumLibrary
Library         util.py

*** Variables ***
${Server_Url}   http://39.107.96.138:3000/
${Browser}      chrome
${UserName}     testuser1
${Password}     123456



*** Keywords ***
testuser1成功登录
    Open Browser    ${Server_Url}  ${Browser}
    Maximize Browser Window
    Click Element   css:a[href="/signin"]
    Input Text      id:name      ${UserName}
    Input Text      id:pass      ${Password}
    Click Element   css:[type="submit"]
    Page Should Contain    ${UserName}


删除用户话题
    Click Element   css:span[class="user_name"]>a
    Click Element   css:div.cell a.topic_title
    Click Element   css:i[class="fa fa-lg fa-trash"]
    Handle Alert



*** Test Cases ***
删除帖子
    ${file_name}=   util.Get Current Time
    Log To Console  -----------------${file_name}-----------------
    testuser1成功登录
    删除用户话题
    #截屏
    [Teardown]      Capture Page Screenshot   ${file_name}.png
    # Close Browser
    