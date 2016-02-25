tinyMCE.init({
  {% for key, value in callbacks.items %}
    '{{ key }}': {{ value|safe }},
  {% empty %}
  {% endfor %}
  {{ tinymce_config|safe }}
}); // end init
