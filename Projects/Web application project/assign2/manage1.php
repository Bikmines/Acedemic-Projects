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
		<form method="post" action="list2.php">
			<label><strong>Student ID:</strong></label><input type="text" name="search"  required="required" />
			<input type="submit" name ="submit">
		</form>
		<?php
			include_once("footer.inc");
		?>
			
</body>
</html>