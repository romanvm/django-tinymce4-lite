/*
Save and continue plugin for TinyMCE 4 to use with Django

It adds 'Save and continue editing' command to 'File' menu and 
the respective button for TinyMCE toolbar.

(c) Roman Miroshnychenko, <romanvm@yandex.ua>, 2016
License: LGPL <http://www.gnu.org/licenses/lgpl-3.0.en.html>
*/
tinymce.PluginManager.add('django_saveandcontinue', function(editor, url) {

  function saveAndContinue() {
    var continue_btn_name = editor.getParam('django_saveandcontinue_btn_name', '_continue');
    var continue_btn = document.getElementsByName(continue_btn_name)[0];
    continue_btn.click();
  }
  
  editor.addButton('django_saveandcontinue', {
    tooltip: 'Save and continue editing',
    image: url + '/img/cloud-upload.png',
    onclick: saveAndContinue
  });

  editor.addMenuItem('django_saveandcontinue', {
    text: 'Save and continue editing',
    context: 'file',
    onclick: saveAndContinue
  });
});
