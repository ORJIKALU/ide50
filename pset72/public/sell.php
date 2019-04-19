<?php


// configuration
require("../includes/config.php");


// if user reached page via GET (as by clicking a link or via redirect)
if ($_SERVER["REQUEST_METHOD"] == "GET")
{
    $rows = query("SELECT * FROM portfolio WHERE id = ?",$_SESSION["id"]);
    
    // render form
    render("sell_form.php", ["title" => "Sell", "rows" => $rows]);

}
// else if user reached page via POST (as by submitting a form via POST)
else if ($_SERVER["REQUEST_METHOD"] == "POST")
{
    if(empty($_POST["symbol"]))
    {
        apologize("symbol is empty");
    }
    else
    {
        $stock = lookup($_POST["symbol"]);
        if($stock === false)
        {
            apologize("invalid symbol");
        }
        $symbols = query("SELECT * FROM portfolio WHERE id = ? AND symbol = ?",$_SESSION["id"],strtolower($_POST["symbol"])); 
        if(empty($symbols))
        {
           apologize("You don't own any share of that symbol");
        }
        foreach ($symbols as $symbol)
        {
            $symbo = $symbol;
        }
        $earning = $stock["price"]*$symbo["shares"];
        $action = "SELL";

        query("UPDATE users SET cash = cash + ? WHERE id = ? ",$earning,$_SESSION["id"]);
        $que = query("INSERT INTO history (id,action, time, symbol, shares, amount) VALUES(?, ?, NOW(), ?,?,?)",$_SESSION["id"],$action,strtoupper($_POST["symbol"]),$symbo["shares"],$earning);
        query("DELETE FROM portfolio WHERE id = ? AND symbol = ?",$_SESSION["id"],strtolower($_POST["symbol"]));
        if($que === false)
        {
            apologize("cound query");
        }
        
    }  

        redirect("/");

}

?>
