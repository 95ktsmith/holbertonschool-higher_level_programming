const $ = window.$;
$('#update_header').click(function () {
  $('HEADER').text(function (i, origText) {
    return 'New Header!!!';
  });
});
