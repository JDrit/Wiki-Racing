<!DOCTYPE html>
<html>
<head>
<title>
Wiki Racing Path Finder
</title>
<link rel="stylesheet" type="text/css" href="/static/style.css">
<link rel="shortcut icon" href="/static/favicon.ico">
<script type="text/javascript" src="/static/spin.js"></script>
<script type="text/javascript">
	function startSpinner() {
		if (document.getElementById("wait").innerHTML == "") {
			var opts = {
				lines: 13, // The number of lines to draw
				length: 7, // The length of each line
				width: 4, // The line thickness
				radius: 10, // The radius of the inner circle
				corners: 1, // Corner roundness (0..1)
				rotate: 0, // The rotation offset
				color: '#000', // #rgb or #rrggbb
				speed: 1, // Rounds per second
				trail: 60, // Afterglow percentage
				shadow: false, // Whether to render a shadow
				hwaccel: false, // Whether to use hardware acceleration
				className: 'spinner', // The CSS class to assign to the spinner
				zIndex: 2e9, // The z-index (defaults to 2000000000)
				top: 'auto', // Top position relative to parent in px
				left: '325' // Left position relative to parent in px
			};
			
			document.getElementById("wait").innerHTML = "Processing, please wait";
			var target = document.getElementById('spin');
			var spinner = new Spinner(opts).spin(target);
		}
	};
</script>
</head>
<body id="body">
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
	<form method="POST" action="/">
		<input name="start" type="text" />
        <input name="end" type="text" />
		<input type="submit" onclick="startSpinner()"/>
	</form>
<br />
<br />
<br />
<div id="spin"><div id="wait"></div></div>
<br />
<br />
<br />
<br />
<p><b>Warning:</b> The server could take up to 60 seconds to respond depending on the length of the path between articles</p>
<br />
<br />
<br />
<br />
<p style="text-align:left;">By: <i>Joseph Batchik</i> - CSH</p>
</div>
</body>
</html>