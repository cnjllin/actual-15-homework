前端三剑客

html:前端骨架
  form :负责V端用户输入数据，并传到C端
  table:渲染/展示M端数据
  div  :把form table放到页面好看的位置-布局

css:页面美化
   <style="color:red">
  
bootstrap: HTML+css
   1、引入css
   2、表格、表单、按钮、文字
   3、栅栏-布局  12宫格


简单粗暴实现jQuery快速入门三步走
Js:
   1、who 操作谁 --select
   2、how 怎么操作 --action
   3、when 什么时候操作 --event

介绍jQuery核心三要素，选择器、动作、事件

选择器
    $('元素名').动作 ：元素选择器，所有HTML的标签元素都可以作为选择器，慎用，危险
    
   <div id="aa" class="test"></div>
   <div id="bb" class="test"></div>
    $('#aa').动作：     ID选择器，每一个被操作的标签，都必须定义一个id，常用,适用于单个元素的操作
    $('.test').动作：类选择器，会同时对这个列名的元素批量操作，适用于同类元素批量操作的场景
  

动作：
    html() vs html(value) 操作元素
    val() vs val(value) 操作表单

事件：
    $("button").click(function(){
    操作内容
})
ajax

首页：
判断是否有session,没有跳转至登录界面，管理员跳转至管理员界面，普通用户跳转至普通用户界面

用户登录：
用户名错误提示错误信息，密码错误提示错误信息，登陆成功跳转至相应用户界面

管理员界面：

用户个人信息，用户列表，添加用户，删除用户

普通用户：
用户个人信息

用户注册：
用户名存在提示错误信息，注册成功登陆

没有修改用户信息和密码
