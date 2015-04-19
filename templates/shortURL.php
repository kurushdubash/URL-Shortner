$expectedURL = trim($_SERVER['URL']);
$split = preg_split("{:80\/}",$expectedURL);
$shortURL = $split[1];
// security: strip all but alphanumerics & dashes


$isShortURL = false;
$result = getLongURL($shortURL);
if ($result) { $isShortURL = true; }
$longURL = $result['longURL'];

if ($isShortURL)
{
	redirectTo($longURL, $shortURL);
} else {
	show404();  // no shortURL found, display standard 404 page
}

function getLongURL($s)
{
	// define these variables for your system
	$host = ""; $user = ""; $pass = ""; $db = "";
	$mysqli = new mysqli($host, $user, $pass, $db);
	// you may just want to fall thru to 404 here if connection error
	if (mysqli_connect_errno()) { die("Unable to connect !"); }
	$query = "SELECT * FROM urls WHERE shorturl = '$s';";
	if ($result = $mysqli->query($query)) {
	    if ($result->num_rows > 0) {
		while($row = $result->fetch_assoc()) {
			return($row);
		}
	    } else {
	    	return false;
	    }
	} else {
		return false;
	}
	$mysqli->close();
}

function redirectTo($longURL)
{
	// change this to your domain
	header("Referer: http://www.your-domain-here.com");
	// use a 301 redirect to your destination
	header("Location: $longURL", TRUE, 301);
	exit;
}

function show404()
{
	// display/include your standard 404 page here
	echo "404 Page Not Found.";
	exit;
}