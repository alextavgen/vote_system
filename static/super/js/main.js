var utopia = $('#utopia')[0];
var end = $('#end')[0];
var intro_played = false;
var end_played = false;
var timeleft = 60;
var timer_set = false;

(function worker() {
  $.get('/super/api/call', function(data) {
    // Now that we've completed the request schedule the next one.
    var data = $.parseJSON(data);
    console.log(data.command==="intro")
    console.log("intro " + intro_played);
    console.log("command " + data.command);
    console.log("payload " + data.payload);
    console.log("timer " + timer_set);

    if (!intro_played) {
      utopia.play();
      console.log("play");
      intro_played = true;
    }


    if (data.command==="wait") {

    }
     else if (data.command === "voting") {
      //utopia.stop();
      $('.result').html(data.payload);
      $('.result-text').html(data.text);
        if (!timer_set) {
          var downloadTimer = setInterval(function () {
            timeleft--;
            document.getElementById("countdowntimer").textContent = timeleft < 10 ? "00:0" + timeleft : "00:" + timeleft;
            if (timeleft <= 0)
              clearInterval(downloadTimer);
          }, 1000);
          timer_set = true;
        }
      }
      else if (data.command==="end"){
      console.log("command_end");
      if (!end_played){
        end.play();
        console.log("play");
        end_played = true;
      }

    }
    setTimeout(worker, 1000);

  });
})();


