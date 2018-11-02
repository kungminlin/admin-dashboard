$(document).ready(function(){
  $('#scrolly').click(function() {
    document.querySelector('#about').scrollIntoView({
      behavior: 'smooth'
    });
  });

  $('.overlay').height($('header').height() + $('main').height() + $('footer').height());

  $(window).resize(function() {
    $('.overlay').height($('header').height() + $('main').height() + $('footer').height());
  })
});