const $ = window.$;
$(document).ready(function () {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.get(url, function (data) {
    $('#hello').text(function () {
      return data.hello;
    });
  });
});
