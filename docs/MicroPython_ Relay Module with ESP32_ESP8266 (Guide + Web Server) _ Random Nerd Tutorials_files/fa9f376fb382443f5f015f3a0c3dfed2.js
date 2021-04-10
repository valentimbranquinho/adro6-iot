(function(){/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var m=this||self;function n(a,b){function c(){}c.prototype=b.prototype;a.L=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.K=function(d,e,f){for(var h=Array(arguments.length-2),k=2;k<arguments.length;k++)h[k-2]=arguments[k];return b.prototype[e].apply(d,h)}};function p(a,b){return a.g?a.j.slice(0,a.g.index)+b+a.j.slice(a.g.index):a.j+b}function ba(a,b){return a.i&&a.h||a.l?1==b?a.i?a.h:p(a,"&dct=1"):2==b?p(a,"&ri=2"):p(a,"&ri=16"):a.j}var ca=class{constructor({url:a}){this.j=a;const b=/[?&]dsh=1(&|$)/.test(a);this.i=!b&&/[?&]ae=1(&|$)/.test(a);this.l=!b&&/[?&]ae=2(&|$)/.test(a);if((this.g=/[?&]adurl=([^&]*)/.exec(a))&&this.g[1]){let c;try{c=decodeURIComponent(this.g[1])}catch(d){c=null}this.h=c}}};function da(a,b){a:{for(var c=a.length,d="string"===typeof a?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a)){b=e;break a}b=-1}return 0>b?null:"string"===typeof a?a.charAt(b):a[b]};var q=class{constructor(a,b){this.g=b===ea?a:""}};q.prototype.i=!0;q.prototype.h=function(){return this.g.toString()};q.prototype.toString=function(){return this.g.toString()};var fa=/^(?:(?:https?|mailto|ftp):|[^:/?#]*(?:[/?#]|$))/i,ea={};var t;a:{var ha=m.navigator;if(ha){var ia=ha.userAgent;if(ia){t=ia;break a}}t=""};function ka(a){let b=!1,c;return function(){b||(c=a(),b=!0);return c}};function v(a,b){b instanceof q||b instanceof q||(b="object"==typeof b&&b.i?b.h():String(b),fa.test(b)||(b="about:invalid#zClosurez"),b=new q(b,ea));a.href=b instanceof q&&b.constructor===q?b.g:"type_error:SafeUrl"};function la(){return Math.floor(2147483648*Math.random()).toString(36)+Math.abs(Math.floor(2147483648*Math.random())^Date.now()).toString(36)};function ma(){return-1!=t.indexOf("iPhone")&&-1==t.indexOf("iPod")&&-1==t.indexOf("iPad")};function na(a){na[" "](a);return a}na[" "]=function(){};var oa=ma(),pa=-1!=t.indexOf("iPad");var qa;(qa=ma())||(qa=-1!=t.indexOf("iPod"));var ra=qa,sa=-1!=t.indexOf("iPad");var ta={},ua=null;function va(a){if(a.i){if(a.j){var b=a.g;for(d in b)if(Object.prototype.hasOwnProperty.call(b,d)){var c=b[d].g;c&&c.o()}}}else{a.h.length=0;var d=w(a);d.sort();for(b=0;b<d.length;b++){let e=a.g[d[b]];(c=e.g)&&c.o();a.h.push([e.key,e.value])}a.i=!0}return a.h}function w(a){a=a.g;var b=[],c;for(c in a)Object.prototype.hasOwnProperty.call(a,c)&&b.push(c);return b}function wa(a,b){return a.j?(b.g||(b.g=new a.j(b.value),a.isFrozen()&&null(b.g)),b.g):b.value}
function xa(a,b){var c=w(a);c.sort();for(var d=0;d<c.length;d++){let e=a.g[c[d]];b.call(void 0,wa(a,e),e.key,a)}}
class ya{constructor(a,b){this.h=a;this.j=b;this.g={};this.i=!0;if(0<this.h.length){for(a=0;a<this.h.length;a++){b=this.h[a];var c=b[0];this.g[c.toString()]=new za(c,b[1])}this.i=!0}}isFrozen(){return!1}o(){return va(this)}G(){return va(this)}entries(){var a=[],b=w(this);b.sort();for(var c=0;c<b.length;c++){let d=this.g[b[c]];a.push([d.key,wa(this,d)])}return new Aa(a)}keys(){var a=[],b=w(this);b.sort();for(var c=0;c<b.length;c++)a.push(this.g[b[c]].key);return new Aa(a)}values(){var a=[],b=w(this);
b.sort();for(var c=0;c<b.length;c++)a.push(wa(this,this.g[b[c]]));return new Aa(a)}set(a,b){var c=new za(a);this.j?(c.g=b,c.value=b.G()):c.value=b;this.g[a.toString()]=c;this.i=!1;return this}get(a){if(a=this.g[a.toString()])return wa(this,a)}has(a){return a.toString()in this.g}}class za{constructor(a,b){this.key=a;this.value=b;this.g=void 0}}class Aa{constructor(a){this.h=0;this.g=a}next(){return this.h<this.g.length?{done:!1,value:this.g[this.h++]}:{done:!0,value:void 0}}}
"undefined"!=typeof Symbol&&"undefined"!=typeof Symbol.iterator&&(Aa.prototype[Symbol.iterator]=function(){return this});function x(){}var Ba="function"==typeof Uint8Array;function y(a,b,c){a.g=null;b||(b=[]);a.A=void 0;a.j=-1;a.h=b;a:{if(b=a.h.length){--b;var d=a.h[b];if(!(null===d||"object"!=typeof d||Array.isArray(d)||Ba&&d instanceof Uint8Array)){a.l=b-a.j;a.i=d;break a}}a.l=Number.MAX_VALUE}a.v={};if(c)for(b=0;b<c.length;b++)d=c[b],d<a.l?(d+=a.j,a.h[d]=a.h[d]||z):(Ca(a),a.i[d]=a.i[d]||z)}var z=[];function Ca(a){var b=a.l+a.j;a.h[b]||(a.i=a.h[b]={})}
function A(a,b){if(b<a.l){b+=a.j;var c=a.h[b];return c!==z?c:a.h[b]=[]}if(a.i)return c=a.i[b],c===z?a.i[b]=[]:c}function E(a,b,c){a=A(a,b);return null==a?c:a}function F(a,b){return E(a,b,"")}function G(a,b){a=A(a,b);a=null==a?a:!!a;return null==a?!1:a}function H(a,b,c){a.g||(a.g={});if(b in a.g)return a.g[b];var d=A(a,b);d||(d=[],I(a,b,d));c=new ya(d,c);return a.g[b]=c}function I(a,b,c){b<a.l?a.h[b+a.j]=c:(Ca(a),a.i[b]=c);return a}
function K(a,b,c){a.g||(a.g={});if(!a.g[c]){var d=A(a,c);d&&(a.g[c]=new b(d))}return a.g[c]}function Da(a){var b=Ea;a.g||(a.g={});if(!a.g[7]){let e=A(a,7);for(var c=[],d=0;d<e.length;d++)c[d]=new b(e[d]);a.g[7]=c}b=a.g[7];b==z&&(b=a.g[7]=[]);return b}function Fa(a){if(a.g)for(var b in a.g){var c=a.g[b];if(Array.isArray(c))for(var d=0;d<c.length;d++)c[d]&&c[d].o();else c&&c.o()}}x.prototype.o=function(){Fa(this);return this.h};x.prototype.G=function(){Fa(this);return this.h};
x.prototype.s=Ba?function(){var a=Uint8Array.prototype.toJSON;Uint8Array.prototype.toJSON=function(){var b;void 0===b&&(b=0);if(!ua){ua={};for(var c="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".split(""),d=["+/=","+/","-_=","-_.","-_"],e=0;5>e;e++){var f=c.concat(d[e].split(""));ta[e]=f;for(var h=0;h<f.length;h++){var k=f[h];void 0===ua[k]&&(ua[k]=h)}}}b=ta[b];c=[];for(d=0;d<this.length;d+=3){var g=this[d],l=(e=d+1<this.length)?this[d+1]:0;k=(f=d+2<this.length)?this[d+2]:0;h=g>>
2;g=(g&3)<<4|l>>4;l=(l&15)<<2|k>>6;k&=63;f||(k=64,e||(l=64));c.push(b[h],b[g],b[l]||"",b[k]||"")}return c.join("")};try{return JSON.stringify(this.h&&this.o(),Ga)}finally{Uint8Array.prototype.toJSON=a}}:function(){return JSON.stringify(this.h&&this.o(),Ga)};function Ga(a,b){return"number"!==typeof b||!isNaN(b)&&Infinity!==b&&-Infinity!==b?b:String(b)}x.prototype.toString=function(){return this.o().toString()};
function Ha(a){if(Array.isArray(a)){for(var b=Array(a.length),c=0;c<a.length;c++){var d=a[c];null!=d&&(b[c]="object"==typeof d?Ha(d):d)}return b}if(Ba&&a instanceof Uint8Array)return new Uint8Array(a);b={};for(c in a)d=a[c],null!=d&&(b[c]="object"==typeof d?Ha(d):d);return b};function Ia(a){y(this,a,null)}n(Ia,x);function Ja(a){y(this,a,Na)}n(Ja,x);function Ea(a){y(this,a,null)}n(Ea,x);function L(a){y(this,a,null)}n(L,x);function Oa(a){y(this,a,null)}n(Oa,x);var Na=[6,7];Ea.prototype.u=function(){return F(this,3)};Ea.prototype.F=function(a){I(this,5,a)};L.prototype.u=function(){return F(this,1)};L.prototype.F=function(a){I(this,2,a)};function Pa(a){y(this,a,Qa)}n(Pa,x);var Qa=[17];class Ra{constructor(a,b){this.error=a;this.context=b.context;this.msg=b.message||"";this.id=b.id||"jserror";this.meta={}}};var Sa={capture:!0},Ta={passive:!0},Ua=ka(function(){let a=!1;try{const b=Object.defineProperty({},"passive",{get:function(){a=!0}});m.addEventListener("test",null,b)}catch(b){}return a});function Va(a){return a?a.passive&&Ua()?a:a.capture||!1:!1}function N(a,b,c,d){a.addEventListener&&a.addEventListener(b,c,Va(d))}function Wa(a,b,c){a.removeEventListener&&a.removeEventListener(b,c,Va(void 0))};var Xa=/^(?:([^:/?#.]+):)?(?:\/\/(?:([^\\/?#]*)@)?([^\\/?#]*?)(?::([0-9]+))?(?=[\\/?#]|$))?([^?#]+)?(?:\?([^#]*))?(?:#([\s\S]*))?$/;function Ya(a){var b=a.indexOf("#");0>b&&(b=a.length);var c=a.indexOf("?");if(0>c||c>b){c=b;var d=""}else d=a.substring(c+1,b);return[a.substr(0,c),d,a.substr(b)]}function Za(a,b){return b?a?a+"&"+b:b:a}function $a(a,b){if(!b)return a;a=Ya(a);a[1]=Za(a[1],b);return a[0]+(a[1]?"?"+a[1]:"")+a[2]}
function ab(a,b,c){if(Array.isArray(b))for(var d=0;d<b.length;d++)ab(a,String(b[d]),c);else null!=b&&c.push(a+(""===b?"":"="+encodeURIComponent(String(b))))}function bb(a){var b=[],c;for(c in a)ab(c,a[c],b);return b.join("&")}function cb(){var a=la();a=null!=a?"="+encodeURIComponent(String(a)):"";return $a("https://pagead2.googlesyndication.com/pagead/gen_204","zx"+a)}
function db(a,b){a=Ya(a);var c=a[1],d=[];c&&c.split("&").forEach(function(e){var f=e.indexOf("=");b.hasOwnProperty(0<=f?e.substr(0,f):e)||d.push(e)});a[1]=Za(d.join("&"),bb(b));return a[0]+(a[1]?"?"+a[1]:"")+a[2]};function eb(a){try{var b;if(b=!!a&&null!=a.location.href)a:{try{na(a.foo);b=!0;break a}catch(c){}b=!1}return b}catch(c){return!1}}function fb(a,b){if(a)for(const c in a)Object.prototype.hasOwnProperty.call(a,c)&&b.call(void 0,a[c],c,a)}let gb=[];const ib=()=>{const a=gb;gb=[];for(const b of a)try{b()}catch(c){}};
var jb=a=>{var b=O;"complete"===b.readyState||"interactive"===b.readyState?(gb.push(a),1==gb.length&&(window.Promise?Promise.resolve().then(ib):window.setImmediate?setImmediate(ib):setTimeout(ib,0))):b.addEventListener("DOMContentLoaded",a)};function P(a,b,c=null){kb(a,b,c)}function kb(a,b,c){a.google_image_requests||(a.google_image_requests=[]);const d=a.document.createElement("img");if(c){const e=f=>{c&&c(f);Wa(d,"load",e);Wa(d,"error",e)};N(d,"load",e);N(d,"error",e)}d.src=b;a.google_image_requests.push(d)};let lb=0;function nb(a){return(a=ob(a,document.currentScript))&&a.getAttribute("data-jc-version")||"unknown"}function ob(a,b=null){return b&&b.getAttribute("data-jc")===String(a)?b:document.querySelector(`[${"data-jc"}="${a}"]`)}
function pb(a){if(!(.01<Math.random())){a=`https://${"pagead2.googlesyndication.com"}/pagead/gen_204?id=jca&jc=${a}&version=${nb(a)}&sample=${.01}`;var b=window,c;if(c=b.navigator)c=b.navigator.userAgent,c=/Chrome/.test(c)&&!/Edge/.test(c)?!0:!1;c&&b.navigator.sendBeacon?b.navigator.sendBeacon(a):P(b,a)}};var O=document,Q=window;function qb(a,b){const c={};c[a]=b;return[c]}function rb(a,b,c,d,e){const f=[];fb(a,function(h,k){(h=sb(h,b,c,d,e))&&f.push(k+"="+h)});return f.join(b)}
function sb(a,b,c,d,e){if(null==a)return"";b=b||"&";c=c||",$";"string"==typeof c&&(c=c.split(""));if(a instanceof Array){if(d=d||0,d<c.length){const f=[];for(let h=0;h<a.length;h++)f.push(sb(a[h],b,c,d+1,e));return f.join(c[d])}}else if("object"==typeof a)return e=e||0,2>e?encodeURIComponent(rb(a,b,c,d,e+1)):"...";return encodeURIComponent(String(a))}function tb(a){let b=1;for(const c in a.h)b=c.length>b?c.length:b;return 3997-b-a.i.length-1}
function ub(a,b,c){b=b+"//pagead2.googlesyndication.com"+c;let d=tb(a)-c.length;if(0>d)return"";a.g.sort(function(f,h){return f-h});c=null;let e="";for(let f=0;f<a.g.length;f++){const h=a.g[f],k=a.h[h];for(let g=0;g<k.length;g++){if(!d){c=null==c?h:c;break}let l=rb(k[g],a.i,",$");if(l){l=e+l;if(d>=l.length){d-=l.length;b+=l;e=a.i;break}c=null==c?h:c}}}a="";null!=c&&(a=e+"trn="+c);return b+a}class vb{constructor(){this.i="&";this.h={};this.j=0;this.g=[]}};function wb(a,b,c,d,e,f){if((d?a.g:Math.random())<(e||.01))try{let h;c instanceof vb?h=c:(h=new vb,fb(c,(g,l)=>{var u=h,r=u.j++;g=qb(l,g);u.g.push(r);u.h[r]=g}));const k=ub(h,a.h,"/pagead/gen_204?id="+b+"&");k&&("undefined"!==typeof f?P(m,k,f):P(m,k))}catch(h){}}class xb{constructor(){this.h="http:"===Q.location.protocol?"http:":"https:";this.g=Math.random()}};var yb={};function zb(){if(yb!==yb)throw Error("Bad secret");};function Ab(){var a="undefined"!==typeof window?window.trustedTypes:void 0;return null!==a&&void 0!==a?a:null};var Bb,Cb=class{};class Db extends Cb{constructor(){var a=null!==Eb&&void 0!==Eb?Eb:"";super();zb();this.g=a}toString(){return this.g.toString()}}var Eb=null===(Bb=Ab())||void 0===Bb?void 0:Bb.emptyHTML;new Db;var Fb,Kb=class{};class Lb extends Kb{constructor(){var a=null!==Mb&&void 0!==Mb?Mb:"";super();zb();this.g=a}toString(){return this.g.toString()}}var Mb=null===(Fb=Ab())||void 0===Fb?void 0:Fb.emptyScript;new Lb;var Nb=class{};class Ob extends Nb{constructor(a){super();zb();this.g=a}toString(){return this.g}}new Ob("about:blank");var Pb=new Ob("about:invalid#zTSz");const Qb="DATA HTTP HTTPS MAILTO FTP RELATIVE".split(" ");function Rb(a,b=Qb){var c;var d=a.substring(0,14).indexOf(":");d=null!==(c=Sb[0>d?"":a.substr(0,d).toLowerCase()])&&void 0!==c?c:Tb;if(b.includes(d.scheme)&&d.m(a))return new Ob(a)}function Ub(a,b=Qb){return Rb(a,b)||Pb}
const Tb={scheme:"RELATIVE",m:a=>/^[^:/?#]*(?:[/?#]|$)/i.test(a)},Sb={tel:{scheme:"TEL",m:R("tel:")},callto:{scheme:"CALLTO",m:a=>/^callto:\+?\d*$/i.test(a)},ssh:{scheme:"SSH",m:R("ssh://")},rtsp:{scheme:"RTSP",m:R("rtsp://")},data:{scheme:"DATA",m:a=>{{const b=a.match(/^data:(.*);base64,[a-z0-9+\/]+=*$/i);if(a=2===(null===b||void 0===b?void 0:b.length))a=b[1].match(/^([^;]+)(?:;\w+=(?:\w+|"[\w;,= ]+"))*$/i),a=2===(null===a||void 0===a?void 0:a.length)&&(/^image\/(?:bmp|gif|jpeg|jpg|png|tiff|webp|x-icon)$/i.test(a[1])||
/^video\/(?:mpeg|mp4|ogg|webm|x-matroska|quicktime|x-ms-wmv)$/i.test(a[1])||/^audio\/(?:3gpp2|3gpp|aac|L16|midi|mp3|mp4|mpeg|oga|ogg|opus|x-m4a|x-matroska|x-wav|wav|webm)$/i.test(a[1]))}return a}},http:{scheme:"HTTP",m:R("http:")},https:{scheme:"HTTPS",m:R("https:")},ftp:{scheme:"FTP",m:R("ftp:")},mailto:{scheme:"MAILTO",m:R("mailto:")},intent:{scheme:"INTENT",m:R("intent:")},market:{scheme:"MARKET",m:R("market:")},itms:{scheme:"ITMS",m:R("itms:")},"itms-appss":{scheme:"ITMS_APPSS",m:R("itms-appss:")},
"itms-services":{scheme:"ITMS_SERVICES",m:R("itms-services:")}};function R(a){return b=>b.substr(0,a.length).toLowerCase()===a};const Vb="HTTP HTTPS MAILTO FTP RELATIVE MARKET ITMS INTENT ITMS_APPSS".split(" ");function S(a,b){if(a instanceof q)return a;const c=Ub(a,Vb);c===Pb&&b(a);if(c instanceof Ob)a=c.g;else throw Error("wrong type");return new q(a,ea)}var T=a=>{var b=`${"http:"===Q.location.protocol?"http:":"https:"}//${"pagead2.googlesyndication.com"}/pagead/gen_204`;return c=>{c=bb({id:"unsafeurl",ctx:a,url:c});c=$a(b,c);navigator.sendBeacon&&navigator.sendBeacon(c,"")}};var Wb=!!window.google_async_iframe_id;let U=Wb&&window.parent||window;var Xb=a=>{var b=O;try{return b.querySelectorAll("*["+a+"]")}catch(c){return[]}};const Yb=/^https?:\/\/(\w|-)+\.cdn\.ampproject\.(net|org)(\?|\/|$)/;var Zb=class{constructor(a,b){this.g=a;this.h=b}},$b=class{constructor(a,b){this.url=a;this.D=!!b;this.depth=null}};let ac=null;var bc=()=>{const a=m.performance;return a&&a.now&&a.timing?Math.floor(a.now()+a.timing.navigationStart):Date.now()},cc=()=>{const a=m.performance;return a&&a.now?a.now():null};class dc{constructor(a,b){var c=cc()||bc();this.label=a;this.type=b;this.value=c;this.duration=0;this.uniqueId=Math.random();this.slotId=void 0}};const V=m.performance,ec=!!(V&&V.mark&&V.measure&&V.clearMarks),W=ka(()=>{var a;if(a=ec){var b;if(null===ac){ac="";try{a="";try{a=m.top.location.hash}catch(c){a=m.location.hash}a&&(ac=(b=a.match(/\bdeid=([\d,]+)/))?b[1]:"")}catch(c){}}b=ac;a=!!b.indexOf&&0<=b.indexOf("1337")}return a});function fc(a){a&&V&&W()&&(V.clearMarks(`goog_${a.label}_${a.uniqueId}_start`),V.clearMarks(`goog_${a.label}_${a.uniqueId}_end`))}
class gc{constructor(){var a=X;this.h=[];this.i=a||m;let b=null;a&&(a.google_js_reporting_queue=a.google_js_reporting_queue||[],this.h=a.google_js_reporting_queue,b=a.google_measure_js_timing);this.g=W()||(null!=b?b:1>Math.random())}start(a,b){if(!this.g)return null;a=new dc(a,b);b=`goog_${a.label}_${a.uniqueId}_start`;V&&W()&&V.mark(b);return a}};function hc(a){let b=a.toString();a.name&&-1==b.indexOf(a.name)&&(b+=": "+a.name);a.message&&-1==b.indexOf(a.message)&&(b+=": "+a.message);if(a.stack){a=a.stack;try{-1==a.indexOf(b)&&(a=b+"\n"+a);let c;for(;a!=c;)c=a,a=a.replace(/((https?:\/..*\/)[^\/:]*:\d+(?:.|\n)*)\2/,"$1");b=a.replace(/\n */g,"\n")}catch(c){}}return b}
function ic(a,b,c){let d,e;try{if(a.g&&a.g.g){e=a.g.start(b.toString(),3);d=c();var f=a.g;c=e;if(f.g&&"number"===typeof c.value){c.duration=(cc()||bc())-c.value;var h=`goog_${c.label}_${c.uniqueId}_end`;V&&W()&&V.mark(h);!f.g||2048<f.h.length||f.h.push(c)}}else d=c()}catch(k){f=!0;try{fc(e),f=a.s(b,new Ra(k,{message:hc(k)}),void 0,void 0)}catch(g){a.l(217,g)}if(f){let g,l;null==(g=window.console)||null==(l=g.error)||l.call(g,k)}else throw k;}return d}
function jc(a,b){var c=kc;return(...d)=>ic(c,a,()=>b.apply(void 0,d))}
class lc{constructor(){var a=mc;this.i=Y;this.h=null;this.s=this.l;this.g=void 0===a?null:a;this.j=!1}pinger(){return this.i}l(a,b,c,d,e){e=e||"jserror";let f;try{const B=new vb;var h=B;h.g.push(1);h.h[1]=qb("context",a);b.error&&b.meta&&b.id||(b=new Ra(b,{message:hc(b)}));if(b.msg){h=B;var k=b.msg.substring(0,512);h.g.push(2);h.h[2]=qb("msg",k)}var g=b.meta||{};b=g;if(this.h)try{this.h(b)}catch(M){}if(d)try{d(b)}catch(M){}d=B;g=[g];d.g.push(3);d.h[3]=g;{d=m;g=[];b=null;do{var l=d;if(eb(l)){var u=
l.location.href;b=l.document&&l.document.referrer||null}else u=b,b=null;g.push(new $b(u||""));try{d=l.parent}catch(Z){d=null}}while(d&&l!=d);for(let Z=0,Gb=g.length-1;Z<=Gb;++Z)g[Z].depth=Gb-Z;l=m;if(l.location&&l.location.ancestorOrigins&&l.location.ancestorOrigins.length==g.length-1)for(u=1;u<g.length;++u){var r=g[u];r.url||(r.url=l.location.ancestorOrigins[u-1]||"",r.D=!0)}var C=g;let M=new $b(m.location.href,!1);l=null;const Ka=C.length-1;for(r=Ka;0<=r;--r){var D=C[r];!l&&Yb.test(D.url)&&(l=D);
if(D.url&&!D.D){M=D;break}}D=null;const Ac=C.length&&C[Ka].url;0!=M.depth&&Ac&&(D=C[Ka]);f=new Zb(M,D)}if(f.h){C=B;var J=f.h.url||"";C.g.push(4);C.h[4]=qb("top",J)}var La={url:f.g.url||""};if(f.g.url){var Ma=f.g.url.match(Xa),aa=Ma[1],Hb=Ma[3],Ib=Ma[4];J="";aa&&(J+=aa+":");Hb&&(J+="//",J+=Hb,Ib&&(J+=":"+Ib));var Jb=J}else Jb="";aa=B;La=[La,{url:Jb}];aa.g.push(5);aa.h[5]=La;wb(this.i,e,B,this.j,c)}catch(B){try{wb(this.i,e,{context:"ecmserr",rctx:a,msg:hc(B),url:f&&f.g.url},this.j,c)}catch(M){}}return!0}}
;let Y,kc;if(Wb&&!eb(U)){let a="."+O.domain;try{for(;2<a.split(".").length&&!eb(U);)O.domain=a=a.substr(a.indexOf(".")+1),U=window.parent}catch(b){}eb(U)||(U=window)}const X=U,mc=new gc;var nc=()=>{if(!X.google_measure_js_timing){var a=mc;a.g=!1;a.h!=a.i.google_js_reporting_queue&&(W()&&Array.prototype.forEach.call(a.h,fc,void 0),a.h.length=0)}};Y=new xb;"number"!==typeof X.google_srt&&(X.google_srt=Math.random());var oc=Y,pc=X.google_srt;0<=pc&&1>=pc&&(oc.g=pc);kc=new lc;
kc.h=a=>{{const b=lb;0!==b&&(a.jc=String(b),a.shv=nb(b))}};kc.j=!0;"complete"==X.document.readyState?nc():mc.g&&N(X,"load",()=>{nc()});var qc=(a,b)=>jc(a,b);var rc=(a,b)=>{b=F(a,2)||b;if(!b)return"";if(G(a,13))return b;const c=/[?&]adurl=([^&]+)/.exec(b);if(!c)return b;const d=[b.slice(0,c.index+1)];xa(H(a,4,null),(e,f)=>{d.push(encodeURIComponent(f)+"="+encodeURIComponent(e)+"&")});d.push(b.slice(c.index+1));return d.join("")},sc=(a,b=[])=>{b=0<b.length?b:Xb("data-asoch-targets");a=H(a,1,Ja);const c=[];for(let k=0;k<b.length;++k){var d=b[k].getAttribute("data-asoch-targets"),e=d.split(","),f=!0;for(let g of e)if(!a.has(g)){f=!1;break}if(f){f=a.get(e[0]);
for(d=1;d<e.length;++d){{var h=a.get(e[d]);f=(new f.constructor(Ha(f.o()))).o();h=h.o();const g=Math.max(f.length,h.length);for(let l=0;l<g;++l)null==f[l]&&(f[l]=h[l]);f=new Ja(f)}}e=H(f,4,null);null!=A(f,5)&&e.set("nb",E(f,5,0).toString());c.push({element:b[k],data:f})}else wb(Y,"gdn-asoch",{type:1,data:d},!0,void 0,void 0)}return c},tc=a=>{for(const b of a)if(a=b.data,"A"==b.element.tagName&&!G(a,1)){const c=b.element,d=rc(a,c.href);0<d.length&&(v(c,S(d,T(609))),c.target||(c.target=null!=A(a,11)?
F(a,11):"_top"))}},uc=a=>{const b=window.oneAfmaInstance;if(b)for(const c of a)if((a=c.data)&&null!=A(a,8)&&(a=F(K(a,Oa,8),4))){b.fetchAppStoreOverlay(a);break}},vc=a=>{const b=[],c=[];for(var d of a)(a=d.data)&&null!=A(a,12)&&(c.push(K(a,L,12)),b.push(K(a,L,12).u()));d=(e,f)=>{if(f)for(const h of c)h.F(f[h.u()]||!1)};a=window.oneAfmaInstance;for(const e of b)a.canOpenAndroidApp(e,d)},yc=(a,b,c,d)=>{if(a||!b||null==A(b,12))return!1;const e=K(b,L,12).u();if(G(K(b,L,12),2)){a="";if(0<Da(b).length)for(const f of Da(b))a+=
F(f,2)+" "+f.u()+" ";wc({id:"gmob-apps",event:"och-open-android-app-before-click",deepLinks:a,appId:e,isDeepLinkPath:!1});d.click(c);d.openAndroidApp(e);setTimeout(()=>{var f={id:"gmob-apps",event:"och-open-android-app",appId:e,isDeepLinkPath:!1};xc(db(cb(),f))},1E3);return!0}wc({id:"gmob-apps",event:"och-open-android-app-validated-false",appId:e,isDeepLinkPath:!1});return!1},zc=(a,b,c,d,e)=>{if(!c||null==A(c,8))return!1;const f=K(c,Oa,8);let h=F(f,2);xa(H(c,10,null),(k,g)=>{{var l=h;g=encodeURIComponent(g);
const u=encodeURIComponent(k);k=new RegExp("[?&]"+g+"=([^&]+)");const r=k.exec(l);console.log(r);g=g+"="+u;h=r?l.replace(k,r[0].charAt(0)+g):l.replace("?","?"+g+"&")}});wc({id:"gmob-apps",event:"och-try-u2-redirect",appId:F(f,4)||"",isIos:a,isDeepLinkPath:!1});return e.redirectForStoreU2({clickUrl:d,trackingUrl:F(f,3),finalUrl:h,pingFunc:e.click,openFunc:b?e.openStoreOverlay:e.openIntentOrNativeApp})},Bc=(a,b=null)=>{if(null!==b){const c=new ca({url:a});if(c.i&&c.h||c.l)return b(p(c,"&act=1&ri=1")),
ba(c,1)}else return b=new ca({url:a}),a=b.i&&b.h||b.l?navigator.sendBeacon?navigator.sendBeacon(p(b,"&act=1&ri=1"),"")?ba(b,1):ba(b,2):ba(b,0):a;return a},wc=a=>{xc(db(cb(),a))},xc=a=>{Q.fetch?Q.fetch(a,{method:"GET",keepalive:!0,mode:"no-cors"}).then(b=>{b.ok||P(Q,a)}):P(Q,a)};function Cc(a){y(this,a,Dc)}n(Cc,x);var Dc=[6];const Ec=["platform","platformVersion","architecture","model","uaFullVersion"];var Fc=()=>{var a=window;return a.navigator&&a.navigator.userAgentData&&"function"===typeof a.navigator.userAgentData.getHighEntropyValues?a.navigator.userAgentData.getHighEntropyValues(Ec).then(b=>{var c=new Cc;c=I(c,1,b.platform);c=I(c,2,b.platformVersion);c=I(c,3,b.architecture);c=I(c,4,b.model);return I(c,5,b.uaFullVersion)}):null};function Gc(a){for(const b of a)if("A"==b.element.tagName){a=b.element;const c=b.data;null!=A(c,2)||I(c,2,a.href)}}function Hc(a,b){return da(a,c=>c.element===b)}function Ic(a){jb(qc(556,()=>{new Jc(a||{})}))}
function Kc(a,b,c,d){if(!G(d,13)){var e=c.href;var f=/[?&]adurl=([^&]+)/.exec(e);e=f?[e.slice(0,f.index),e.slice(f.index)]:[e,""];for(v(c,S(e[0],T(557)));!c.id;)if(f="asoch-id-"+la(),!O.getElementById(f)){c.id=f;break}f=c.id;"function"===typeof window.xy&&window.xy(b,c,O.body);"function"===typeof window.mb&&window.mb(c);"function"===typeof window.bgz&&window.bgz(f);"function"===typeof window.ja&&window.ja(f,d?E(d,5,0):0);a.j&&"function"===typeof window.ss&&(a.B?window.ss(f,1,a.j):window.ss(a.j,1));
0<e.length&&(a=0<a.A.length?c.href+"&uach="+encodeURIComponent(a.A)+e[1]:c.href+e[1],v(c,S(a,T(557))))}}async function Lc(a,b,c,d){let e="";window.oneAfmaInstance&&(e=await window.oneAfmaInstance.appendClickSignalsAsync(c.href)||"");Mc(a,b,c,d,e)}
function Mc(a,b,c,d,e){const f=G(a.g,2),h=f&&Date.now()-a.I>a.J;if(window.oneAfmaInstance){b.preventDefault?b.preventDefault():b.returnValue=!1;var k=window.oneAfmaInstance;b=a.i&&G(a.i,14)||!1;c=G(a.g,13)||a.i&&G(a.i,13);a.i&&G(a.i,18);var g=k.logScionEventAndAddParam(e);if(!yc(a.l,d,g,k)&&!zc(a.l,a.C,d,g,k)){{e=c;c=a.l;b=b&&G(d,15);const l=!/[?&]dsh=1(&|$)/.test(g)&&/[?&]ae=1(&|$)/.test(g);f&&h&&!b&&l&&(g=Bc(g,k.click));g&&g.startsWith("intent:")?(k.openIntentOrNativeApp(g),d={id:"gmob-apps",event:"och-open-intent-or-native-app",
appId:null!=A(d,8)&&F(K(d,Oa,8),4)||"",isIos:c,isDeepLinkPath:!1},xc(db(cb(),d))):e?k.openChromeCustomTab(g):k.openSystemBrowser(g,{useFirstPackage:!0,useRunningProcess:!0})}}}else h&&(d=Bc(c.href),d!==c.href&&v(c,S(d,T(599))));h&&(a.I=Date.now());pb(a.H)}
var Jc=class{constructor(a){this.l=ra||oa||sa||pa;var b=Xb("data-asoch-meta");1!==b.length?wb(Y,"gdn-asoch",{type:2,data:b.length},!0,void 0,void 0):(this.H=70,this.g=new Pa(JSON.parse(b[0].getAttribute("data-asoch-meta"))||[]),this.i=a["extra-meta"]?new Pa(JSON.parse(a["extra-meta"])):null,this.C=this.l&&"true"===a["ios-store-overlay"],this.A="",b=Fc(),null!=b&&b.then(c=>{this.A=c.s()}),this.h=sc(this.g),this.J=Number(a["async-click-timeout"])||300,this.I=-Infinity,this.j=F(this.g,5)||"",this.B=
G(this.g,11),this.i&&(this.B=G(this.i,11)),this.v=this.s=null,G(this.g,3)||(tc(this.h),I(this.g,3,!0)),Gc(this.h),!this.l&&window.oneAfmaInstance&&vc(this.h),window.oneAfmaInstance&&this.C&&"true"===a["prefetch-ios-store-overlay"]&&uc(this.h),N(O,"click",qc(557,c=>{a:if(!c.defaultPrevented||this.s===c){for(var d,e,f=c.target;(!d||!e)&&f;){e||"A"!=f.tagName||(e=f);var h=f.hasAttribute("data-asoch-targets");!d&&("A"==f.tagName||h)&&(h=h&&"true"===f.getAttribute("data-asoch-is-dynamic")?sc(this.g,[f]):
this.h,h=Hc(h,f))&&(d=h.data);f=f.parentElement}if(f=d&&!G(d,1)){if(c.defaultPrevented){var k=e;if(this.s===c&&this.v){var g=new Ia(this.v);e=F(d,9);f="";switch(E(g,4,1)){case 2:if(E(g,2,0))f="blocked_fast_click";else if(F(g,1)||F(g,7))f="blocked_border_click";break;case 3:g=O,g=g.getElementById?g.getElementById("common_15click_anchor"):null,"function"===typeof window.copfcChm&&g&&(d=new d.constructor(Ha(d.o())),I(d,5,12),H(d,4,null).set("nb",(12).toString()),(f=Hc(this.h,g))?f.data=d:this.h.push({element:g,
data:d}),k&&(Kc(this,c,k,d),I(d,2,k.href)),window.copfcChm(c,rc(d,g.href))),f="onepointfiveclick_first_click"}e&&f&&xc(e+"&label="+f);pb(this.H)}break a}h=d;for(g of A(h,6))xc(g)}if(e&&f){d=f?d:null;(g=Hc(this.h,e))?g=g.data:(g=new Ja,I(g,2,e.href),I(g,11,e.target||"_top"),this.h.push({element:e,data:g}));g=rc(d||g,F(g,2));0<g.length&&(v(e,S(g,T(557))),e.target||(e.target=d&&null!=A(d,11)?F(d,11):"_top"));Kc(this,c,e,d);for(k of A(this.g,17)){{let l;g=k;f=O.body;h={};"function"===typeof window.CustomEvent?
l=new CustomEvent(g,h):(l=document.createEvent("CustomEvent"),l.initCustomEvent(g,!!h.bubbles,!!h.cancelable,h.detail));f.dispatchEvent(l)}}G(this.g,16)?Lc(this,c,e,d):(k="",window.oneAfmaInstance&&(k=window.oneAfmaInstance.appendClickSignals(e.href)),Mc(this,c,e,d,k))}}}),Sa),this.j&&"function"===typeof window.ss&&N(O.body,"mouseover",qc(626,()=>{window.ss(this.j,0)}),Ta),a=window,a.googqscp&&"function"===typeof a.googqscp.registerCallback&&a.googqscp.registerCallback((c,d)=>{this.s=c;this.v=d}))}};{var Nc=qc(555,b=>Ic(b));lb=70;const a=ob(70,document.currentScript);if(null==a)throw Error("JSC not found 70");var Oc;{const b={},c=a.attributes;for(let d=c.length-1;0<=d;d--){const e=c[d].name;0===e.indexOf("data-jcp-")&&(b[e.substring(9)]=c[d].value)}Oc=b}Nc(Oc)};}).call(this);