<?php

class WatcherApi
{

	const STOP_ALARM = 0;
	const SERVER_PORT = 6789;
	private $maxSize = 1024;

	public function __construct(){
	}

	public function stopWatcher(){
		echo $_SERVER['SERVER_ADDR'];
		$result = $this->sendingSignalServer(json_encode(self::STOP_ALARM));
		return $result;
	}

	private function sendingSignalServer($instruction_num){
		$message = json_encode(array('flag' => self::STOP_ALARM,));

		if(($socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP)) === false) return "Could not create socket\n";
		if(socket_connect($socket, '172.16.1.26', self::SERVER_PORT) === false) return "Could not connect watcher server\n";
		if(socket_write($socket, $message, strlen($message)) === false) return "Could not send data to server\n";
		$result = socket_read ($socket, $this->maxSize);
		if ($result === null){
			return "Could not read server response\n";
		}
		socket_close($socket);
		return $result;
	}
}

?>
