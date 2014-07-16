var URL = window.location.href

average = function(a){
    var r = {mean: 0, variance: 0, deviation: 0}, t = a.length;
    for(var m, s = 0, l = t; l--; s += a[l]);
    for(m = r.mean = s / t, l = t, s = 0; l--; s += Math.pow(a[l] - m, 2));
    return r.deviation = Math.sqrt(r.variance = s / t), r;
}

function getURLparameters(){
    var index = URL.indexOf('?')
	var b=""
	if(index>-1){  
		b= URL.substring(URL.indexOf('?'))
	}
    return b;
}

var urlParams = getURLparameters();

//
// This method Gets URL Parameters (GUP)
//
function gupURL( name)
{
  var regexS = "[\\?&]"+name+"=([^&#]*)";
  var regex = new RegExp( regexS );
  var results = regex.exec( URL );
  if( results == null )
    return "";
  else
    return results[1];
}

//
// This method decodes the query parameters that were URL-encoded
//

/*
function decode(strToDecode)
{
  var encoded = strToDecode;
  return unescape(encoded.replace(/\+/g,  " "));
}
*/
    
function submitForm(){
    var f= document.createElement('form')
    f.id="mturk_form"
    f.method="POST"
	var sandbox = true;
	if(URL.indexOf("workersandbox.mturk.com")<0){
		sandbox = false;
	}		
	if (sandbox) {
		f.action = "http://workersandbox.mturk.com/mturk/externalSubmit";
	} else{
		f.action="http://www.mturk.com/mturk/externalSubmit"  
	}   
    
    var b= document.createElement('input')
    b.id="submitButton"
    b.type="hidden" 
    b.name="default" 
    b.value="1234"
    
    var h= document.createElement('input')
    h.id="assignmentId"
    h.type="hidden" 
    h.name="assignmentId" 
    h.value= gupURL('assignmentId', URL);
    
    f.appendChild(h)
    f.appendChild(b)
            
    document.body.appendChild(f)
    
    f.submit();
}