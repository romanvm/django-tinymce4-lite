/* Common JavaScript code for django-tinymce4-lite */
function getCookie(cname) {
  var name = cname + '=';
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i <ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return '';
}
var csrftoken = getCookie('csrftoken');
if (csrftoken) {
  tinymce.util.XHR.on('beforeSend', function(e) {
    e.xhr.setRequestHeader('X-CSRFToken', csrftoken);
  });
}
