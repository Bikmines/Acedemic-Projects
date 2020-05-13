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
			
			<div id="form">
				<form method="post" action="markquiz.php">
					<fieldset>
						<legend>Details</legend>
							<p>
								<label><strong>Student ID:</strong></label><input type="text" name="studentid" pattern = "[\d].{6,10}" required="required" />
								<label><strong>First Name:</strong></label><input type="text" name="givenname" pattern = "[A-Za-z].{2,20}" required="required" />
								<label><strong>Last Name:</strong></label><input type="text" name="familyname" pattern = "[A-Za-z].{2,20}" required="required" />
							</p>
							
					</fieldset>
					 
					<fieldset>
						<legend>Questionnaire</legend>
							<p>
								<label><strong>How old are you?</strong></label>
							</p>
								<p>
									<input type="number" name="age" required="required" />
								</p>
							
							<p> 
								<label><strong>Destination:</strong></label>
								<input type="radio" name="mustang" id="mustang" value="mustang" required="required" /><label for="Male">Mustang</label>
								<input type="radio" name="mustang" id="ghasa" value="ghasa" /><label for="Female">Ghasa</label>
								<input type="radio" name="mustang" id="other" value="other"/><label for="other">other</label>
							</p>
					 
							<p>
								<label><Strong>Buy ticket from:</strong></label>
									<select name="Place" required="required">
										<option selected="selected">Please Select</option>
										<option value="Gangabu">Gangabu</option>
										<option value="Ghasa">Ghasa</option>
										<option value="Beni">Beni</option>
									</select>
							</p>
							
							<p>
								<label><strong>Name of my hometown:</strong></label>
								<label for="Mustang">Mustang</label><input type="checkbox" name="language " value="mustang" id="Mustang" checked="checked"/>
								<label for="Ghasa">Ghasa</label><input type="checkbox" name="language" value="Ghasa" id="Ghasa" />
								<label for="jomsom">jomsom</label><input type="checkbox" name="language" value="jomsom" id="jomsom"/>
								<label for="Muktinath">Muktinath</label><input type="checkbox" name="language" value="Muktinath" id="Muktinath" />
								<label for="Kagbeni">Kagbeni</label><input type="checkbox" name="language" value="Kagbeni" id="Kagbeni" />
							</p>
							
							<p>
								<label><strong>Suggestions for improvement:</strong></label>
							</p>
							<p>
								<textarea name="description" cols="50" rows="5" >write description of your problems here: </textarea>
							</p>
							
							
							<p>
								<label><strong>Date:</strong></label><input type="date" name="date" />
							</p>
							<p>
								<label><strong>Time:</strong></label><input type="time" name="time" />
							</p>
					
					</fieldset>
					 
							<p>
								<input type="submit" name ="submit" value="Submit">
								<input type="reset" value="Reset Form">
							</p>
					
				</form>
					
			</div>
			<?php
			         include_once("footer.inc");
		       ?>
	</body>
</html>