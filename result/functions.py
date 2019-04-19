{% extends "layout.html" %}

{% block title %}
    Register
{% endblock %}

{% block main %}
<div class="form-w3ls">

    <form action="/register" method="post">
				<p class="header">User Name</p>
				<input type="text" name="username" placeholder="User Name" onfocus="this.value = '';" onblur="if (this.value == '') {this.value = 'User Name';}" required="required">
        <div class="form-group">
            <input class="form-control" name="schoolname" placeholder="schoolname" type="text"/>
        </div>
        <div class="form-group">
            <input class="form-control" name="surname" placeholder="surname" type="text"/>
        </div>
        <div class="form-group">
            <input class="form-control" name="firstname" placeholder="firstname" type="text"/>
        </div>
        <div class="form-group">
            <input class="form-control" name="othername" placeholder="othername" type="text"/>
        </div>
        <div class="form-group">
            <input class="form-control" name="email" placeholder="email" type="text"/>
        </div>
         <div class="form-group">
            <input class="form-control" name="motto" placeholder="motto" type="text"/>
        </div>
         <div class="form-group">
            <input class="form-control" name="phone" placeholder="phone number" type="text"/>
        </div>
        <div class="form-group">
            <input autocomplete="off" autofocus class="form-control" name="address" placeholder="address" type="text"/>
        </div>
        <div class="form-group">
            <input class="form-control" name="password" placeholder="Password" type="password"/>
        </div>
        <div class="form-group">
            <input class="form-control" name="confirmation" placeholder="Password" type="password"/>
        </div>
        <div class="form-group">
            <input class="form-control" name="admin_password" placeholder="admin Password" type="password"/>
        </div>
        <div class="form-group">
            <input class="form-control" name="admin_password_confirmation" placeholder="confirm admin Password" type="password"/>
        </div>
        
        <button class="btn btn-primary" type="submit">Register</button>
    </form>
</div>
<!-- js files -->
	<script src='/static/js/jquery.min.js'></script>
	<script src="/static/js/register.js"></script>
<!-- /js files -->
{% endblock %}
