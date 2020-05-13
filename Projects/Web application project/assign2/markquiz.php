<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initialscale=1.0">
  <link rel="stylesheet" href="styles/style.css" >
  <title>Mustang</title>
</head>
 
<body>
		<?php
			include_once("header.inc");
		?>
		<?php
			$servername = "feenix-mariadb.swin.edu.au";
			$username = "s101985810";
			$password = "150895";
			$dbname = "s101985810_db";

			// Create connection
			$conn = new mysqli($servername, $username, $password, $dbname);
			if ($conn->connect_error) {
				die("Connection failed: " . $conn->connect_error);
			} 
			
				// sql to create table
			$table = "CREATE TABLE attempts (
								attempt_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
								time TIMESTAMP,
								firstname VARCHAR(30) NOT NULL,
								lastname VARCHAR(30) NOT NULL,
								studentid VARCHAR(30) NOT NULL,
								attempt INT,
								score INT
								)";
			mysqli_query($conn,$table);
			$count=0;
			$studentid = $_POST["studentid"];
			$givenname = $_POST["givenname"];
			$familyname = $_POST["familyname"];
			$Place = $_POST["Place"];
			$mustang = $_POST["mustang"];
			$attempt = 1;
			
			if (strcmp('Gangabu',$Place)==0){
				$count=$count + 1;
			}
			if(strcmp('mustang',$mustang)==0){
				$count=$count + 1;
				}
			$numberofattempts = "SELECT attempt FROM attempts WHERE studentid = $studentid";
			$result = mysqli_query($conn, $numberofattempts);
			while($row = mysqli_fetch_assoc($result)) {
			$attempt = $row['attempt'];
			if ($attempt == 3) {
					echo "Maximum number of attempts:,  ",   $attempt ,"and Your score is:  ",  $count;
					$attempt=4;
			}
			else	{ 
				$attempt++;
			}
			}
			if ($attempt <= 3){
				$insert_query = "INSERT INTO attempts  (firstname,lastname,studentid,score,attempt)  VALUES ('$givenname','$familyname',$studentid,$count, $attempt)";			
				mysqli_query ($conn, $insert_query);
				echo "Your score is: ", $count;}
			$conn->close();
		?>

		<p><a href="quiz.php">Back to Quiz</a></p>
		<?php
			include_once("footer.inc");
		?>
			
</body>
</html>

