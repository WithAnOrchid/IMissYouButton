'use strict';

const https = require('https');
var querystring = require('querystring');

module.exports = (access_token, callback) => {
    console.log('In sendMsg: ' + access_token);
    var beijing_time = new Date(new Date().getTime() + 28800000);

    var post_data = JSON.stringify({
        "touser": "LiuDi",
        "msgtype": "text",
        "agentid": 1000003,
        "text": {
            "content": "*******嘿，我这现在是*******\n" + 
            beijing_time.getFullYear() + "年" + 
            beijing_time.getMonth()+1 + "月" + 
            beijing_time.getDate() + "日" + 
            beijing_time.getHours() + "时" +
            beijing_time.getMinutes() + "分" + 
            beijing_time.getSeconds() + "秒" +
            "\n\n我想你了[跳跳]"
        },
        "safe": 0
    });

    var post_options = {
        "host": "qyapi.weixin.qq.com",
        "path": "/cgi-bin/message/send?access_token=" + access_token,
        "method": "POST",
        "headers":{
            'Content-Type': 'application/json',
            'Content-Length': Buffer.byteLength(post_data)}
        };
    var req = https.request(post_options, function(res) {
        res.setEncoding('utf8');
        res.on('data', function(chunk) {
            console.log('Response: ' + chunk);
        });
        res.on('error', function(e) {
            context.fail('error:' + e.message);
        });
    });
    req.write(post_data);
    req.end();
};
