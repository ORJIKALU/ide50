
<table class="table table-striped">

    <thead>
    


    
        <tr>
            <th>Action</th>
            <th>Time</th>
            <th>Symbol</th>
            <th>Shares</th>
            <th>Amount</th>
        </tr>
    </thead>
    <tbody>
        
        <?php

            foreach ($rows as $row)
            {
                print("<tr>");
                print("<th>".$row["action"]."</th>");
                print("<th>".$row["time"]. "</th>");
                print("<th>".$row["symbol"]."</th>");
                print("<th>".$row["shares"]."</th>");
                print("<th>".'$'.$row["amount"]."</th>");
                print("</tr>");

            }
             

        ?>
        

    </tbody>
</table>
<div>
    <a href="javascript:history.go(-1);">Back</a>
</div>

