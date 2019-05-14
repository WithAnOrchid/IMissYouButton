'use strict';

const https = require('https');

module.exports = (event, callback) => {
        var get_options = {
        "host": "qyapi.weixin.qq.com",
        "path": "/cgi-bin/gettoken?corpid=SOMEID&corpsecret=SOMESECRET",
        "method": "GET"
        };
    const req = https.request(get_options, (res) => {
        let body = '';
        console.log('Status:', res.statusCode);
        console.log('Headers:', JSON.stringify(res.headers));
        res.setEncoding('utf8');
        res.on('data', (chunk) => body += chunk);
        res.on('end', () => {
            console.log('Successfully processed getToken');
            body = JSON.parse(body);
            callback(null, body.access_token);
        });
    });
    req.end();
};
