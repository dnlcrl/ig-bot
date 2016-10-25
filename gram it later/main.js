
function _anchorDownloader(info, tab) {
  var timeout = 500;
  var filename = 'pinitlater'+ Math.random().toString(36).substr(2);
  var description = tab.title.substr(0, 500).replace(/[-[\]{}()*+?.,'"\\^$|#\s]/g, "\\\$&");
  
  var url = encodeURIComponent(tab.url);
  var src = encodeURIComponent(info.srcUrl);
  var res =  'javascript:\'<!doctype html><html>'+
    '<head></head>' +
    '<script type="text/javascript">' +
      'document.addEventListener("DOMContentLoaded", function() {var filename = "gramitlater"+ Math.random().toString(36).substr(2);'+
      'var description ="'+  description +'";'+
      'var url = "' + url + '";'+
      'var src = "' + src + '";' + 
      'var content = description +  String.fromCharCode(13) + url +  String.fromCharCode(13) + src +   String.fromCharCode(13) +"' + info.menuItemId + '";'+ 
      'var blob = new Blob([ content ], {type : "text/plain;charset=UTF-8"});'+
      'var a = document.createElement("a");'+
      'a.href = window.URL.createObjectURL(blob);'+
      'a.download = filename;' +
      'a.onload = "initDownload()";'+
      'document.body.appendChild(a);'+
      
      ''+
      'a.click();}, false);' +
      'setTimeout(function() { window.close(); }, ' + timeout + ');' +
      ''+
      //'a.click()'
    '</script>' +
    '<body >' +
    '</body>' +
    '</html>\'';
  console.log(res);
  return res;
};

function createFile(info, tab)
{
   chrome.tabs.create( { 'url' : _anchorDownloader( info, tab ), 'active' : false  } );
   return;
}


var tags = [
"supreme",
"supremenyc",
"streetwear",
"streetstyle",
"nike",
"adidas",
"swag",
"style",
"yeezy",
"jordan",
"model",
"stussy",
"moda",
"outfit",
"clothes",
"clothing",
"thenorthface",
"stoneisland",
"hype",
]
tags.sort();

for (var i = 0; i < tags.length; i++)
{
  var key = tags[i];
  chrome.contextMenus.create({
      title: key,
      id: key, 
      contexts: ["image"],
      onclick: createFile
  });
}


