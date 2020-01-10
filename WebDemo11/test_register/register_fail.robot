***Settings***
Documentation       主要测试注册失败的场景

Library             SeleniumLibrary
Suite Setup         打开浏览器到注册页面
# Test Setup
Test Teardown       截屏并清除cookie
Suite Teardown      关闭浏览器
Test Template       用户注册失败的几个场景
Resource            resource.robot



*** Test Cases ***          username        password            repassword              email
用户名为空                  ${EMPTY}        ${valid_password}   ${valid_repassword}     ${valid_email}
密码为空                    ${valid_username}       ${EMPTY}   ${valid_repassword}     ${valid_email}
确认密码为空                ${valid_username}        ${valid_password}   ${EMPTY}     ${valid_email}
email为空                  ${valid_username}        ${valid_password}   ${valid_repassword}     ${EMPTY}
用户名密码正确              ${valid_username}       ${valid_password}   ${valid_repassword}     ${valid_email}
                    


***Keywords***
用户注册失败的几个场景
    [Arguments]     ${username}     ${password}     ${repassword}   ${email}
    输入用户名      ${username}
    输入密码        ${password}
    确认密码        ${repassword}
    输入电子邮件    ${email}