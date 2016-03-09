$(document).ready(function() {
  $('#search-form').submit(function(e) {
    e.preventDefault();
    var theUrl = "https://api.twitter.com/1.1/search/tweets.json?q=" + $('#search-field').val();
    //debugger
    $.ajax({
             url: theUrl,
             dataType: 'json',
             type: "GET",
             beforeSend: function(xhr){
                xhr.setRequestHeader('Access-Control-Allow-Origin','http://localhost:8000'),
                xhr.setRequestHeader('X-Target-URI', "https://api.twitter.com"),
                xhr.setRequestHeader('Connection', "Keep-Alive")
              }
    })
    .done(function(response){
      console.log(response);
    })
  })
})