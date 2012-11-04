<!DOCTYPE html>
<html>
<head>
<title>
Wiki Racing Path Finder
</title>
<style media="screen" type="text/css">
#main {
	width: 900px ;
	margin-left: auto ;
	margin-right: auto ;
}
</style>
</head>
<body>
<br />
<br />
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
</div>
</body>
</html>