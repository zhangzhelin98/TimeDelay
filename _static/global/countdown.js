const countdown_timer = function(){
    let mins = 10; // ここを変えれば指定の minutes にできます
    let secs = mins * 60;
    let msecs = secs * 1000;
    let start_date = new Date();
    let end_date = new Date(start_date.getTime() + msecs);
    let current_mins = 0;
    let current_secs = 0;
    let current_msecs = 0;

    $('.target').append(
      '<div class="countdown_timer">'
      + '<p class="time">あと<span class="mins">'+mins+'</span>分<span class="secs">00</span>秒<span class="msecs">00</span></p>'
      + '</div>'
    );
    
    if ((navigator.userAgent.indexOf('iPhone') > 0 || navigator.userAgent.indexOf('Android') > 0 && navigator.userAgent.indexOf('Mobile') > 0 || navigator.userAgent.indexOf('iPad') > 0 || navigator.userAgent.indexOf('Android') > 0)) {
      $('.text_attention').html('※このページが表示されてから、<br>60分間の限定割引になります。');
    }
  
    let timer = setInterval(function(){
      let now_date = new Date();

      current_mins = Math.floor(((end_date - now_date) % (24 * 60 * 60 * 1000)) / (60 * 1000)) % 60;
      current_secs = Math.floor(((end_date - now_date) % (24 * 60 * 60 * 1000)) / 1000) % 60 % 60;
      current_msecs = Math.floor(((end_date - now_date) % (24 * 60 * 60 * 1000)) / 10) % 100;
  
      if(current_mins <= 9) {
        current_mins = "0" + current_mins;
      }
      if(current_secs <= 9) {
        current_secs = "0" + current_secs;
      }
      if(current_msecs <= 9){
        current_msecs = "0" + current_msecs;
      }
  
      $(".time").html(
        'あと'
        + '<span class="font_size_xl">' + current_mins + '</span>'
        + '分'
        + '<span class="font_size_xl">' + current_secs + '</span>'
        + '秒'
        + '<span class="font_size_xl">' + current_msecs + '</span>'
      );
    },10);
}

countdown_timer();