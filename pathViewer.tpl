<!DOCTYPE html>
<html>
<head>
<title>
Wiki Racing Path Finder
</title>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<br />
<br />
<h1 id="header">Wikipedia Racing Path Finder</h1>
<br />
<br />
<div id="main">
<h1>Best Path</h1>
<ol>
% for element in path:
	<li id="list">{{element}}</li>
%end
</ol>
<br />
<br />
<br />
<p>Took <b>{{time}}</b> seconds to find the best path.</p>
<br />
<br />
<br />
<br />
<p style="text-align:left;">By: <i>Joseph Batchik</i> - CSH</p>	
</div>
</body>
</html>