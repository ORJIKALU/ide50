<?php


// configuration
require("../includes/config.php");


// if user reached page via GET (as by clicking a link or via redirect)
if ($_SERVER["REQUEST_METHOD"] == "GET")
{

// else render form
render("register_form.php", ["title" => "Register"]);

}
// else if user reached page via POST (as by submitting a form via POST)
else if ($_SERVER["REQUEST_METHOD"] == "POST")
{
// TODO

if(empty($_POST["username"]))
{
    apologize("username is empty");
}

else if(empty($_POST["password"]))
{
    apologize("password is empty");
}
else if(empty($_POST["comfirmation"]))
{
    apologize("confirm password");
}
else if(empty($_POST["email"]))
{
    apologize("Email is empty");
}
else if($_POST["password"] != $_POST["comfirmation"] )
{
    apologize("passwords do not match");
}

else
{
    
    $emailck = query("SELECT email FROM users WHERE email = ?", $_POST["email"]);
    if($emailck)
    {
        apologize("email already exist");
    }  
    $check = query("INSERT INTO users (username, hash, cash, email) VALUES(?, ?, 10000.00, ?)",$_POST["username"], crypt($_POST["password"]),$_POST["email"]);
    if($check === false)
    {
        apologize("username already exist");
    }
    else
    {
        $rows = query("SELECT LAST_INSERT_ID() AS id");
        $id = $rows[0]["id"];
        $_SESSION["id"] = $id;
        redirect("index.php");
    }
}

}
?>
