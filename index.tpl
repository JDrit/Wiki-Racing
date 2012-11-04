<!DOCTYPE html>
<html>
<head>
<title>
Wiki Racing Path Finder
</title>
<style media="screen" type="text/css">
#main {
	width:900px;
	margin-left:auto;
	margin-right:auto;
	border-style:sold;
	border-style:solid;
	border-width:5px;
	text-align:center;
	background-color:#ffffff;
	padding: 25px;
}
#header {
	width:900px;
	margin-left:auto;
	margin-right:auto;
	text-align:center;
	font-size:250%;
}
</style>
</head>
<body style="background-color:#009900;">
<br />
<br />
<h1 id="header">Wikipedia Racing Path Finder</h1>
<br />
<br />
<div id="main">
	<br />
	<br />
	<h1>{{message}}</h1>
	<br />
	<form method="POST" action="/path">
		<input name="start" type="text" />
        <input name="end" type="text" />
		<input type="submit" />
	</form>
<br />
<br />
<br />
<br />
<p><b>Warning:</b> The server could take up to 60 seconds to respond depending on the length of the path between articles</p>
<br />
<br />
<br />
<br />
<p style="text-align:left;">By: <i>Joseph Batchik</i></p>
</div>
</body>
</html>