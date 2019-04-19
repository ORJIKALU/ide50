<?php

    // configuration
    require("../includes/config.php"); 

    // if user reached page via GET (as by clicking a link or via redirect)
    if ($_SERVER["REQUEST_METHOD"] == "GET")
    {
        // else render form
        render("buy_form.php", ["title" => "Buy"]);
    }

    // else if user reached page via POST (as by submitting a form via POST)
    else if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        // validate submission
        if (empty($_POST["symbol"]))
        {
            apologize("You must provide your symbol.");
        }
        else if (empty($_POST["shares"]))
        {
            apologize("You must provide number of shares.");
        }

        // query database for user
        $rows = query("SELECT cash FROM users WHERE id = ?",$_SESSION["id"] );
        if(empty($rows))
        {
            apologize("you don't have money");
        }
        if(!preg_match("/^\d+$/", $_POST["shares"]))
        {
            apologize("non negative whole numbers required for shares");
        }
        $row = $rows[0];
        $stock = lookup($_POST["symbol"]);
        if($stock === false)
        {
            apologize("Invalid symbol");
        }
        $amount = $stock["price"]* $_POST["shares"];
        if($row["cash"] < $amount)
        {
            apologize("you do not have enough money to buy shares");
        }
        query("INSERT INTO portfolio (id, symbol, shares) VALUES(?, ?, ?) ON DUPLICATE KEY UPDATE shares = shares + ?",$_SESSION["id"],strtoupper($_POST["symbol"]),$_POST["shares"],$_POST["shares"]);
        query("UPDATE users SET cash = cash - ? WHERE id = ? ",$amount,$_SESSION["id"]);
        $action = "BUY";
        query("INSERT INTO history (id,action, time, symbol, shares, amount) VALUES(?, ?, NOW(), ?,?,?)",$_SESSION["id"],$action,strtoupper($_POST["symbol"]),$_POST["shares"],$amount);
        redirect("/");
           
    }

?>
