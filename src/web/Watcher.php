<!DOCTYPE html>
<head><meta charset="UTF-8">
	<title>Watcher</title>
</head>
<?php
require_once("WatcherApi.php");
function h($str) {
	return htmlspecialchars($str, ENT_QUOTES, 'UTF-8');
}
$order = (string)filter_input(INPUT_POST, 'order');
if ($_SERVER['REQUEST_METHOD'] === 'POST' ) {
	$a = new WatcherApi();
	echo $a->stopWatcher();
} else {
	echo 'not clear';
	echo $_SERVER['REMOTE_ADDR'];
}

?>

<h1>Watcher</h1>
<section>
	<h2>Watcher停止</h2>
	<form action="" method="post">
		本文: <input type="hidden" name="order" value="WatcherStop"><br>
		<input type="submit" value="WatcherStop">
	</form>
</section>
