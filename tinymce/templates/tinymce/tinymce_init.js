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
  tinyMCE.init(tinymce_config);
}
{% if not is_admin_inline %}
tinymce_init();
{% else %}
(function($) {
  $(document).off('formset:added').on('formset:added', function(event, $row, formsetName) {
    $('div#' + $row['0'].id + ' .tinymce4_editor').each(function(i, elem) {
      tinymce_init(elem.tagName + '#' + elem.id);
    });
  });
})(django.jQuery);
{% endif %}
