const $ = window.$;
$('#toggle_header').click(function () {
  if ($('header').attr('class') === 'red') {
    $('header').addClass('green');
    $('header').removeClass('red');
  } else {
    $('header').addClass('red');
    $('header').removeClass('green');
  }
});
