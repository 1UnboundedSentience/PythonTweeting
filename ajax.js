// var sampleTweets = require('results.json');
// console.log(sampleTweets);

$(document).ready(function() {
  $('#search-form').submit(function(e) {
    e.preventDefault();
    var theUrl = "https://api.twitter.com/1.1/search/tweets.json?q=" + $('#search-field').val();
    //<?php $url = $_GET['url'];
    //exec("python request.py $url"); ?>
    $.ajax({
             url: theUrl,
             dataType: 'json',
             type: "GET",
             headers: {
                'Access-Control-Allow-Origin':'*',
                'x-frame-options':'SAMEORIGIN',
                'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, PUT, PATCH, DELETE',
                'Access-Control-Allow-Headers': 'X-Requested-With,content-type',
                'Access-Control-Allow-Credentials': true,
                'Authorization': 'Oauth oauth_consumer_key="DC0sePOBbQ8bYdC8r4Smg",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1457485404",oauth_nonce="2100811271",oauth_version="1.0",oauth_token="1035256117-uQWBnMbSQUcUvuMXP5OOTMAjIvWeg2xWa9nGcT7",oauth_signature="jGStb8Sm66qJiAjDzwFM05RHeGs%3D"'
              }
    })
    .done(function(response){
      console.log(response);
      var randomTweetId = Math.random()*response["statuses"].length;
      response["statuses"][randomTweetId]
    })
  })
})