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
#list {
	text-align:left;
	width:300px;
	margin-left:auto;
	margin-right:auto;
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