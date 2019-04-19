<form action="sell.php" method="post">
    <fieldset>
        <div class="form-group">
            <input autofocus class="form-control" name="symbol" placeholder="symbol" type="text"/>
        </div>
        
        <div class="form-group">
            <button type="submit" class="btn btn-default">sell</button>
        </div>
        <table class="table table-striped">

    <thead>
   
        <tr>

            <th>Your shares Symbol</th>
            <th>Number of Shares you own</th>
        </tr>
    </thead>
    <tbody>
        
        <?php

            foreach ($rows as $row)
            {
                print("<tr>");
                print("<th>".$row["symbol"]. "</th>");
                print("<th>".$row["shares"]. "</th>");
                print("</tr>");

            }

        ?>
         </tbody>
</table>
    </fieldset>
</form>
<div>
    <a href="javascript:history.go(-1);">Back</a>
</div>
