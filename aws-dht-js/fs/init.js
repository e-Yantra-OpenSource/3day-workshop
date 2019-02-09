load('api_config.js');
load('api_rpc.js');
load('api_dht.js');
load('api_timer.js');
load('api_gpio.js');
load('api_mqtt.js');

// Configuration for devices attached to the thing
let led = Cfg.get('app.led');
let dhtPin = Cfg.get('app.dht');

// Getting name of the thing from config
let thingName = "thing81";

// Setting pin mode for led as output
let ledState = 0;
GPIO.setup_output(led, ledState);

// Creating dht object
let dht = DHT.create(dhtPin, DHT.DHT11);

// All AWS thing shadow topics
let updateTopic = "$aws/things/" + thingName + "/shadow/update";
let updateAcceptedTopic = "$aws/things/" + thingName + "/shadow/update/accepted";
let updateRejectedTopic = "$aws/things/" + thingName + "/shadow/update/rejected";
let updateDeltaTopic = "$aws/things/" + thingName + "/shadow/update/delta";

// function to publish data to thing shadow
function report() {
  print ("Reporting LED state as: ", ledState);
  let topic = updateTopic;
    // TODO
    let message = JSON.stringify({
      "state":{
       "reported":{
          "device165.388": ledState, //for led
          "device164.386": dht.getTemp(), //for temperature
          "device164.387": dht.getHumidity() //for humidity
       }
     }
  });

  MQTT.pub(updateTopic, message, 1);
}

// calls report method after 5000 seconds
Timer.set(Cfg.get('app.interval'), Timer.REPEAT, function() {
  report();
}, null);

// Subscription to AWS thing shadow topics
MQTT.sub(updateAcceptedTopic, function(conn, topic, msg) {
  print('Topic:', topic, 'message:', JSON.stringify(msg));
}, null);

MQTT.sub(updateRejectedTopic, function(conn, topic, msg) {
  print('Topic:', topic, 'message:', JSON.stringify(msg));
}, null);

MQTT.sub(updateDeltaTopic, function(conn, topic, msg) {
  print('Topic:', topic, 'message:', JSON.stringify(msg));
  let m = JSON.parse(msg);
  // TODO
  if (m.state["device165.388"] === 1) {
    ledState = 1;
    GPIO.write(led, ledState);
  }
  else {
    ledState = 0;
    GPIO.write(led, ledState);
  }
  report();
}, null);
