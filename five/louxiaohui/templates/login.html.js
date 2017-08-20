<!DOCTYPE html>
<html class="">
  <head>
    <meta charset="utf-8">
    <title>Account Management</title>
    <meta name="viewport" content="width=device-width">
    <meta name="description" content="">
    <link rel="icon" href="http://www.51reboot.com/images/favicon.ico">
  </head>
  <body>
    <div id="container">
      <div id="tip" class=" notification">
        <p>
          
        </p>
      </div>
      <div id="body">
          <link rel="stylesheet" href="{{url_for('static', filename='login.css')}}">

<div id="login-register-page" class="form-container login">
  <div class="tabs register">
    <a class="tab register" href="/register/">
      <span>New to JS Bin</span>
      Register
    </a>
    <a class="tab login" href="/login">
      <span>Existing users</span>
      Login
    </a>
  </div>
  <div class="info "><p></p></div>
  <form action="/register" method="post" class="register">
    <div>
      <label for="signup-username">Username</label>
      <input name="username" id="signup-username" type="text" required pattern="[a-zA-Z0-9_\-]+" oninput="setCustomValidity('')" oninvalid="setCustomValidity('Only numbers, letters, underscore and dash are allowed in the username')">
    </div>
    <div>
      <label for="signup-email">Email address</label>
      <input name="email" id="signup-email" type="email" required>
    </div>
    <div>
      <label for="signup-key">Password</label>
      <input name="key" id="signup-key" type="password" required>
    </div>
    <div class="submit">
      <input type="submit" value="Register">
    </div>    <input type="hidden" name="_csrf" value="nQ4FbhYS-yeMJscSwamegNS0-GKe7C1CioZY">
    <input type="hidden" name="referrer" value="">
  </form>
  <form action="/login" method="post" class="login" id="login">
    <div>
      <label for="login-username">Email address or username</label>
      <input name="username" id="login-username" type="text" required value="">
    </div>
    <div>
      <label for="login-key">Password</label>
      <input name="passwd" id="login-key" type="password" required>
    </div>
      {% if error %}
      <span style='color:red'> {{error}} </span>
      {% endif %}
    <div class="submit">
      <input type="submit" value="Log in">
      <a id="lostpass" class="lostpass" href="https://jsbin.com/forgot">I've forgotten my password</a>
    </div>    <input type="hidden" name="_csrf" value="nQ4FbhYS-yeMJscSwamegNS0-GKe7C1CioZY">
    <input type="hidden" name="referrer" value="">
  </form>

</div>


  </body>
</html>
