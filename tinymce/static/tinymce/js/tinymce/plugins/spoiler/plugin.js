/*
Spoiler plugin for TinyMCE 4 editor

It adds special markup that in combination with a site-side JS script
can create spoiler effect (hidden text that is shown on clik) on a web-page.
An example of a site-side script: https://jsfiddle.net/romanvm/7w9shc27/

(c) 2016, Roman Miroshnychenko <romanvm@yandex.ua>
License: LGPL <http://www.gnu.org/licenses/lgpl-3.0.en.html>
*/
tinymce.PluginManager.add('spoiler', function(editor, url)
{

  editor.contentCSS.push(url + '/css/spoiler.css');
  var spoilerCaption = editor.getParam('spoiler_caption', 'Spoiler!');

  function addSpoiler()
  {
    var selection = editor.selection;
    var node = selection.getNode();
    if (node) {
      editor.undoManager.transact(function() {
      var content = selection.getContent();
      if (!content) {
        content = 'Spoiler text.';
      }
      selection.setContent('<div class="spoiler" contenteditable="false">' +
                      '<div class="spoiler-toggle">' + spoilerCaption + ' </div>' +
                      '<div class="spoiler-text" contenteditable="true">' +
                      content +
                      '</div></div>');
      });
      editor.nodeChanged();
    }
  }

  function removeSpoiler()
  {
    console.log(editor.contentCSS);
    var selection = editor.selection;
    var node = selection.getNode();
    if (node && node.className == 'spoiler')
    {
      editor.undoManager.transact(function()
      {
        var newPara = document.createElement('p');
        newPara.innerHTML = node.getElementsByClassName('spoiler-text')[0].innerHTML;
        node.parentNode.replaceChild(newPara, node);
      });
      editor.nodeChanged();
    }
  }

  editor.addButton('spoiler-add',
  {
    tooltip: 'Add spoiler',
    image: url + '/img/eye-blocked.png',
    onclick: addSpoiler
  });
  editor.addMenuItem('spoiler-add',
  {
    text: 'Add spoiler',
    context: 'format',
    onclick: addSpoiler
  });
  editor.addButton('spoiler-remove',
  {
    tooltip: 'Remove spoiler',
    image: url + '/img/eye-plus.png',
    onclick: removeSpoiler
  });
  editor.addMenuItem('spoiler-remove',
  {
    text: 'Remove spoiler',
    context: 'format',
    onclick: removeSpoiler
  });
});
