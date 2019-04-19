<?php

    // configuration
    require("../includes/config.php"); 
    
    if(empty($_SESSION["id"]))
    {
        redirect("login.php");
    }
    else
    {
        
        $rows = query("SELECT symbol, shares FROM portfolio WHERE id = ?", $_SESSION["id"]);
        $cashrows = query("SELECT cash FROM users WHERE id = ?", $_SESSION["id"]);
        $positions = [];

        
        foreach ($rows as $row)
        {
            $stock = lookup($row["symbol"]);
            $total = $stock["price"] * $row["shares"];
            
            if ($stock !== false)
            {
                $positions[] = [
                "name" => $stock["name"],
                "price" => '$'.number_format($stock["price"], 2),
                "shares" => $row["shares"],
                "symbol" => $row["symbol"],
                "total" => '$'.number_format($total, 2)
                ];
            }

        }

        $balance;
        foreach ($cashrows as $cash)
        {
          $balance = number_format($cash["cash"],2);
        }
        render("portfolio.php", ["title" => "portfolio", "positions" => $positions, "cash" => '$'.$balance]);
    }
    
   
?>
