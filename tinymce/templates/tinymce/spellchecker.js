function(method, text, success, failure) {
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
