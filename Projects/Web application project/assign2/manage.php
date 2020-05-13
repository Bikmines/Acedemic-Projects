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
		<ul>
			<li>	<a href="list1.php">list all attempts</a></li>
			<li>	<a href="manage1.php">list all attempts for a particular student</a></li>
			<li>	<a href="list3.php"> list all students (id, first and last name) who got 100% on their first attempt</a></li>
			<li>	<a href="list4.php">list all students (id, first and last name) got less than 50% on their third attempt</a></li>
			<li>	<a href="manage2.php">delete all attempts for a particular student (given a student id)</a></li>
			<li>	<a href="manage3.php">change the score for a quiz attempt (given a student id)</a></li>
		</ul>
		
		<?php
			include_once("footer.inc");
		?>
			
</body>
</html>