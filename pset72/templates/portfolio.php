<ul class="nav nav-pills">
    <li><a href="quote.php">Quote</a></li>
    <li><a href="buy.php">Buy</a></li>
    <li><a href="sell.php">Sell</a></li>
    <li><a href="history.php">History</a></li>
</ul>
<table class="table table-striped">

    <thead>
   
        <tr>
            <th>Symbol</th>
            <th>Name</th>
            <th>Shares</th>
            <th>Price</th>
            <th>TOTAL</th>
        </tr>
    </thead>
    <tbody>
        
        <?php

            foreach ($positions as $position)
            {
                print("<tr>");
                print("<th>".$position["symbol"]."</th>");
                print("<th>".$position["name"]. "</th>");
                print("<th>".$position["shares"]."</th>");
                print("<th>".$position["price"]."</th>");
                print("<th>".$position["total"]."</th>");
                print("</tr>");

            }
             
         print("<tr><th>YOUR CASH: .'$'.".$cash."</th></tr>");              

        ?>
        

    </tbody>
</table>
<div>
    <a href="logout.php"><b>Log Out</b></a>
</div>
<div>
    <a href="password.php"><b>Change password</b></a>
</div>


