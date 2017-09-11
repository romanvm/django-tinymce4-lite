// Spellchecker callback function for TinyMCE 4

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

function tinymce4_spellcheck(method, text, success, failure) {
  tinymce.util.JSONRequest.sendRPC(
  {
    url: '{% url "tinymce-spellchecker" %}',
    method: 'spellcheck',
    params: {
      lang: this.getLanguage(),
      text: text
    }, // end params
    success: function(result) {
      success(result);
    }, // end success
    error: function(error, xhr) {
      failure('Spellcheck error: ' + error);
    } // end error
  }); // End sendRPC
} // end spellchecker_callback
