var http = require('http');
var sys = require('sys');
var io = require('./vendor/Socket.IO-node/lib/socket.io');
var wina = require('./vendor/wina');

var server = wina.createServer('./static');

server.listen(8888, "0.0.0.0");


// socket.io, I choose you
var socket = io.listen(server);
socket.addListener("clientConnect", function(client) {
  sys.debug("client connected: " + client);
  client.send("hello world");
});

socket.addListener("clientDisconnect", function(client) {
  sys.debug("client disconnected: " + client);
});

socket.addListener("clientMessage", function(message, client) {
  sys.debug("client: " + client + ", message: " + message);
  client.send("echo: " + message);
});
