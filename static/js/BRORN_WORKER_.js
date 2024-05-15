
export let CALLERSTACK = []
export let _ = undefined
export var CONNECTION = {}
export var REQUESTS = {}
export var CONNECTION_COUNTER = 0
export var ERR_EXCEPTIONS = false
export var ON_GOING_REQUEST = []
export let _last_ls_random_result = ''
export const _JS_NAME = 'CACHE___brorn.JS' 
export const _JS_VERSION_ = 'v 0.13.1_alpha' 
export const _VERSION_ = _JS_VERSION_
export const POST = "POST"
export const GET = "GET"
export const OPTION = "OPTION"
export function $CLASS(class_name){return document.getElementsByClassName(class_name)}
export function $TAG(tag){return document.getElementsByTagName(tag)}
export function $randint(size){return Math.floor(Math.random() * size);}
export function $ID(id_name){return document.getElementById(id_name)}
export function goto(url){window.location.replace(url);}
export function redirectto(url){window.location.href = url;}
export function $$$_(q){return document.querySelector(q)}
export function $json(str){return JSON.parse(str)}
export function $table(...p){console.table(...p)}
export function $print(...p){console.log(...p)}
export function println(...p){console.log(...p)}
export function $date(){return new Date()}
export function $datetime(){return new Date().toLocaleString()}

export function $http(p){return http(p)}
export function $send(p){return http(p)} 
export function http(p){ 
	var UNIQUE_REQUEST_KEY = gen_code(14)
	p = p
	let RESULT_REQ = undefined
	CONNECTION_COUNTER += 1
	const params = populate(p)
	var ACTIVE_CONNECTION = (CONNECTION_COUNTER)
	REQUESTS[ACTIVE_CONNECTION] =  params
	CONNECTION[ACTIVE_CONNECTION] = new XMLHttpRequest()
	var xhttp = {}
	xhttp[UNIQUE_REQUEST_KEY] = CONNECTION[ACTIVE_CONNECTION]
	xhttp[UNIQUE_REQUEST_KEY]["UNIQUE_REQUEST_KEY"] = UNIQUE_REQUEST_KEY
	xhttp[UNIQUE_REQUEST_KEY].open(REQUESTS[ACTIVE_CONNECTION].method,REQUESTS[ACTIVE_CONNECTION].action,REQUESTS[ACTIVE_CONNECTION].a_sync)
	// xhttp[UNIQUE_REQUEST_KEY].timeout = 1;
	for (var key in REQUESTS[ACTIVE_CONNECTION].headers){xhttp[UNIQUE_REQUEST_KEY].setRequestHeader(key, REQUESTS[ACTIVE_CONNECTION].headers[key])}
	// xhttp[UNIQUE_REQUEST_KEY].onreadystatechange = function(){RESULT_REQ = this}
	let loadEnd =  function (e) {
		RESULT_REQ = e.target
		if(parseInt(e.target.status)!=200){REQUESTS[ACTIVE_CONNECTION].err(e)}
		if(RESULT_REQ.readyState == 4) {
			if(RESULT_REQ.status == 200){
				if(REQUESTS[ACTIVE_CONNECTION].response=="all"){REQUESTS[ACTIVE_CONNECTION].func(RESULT_REQ)}
				else if(REQUESTS[ACTIVE_CONNECTION].response=="header"){REQUESTS[ACTIVE_CONNECTION].func(RESULT_REQ.getAllResponseHeaders())}
				else if(REQUESTS[ACTIVE_CONNECTION].response=="text"){REQUESTS[ACTIVE_CONNECTION].func(RESULT_REQ.responseText)}
				else{REQUESTS[ACTIVE_CONNECTION].func(RESULT_REQ.responseText)}
			}
		}
		else if(RESULT_REQ.status == 500 || RESULT_REQ.status == 404	|| RESULT_REQ.status == 401){
			REQUESTS[ACTIVE_CONNECTION].func(RESULT_REQ.getAllResponseHeaders)
			ERROR = {"ERROR_REQUEST":CONNECTION[ACTIVE_CONNECTION]}
			return xhttp[UNIQUE_REQUEST_KEY]
			
		}
		else{REQUESTS[ACTIVE_CONNECTION].on_request(this)}
	}

	let progress_ = function(e){REQUESTS[ACTIVE_CONNECTION].progress(e)}
	let _timeout = function(e){REQUESTS[ACTIVE_CONNECTION].timeout(e)}
	// xhttp[UNIQUE_REQUEST_KEY].timeout = 2000
	xhttp[UNIQUE_REQUEST_KEY].addEventListener("loadend", loadEnd);
	xhttp[UNIQUE_REQUEST_KEY].addEventListener("progress", progress_);
	xhttp[UNIQUE_REQUEST_KEY].addEventListener("timeout", _timeout);
	xhttp[UNIQUE_REQUEST_KEY].send(params.data);
	return xhttp[UNIQUE_REQUEST_KEY]
}

export function populate(params){
	if(params.action==undefined){params.action='/'}
	if(params.data==undefined){params.data=$DATA({'_DATA':'NULL'})}
	if(params.func==undefined){params.func=function(res){$print(res)}}
	if(params.err==undefined){params.err=function(res){$print(res)}}
	if(params.progress==undefined){params.progress=function(res){}}
	if(params.timeout==undefined){params.timeout=function(res){}}
	if(params.on_request==undefined){params.on_request=function(ret){println(" *[BRORN.js] on request :"+JSON.stringify(ret.xhttp))}}
	if(params.method==undefined){params.method='POST'}
	if(params.a_sync==undefined){params.a_sync=true}
	if(params.response==undefined){params.type="responseText"}
	if(params.headers==undefined){params.headers={}}
	return params
}


export function gen_code(length) {
	for (var s=''; s.length < length; s += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'.charAt(Math.random()*62|0));
	return s;
}

export function headerMap(resp){
	const arr = resp.target.getAllResponseHeaders().trim().split(/[\r\n]+/);
	const _headerMap = {};
	arr.forEach((line) => {
		const parts = line.split(': ');
		const header = parts.shift();
		const value = parts.join(': ');
		_headerMap[header] = value;
	});
	return _headerMap
}

export function $DATA(d){var data_form = new FormData();for(var key in d){data_form.append(key, d[key])};return data_form}

FormData.prototype.appendFile = function(file_tag) {for (var i = 0; i < file_tag.files.length; i++) {this.append(file_tag.id+i,file_tag.files[i])};return this}
FormData.prototype.appendFileArr = function(file_tag) {for (var x = 0; x < file_tag.files.length; x++) {this.append(file_tag.id+"[]", file_tag.files[x]);}return this}

export function num_comma(x){return Money(x)}
export function money(x){return Money(x)}
export function Money(x) {
	if(x==null){return x}
	else{return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");}
}