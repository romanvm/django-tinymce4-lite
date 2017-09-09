(function($) {
  function tinymce_init(selector) {
    var tinymce_config = {
      {% for key, value in callbacks.items %}
        '{{ key }}': {{ value|safe }},
      {% empty %}
      {% endfor %}
      {{ tinymce_config|safe }}
    };
    if (typeof selector != 'undefined') {
      tinymce_config['selector'] = selector;
    }
    tinymce.init(tinymce_config);
  }
{% if not is_admin_inline %}
  tinymce_init();
})();
{% else %}
  // Add an event listener to initialise TinyMCE editors in
  // the new inline formset in Django admin.
  $(document).on('formset:added', function(event, $row, formsetName) {
    $row.find('.tinymce4_editor').each(function(i, elem) {
      tinymce_init(elem.tagName + '#' + elem.id);
    });
  });
  // Add and event listener to remove TinyMCE editors from the removed formset.
  $(document).on('formset:removed', function(event, $row, formsetName) {
    $row.find('.tinymce4_editor').each(function(i, elem) {
      var i;
      for (i = 0; tinymce.EditorManager.editors.length; i++) {
        if (tinymce.EditorManager.editors[i].id == elem.id) {
          tinymce.EditorManager.editors[i].remove();
          break;
        }
      }
    });
  });
})(django.jQuery);
{% endif %}
