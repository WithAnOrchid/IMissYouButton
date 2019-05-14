'use strict';

const getToken = require('./getToken.js');
const sendMsg = require('./sendMsg.js');

module.exports.handler = (event, context, callback) => {
  var access_token = '';
  getToken(event, (error, access_token) => {
    console.log('result1:', access_token);
    sendMsg(access_token, (error, result) => {
      console.log('result2:', result);
    });
  });
};
