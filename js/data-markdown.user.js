// ==UserScript==
// @name Use Markdown, sometimes, in your HTML.
// @author Paul Irish <http://paulirish.com/>
// @link http://git.io/data-markdown
// @match *
// ==/UserScript==


// If you're not using this as a userscript just delete from this line up. It's cool, homey.

(function boom(){
  
  if (!window.Showdown){
    var scr = document.createElement('script');
    scr.onload = boom;
    scr.src = 'https://raw.github.com/github/github-flavored-markdown/gh-pages/scripts/showdown.js';
    document.body.appendChild(scr);
    return;
  }

  [].forEach.call( document.querySelectorAll('[data-markdown]'), function  fn(elem){
      
    // strip leading whitespace so it isn't evaluated as code
    var text      = elem.innerHTML.replace(/\n\s*\n/g,'\n'),
        // set indentation level so your markdown can be indented within your HTML
        leadingws = text.match(/^\n?(\s*)/)[1].length,
        regex     = new RegExp('\\n?\\s{' + leadingws + '}','g'),
        md        = text.replace(regex,'\n'),
        html      = (new Showdown.converter()).makeHtml(md);

    // here, have sum HTML
    elem.innerHTML = html;

  });

}());
