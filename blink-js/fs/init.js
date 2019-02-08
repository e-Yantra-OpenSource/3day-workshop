load('api_config.js');
load('api_rpc.js');
load('api_timer.js');
load('api_gpio.js');

let pin = Cfg.get('app.pin');

let ledState = 0;
GPIO.setup_output(2, ledState);

Timer.set(Cfg.get('app.interval'), Timer.REPEAT, function() {
	let value = GPIO.toggle(2);   
	print(value ? 'Tick' : 'Tock');
}, null);
