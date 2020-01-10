***Settings***
Documentation       常用操作
Library             SeleniumLibrary
Library             ../test_samples/util.py
Library             RegisiterPage.py
Variables           variables.py




***Variables***
${Server_Url}           http://39.107.96.138:3000/
${Browser}              chrome
${valid_username}       zhangsan01
${valid_password}       123456
${valid_repassword}     123456
${valid_email}          zhangsan01@gmail.com



***Keywords***
打开浏览器到注册页面
    Open Browser    ${Server_Url}  ${Browser}
    Maximize Browser Window
    Click Element   css:a[href="/signup"]

截屏并清除cookie
    ${filename}=    get current time
    Capture Page Screenshot     ${filename}.png
    Delete All Cookies

关闭浏览器
    Close Browser

输入用户名
    [Arguments]     ${username}
    ${usernameId}=  get username
    Log To Console  +++++++++++++++++++${usernameId}++++++++++++++++++++
    Input Text      id:${usernameId}    ${username}
输入密码
    [Arguments]     ${password}
    Input Text      id:pass         ${password}

确认密码
    [Arguments]     ${repass}
    Input Text      id:re_pass       ${repass}
    
输入电子邮件
    [Arguments]     ${email}
    Input Text      id:email        ${email}