<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initialscale=1.0">
  <link rel="stylesheet" href="styles/style.css" >
  <link rel="stylesheet" media="screen and (max-width: 600px)" href="styles/style.css">
  <link rel="stylesheet" media="screen and (max-width: 400px)" href="styles/style.css">  
  <title>Mustang</title>
</head>
 
<body>
		<?php
			include_once("header.inc");
		?>
		
		<?php 
			$id = $_POST['search'];
			$score = $_POST['change'];
			$servername = "feenix-mariadb.swin.edu.au";
			$username = "s101985810";
			$password = "150895";
			$dbname = "s101985810_db";

			// Create connection
			$conn = new mysqli($servername, $username, $password, $dbname);
			if ($conn->connect_error) {
				die("Connection failed: " . $conn->connect_error);
			} 
			else {
					 // Upon successful connection
					 $sql_table="attempts";
					  
					 // Set up the SQL command to query or add data into the table
					 $query = "UPDATE attempts SET score=$score  WHERE studentid=$id";
					 // execute the query and store result into the result pointer
					 $result = mysqli_query($conn, $query);
					 // checks if the execution was successful
					 if(!$result) {
					 echo "<p>Something is wrong with ", $query, "</p>";
					 } 
					 // close the database connection
					 mysqli_close($conn);
					 // if successful database connection
				}
		?>
		
		<?php
			include_once("footer.inc");
		?>
			
</body>
</html>