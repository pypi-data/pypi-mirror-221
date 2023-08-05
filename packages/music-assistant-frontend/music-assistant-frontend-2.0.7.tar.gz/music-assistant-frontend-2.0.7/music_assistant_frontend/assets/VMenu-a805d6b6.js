import{b3 as qe,b8 as je,g as K,j as w,k as R,T as me,p as L,s as z,o as ze,c as C,b9 as Ge,ba as wt,aH as te,t as V,R as Ke,ah as Ue,m as Se,d as pe,a as D,a_ as St,bb as j,aI as Ye,i as pt,r as G,bc as ye,at as xe,aO as Y,aY as Ce,aZ as H,w as M,bd as xt,n as re,aQ as Ae,aW as Ee,be as Xe,ag as Pe,bf as Ct,b7 as Et,e as Pt,aw as Ze,ae as Je,bg as Ot,f as Qe,u as kt,bh as At,af as Vt,F as Lt,ay as Tt,as as Bt}from"./index-8ef8125d.js";import{a as Q,f as Ft,s as ge,g as It,n as et,b as Dt,B as se,h as Ve}from"./index-a4f9d82d.js";import{u as Rt,e as Mt,f as _t,g as tt,V as Le,m as Nt,h as $t}from"./VListItem-b049d12d.js";import{a as ee,d as Oe,i as Z,F as nt,M as ot,H as at,m as Ht,n as Wt,J as it,b as qt,c as jt,A as zt,e as rt,u as Gt,p as Kt,K as st,f as Ut,g as Yt,W as Te,X as le,Y as ue,Z as Be,_ as Fe,G as Xt,h as Zt,$ as Jt}from"./VBtn-49774b84.js";const ne=new WeakMap;function Qt(e,n){Object.keys(n).forEach(t=>{if(qe(t)){const o=je(t),a=ne.get(e);if(n[t]==null)a==null||a.forEach(i=>{const[s,r]=i;s===o&&(e.removeEventListener(o,r),a.delete(i))});else if(!a||![...a].some(i=>i[0]===o&&i[1]===n[t])){e.addEventListener(o,n[t]);const i=a||new Set;i.add([o,n[t]]),ne.has(e)||ne.set(e,i)}}else n[t]==null?e.removeAttribute(t):e.setAttribute(t,n[t])})}function en(e,n){Object.keys(n).forEach(t=>{if(qe(t)){const o=je(t),a=ne.get(e);a==null||a.forEach(i=>{const[s,r]=i;s===o&&(e.removeEventListener(o,r),a.delete(i))})}else e.removeAttribute(t)})}function lt(e){if(typeof e.getRootNode!="function"){for(;e.parentNode;)e=e.parentNode;return e!==document?null:document}const n=e.getRootNode();return n!==document&&n.getRootNode({composed:!0})!==document?null:n}function tn(e){let n=arguments.length>1&&arguments[1]!==void 0?arguments[1]:!1;for(;e;){if(n?nn(e):ke(e))return e;e=e.parentElement}return document.scrollingElement}function ae(e,n){const t=[];if(n&&e&&!n.contains(e))return t;for(;e&&(ke(e)&&t.push(e),e!==n);)e=e.parentElement;return t}function ke(e){if(!e||e.nodeType!==Node.ELEMENT_NODE)return!1;const n=window.getComputedStyle(e);return n.overflowY==="scroll"||n.overflowY==="auto"&&e.scrollHeight>e.clientHeight}function nn(e){if(!e||e.nodeType!==Node.ELEMENT_NODE)return!1;const n=window.getComputedStyle(e);return["scroll","auto"].includes(n.overflowY)}function on(e){for(;e;){if(window.getComputedStyle(e).position==="fixed")return!0;e=e.offsetParent}return!1}const an=L({target:Object},"v-dialog-transition"),rn=K()({name:"VDialogTransition",props:an(),setup(e,n){let{slots:t}=n;const o={onBeforeEnter(a){a.style.pointerEvents="none",a.style.visibility="hidden"},async onEnter(a,i){var g;await new Promise(h=>requestAnimationFrame(h)),await new Promise(h=>requestAnimationFrame(h)),a.style.visibility="";const{x:s,y:r,sx:l,sy:f,speed:d}=De(e.target,a),y=Q(a,[{transform:`translate(${s}px, ${r}px) scale(${l}, ${f})`,opacity:0},{}],{duration:225*d,easing:Ft});(g=Ie(a))==null||g.forEach(h=>{Q(h,[{opacity:0},{opacity:0,offset:.33},{}],{duration:225*2*d,easing:ge})}),y.finished.then(()=>i())},onAfterEnter(a){a.style.removeProperty("pointer-events")},onBeforeLeave(a){a.style.pointerEvents="none"},async onLeave(a,i){var g;await new Promise(h=>requestAnimationFrame(h));const{x:s,y:r,sx:l,sy:f,speed:d}=De(e.target,a);Q(a,[{},{transform:`translate(${s}px, ${r}px) scale(${l}, ${f})`,opacity:0}],{duration:125*d,easing:It}).finished.then(()=>i()),(g=Ie(a))==null||g.forEach(h=>{Q(h,[{},{opacity:0,offset:.2},{opacity:0}],{duration:125*2*d,easing:ge})})},onAfterLeave(a){a.style.removeProperty("pointer-events")}};return()=>e.target?w(me,R({name:"dialog-transition"},o,{css:!1}),t):w(me,{name:"dialog-transition"},t)}});function Ie(e){var t;const n=(t=e.querySelector(":scope > .v-card, :scope > .v-sheet, :scope > .v-list"))==null?void 0:t.children;return n&&[...n]}function De(e,n){const t=e.getBoundingClientRect(),o=et(n),[a,i]=getComputedStyle(n).transformOrigin.split(" ").map(p=>parseFloat(p)),[s,r]=getComputedStyle(n).getPropertyValue("--v-overlay-anchor-origin").split(" ");let l=t.left+t.width/2;s==="left"||r==="left"?l-=t.width/2:(s==="right"||r==="right")&&(l+=t.width/2);let f=t.top+t.height/2;s==="top"||r==="top"?f-=t.height/2:(s==="bottom"||r==="bottom")&&(f+=t.height/2);const d=t.width/o.width,y=t.height/o.height,g=Math.max(1,d,y),h=d/g||0,v=y/g||0,c=o.width*o.height/(window.innerWidth*window.innerHeight),m=c>.12?Math.min(1.5,(c-.12)*10+1):1;return{x:l-(a+o.left),y:f-(i+o.top),sx:h,sy:v,speed:m}}function sn(){const e=z(!1);return ze(()=>{window.requestAnimationFrame(()=>{e.value=!0})}),{ssrBootStyles:C(()=>e.value?void 0:{transition:"none !important"}),isBooted:Ge(e)}}const ln=wt({name:"VListGroupActivator",setup(e,n){let{slots:t}=n;return Rt(),()=>{var o;return(o=t.default)==null?void 0:o.call(t)}}}),un=L({activeColor:String,baseColor:String,color:String,collapseIcon:{type:te,default:"$collapse"},expandIcon:{type:te,default:"$expand"},prependIcon:te,appendIcon:te,fluid:Boolean,subgroup:Boolean,title:String,value:null,...ee(),...Oe()},"VListGroup"),Re=K()({name:"VListGroup",props:un(),setup(e,n){let{slots:t}=n;const{isOpen:o,open:a,id:i}=Mt(V(e,"value"),!0),s=C(()=>`v-list-group--id-${String(i.value)}`),r=_t(),{isBooted:l}=sn();function f(h){a(!o.value,h)}const d=C(()=>({onClick:f,class:"v-list-group__header",id:s.value})),y=C(()=>o.value?e.collapseIcon:e.expandIcon),g=C(()=>({VListItem:{active:o.value,activeColor:e.activeColor,baseColor:e.baseColor,color:e.color,prependIcon:e.prependIcon||e.subgroup&&y.value,appendIcon:e.appendIcon||!e.subgroup&&y.value,title:e.title,value:e.value}}));return Z(()=>w(e.tag,{class:["v-list-group",{"v-list-group--prepend":r==null?void 0:r.hasPrepend.value,"v-list-group--fluid":e.fluid,"v-list-group--subgroup":e.subgroup,"v-list-group--open":o.value},e.class],style:e.style},{default:()=>[t.activator&&w(nt,{defaults:g.value},{default:()=>[w(ln,null,{default:()=>[t.activator({props:d.value,isOpen:o.value})]})]}),w(ot,{transition:{component:Dt},disabled:!l.value},{default:()=>{var h;return[Ke(w("div",{class:"v-list-group__items",role:"group","aria-labelledby":s.value},[(h=t.default)==null?void 0:h.call(t)]),[[Ue,o.value]])]}})]})),{}}}),cn=L({color:String,inset:Boolean,sticky:Boolean,title:String,...ee(),...Oe()},"VListSubheader"),fn=K()({name:"VListSubheader",props:cn(),setup(e,n){let{slots:t}=n;const{textColorClasses:o,textColorStyles:a}=at(V(e,"color"));return Z(()=>{const i=!!(t.default||e.title);return w(e.tag,{class:["v-list-subheader",{"v-list-subheader--inset":e.inset,"v-list-subheader--sticky":e.sticky},o.value,e.class],style:[{textColorStyles:a},e.style]},{default:()=>{var s;return[i&&w("div",{class:"v-list-subheader__text"},[((s=t.default)==null?void 0:s.call(t))??e.title])]}})}),{}}});const dn=L({color:String,inset:Boolean,length:[Number,String],thickness:[Number,String],vertical:Boolean,...ee(),...Se()},"VDivider"),vn=K()({name:"VDivider",props:dn(),setup(e,n){let{attrs:t}=n;const{themeClasses:o}=pe(e),{textColorClasses:a,textColorStyles:i}=at(V(e,"color")),s=C(()=>{const r={};return e.length&&(r[e.vertical?"maxHeight":"maxWidth"]=D(e.length)),e.thickness&&(r[e.vertical?"borderRightWidth":"borderTopWidth"]=D(e.thickness)),r});return Z(()=>w("hr",{class:[{"v-divider":!0,"v-divider--inset":e.inset,"v-divider--vertical":e.vertical},o.value,a.value,e.class],style:[s.value,i.value,e.style],"aria-orientation":!t.role||t.role==="separator"?e.vertical?"vertical":"horizontal":void 0,role:`${t.role||"separator"}`},null)),{}}}),mn=L({items:Array},"VListChildren"),ut=K()({name:"VListChildren",props:mn(),setup(e,n){let{slots:t}=n;return tt(),()=>{var o,a;return((o=t.default)==null?void 0:o.call(t))??((a=e.items)==null?void 0:a.map(i=>{var h,v;let{children:s,props:r,type:l,raw:f}=i;if(l==="divider")return((h=t.divider)==null?void 0:h.call(t,{props:r}))??w(vn,r,null);if(l==="subheader")return((v=t.subheader)==null?void 0:v.call(t,{props:r}))??w(fn,r,null);const d={subtitle:t.subtitle?c=>{var m;return(m=t.subtitle)==null?void 0:m.call(t,{...c,item:f})}:void 0,prepend:t.prepend?c=>{var m;return(m=t.prepend)==null?void 0:m.call(t,{...c,item:f})}:void 0,append:t.append?c=>{var m;return(m=t.append)==null?void 0:m.call(t,{...c,item:f})}:void 0,title:t.title?c=>{var m;return(m=t.title)==null?void 0:m.call(t,{...c,item:f})}:void 0},[y,g]=Re.filterProps(r);return s?w(Re,R({value:r==null?void 0:r.value},y),{activator:c=>{let{props:m}=c;return t.header?t.header({props:{...r,...m}}):w(Le,R(r,m),d)},default:()=>w(ut,{items:s},t)}):t.item?t.item({props:r}):w(Le,r,d)}))}}}),yn=L({items:{type:Array,default:()=>[]},itemTitle:{type:[String,Array,Function],default:"title"},itemValue:{type:[String,Array,Function],default:"value"},itemChildren:{type:[Boolean,String,Array,Function],default:"children"},itemProps:{type:[Boolean,String,Array,Function],default:"props"},returnObject:Boolean},"list-items");function ct(e,n){const t=j(n,e.itemTitle,n),o=e.returnObject?n:j(n,e.itemValue,t),a=j(n,e.itemChildren),i=e.itemProps===!0?typeof n=="object"&&n!=null&&!Array.isArray(n)?"children"in n?Ye(n,["children"])[1]:n:void 0:j(n,e.itemProps),s={title:t,value:o,...i};return{title:String(s.title??""),value:s.value,props:s,children:Array.isArray(a)?ft(e,a):void 0,raw:n}}function ft(e,n){const t=[];for(const o of n)t.push(ct(e,o));return t}function Qn(e){const n=C(()=>ft(e,e.items));return gn(n,t=>ct(e,t))}function gn(e,n){function t(a){return a.filter(i=>i!==null||e.value.some(s=>s.value===null)).map(i=>e.value.find(r=>St(i,r.value))??n(i))}function o(a){return a.map(i=>{let{value:s}=i;return s})}return{items:e,transformIn:t,transformOut:o}}function hn(e){return typeof e=="string"||typeof e=="number"||typeof e=="boolean"}function bn(e,n){const t=j(n,e.itemType,"item"),o=hn(n)?n:j(n,e.itemTitle),a=j(n,e.itemValue,void 0),i=j(n,e.itemChildren),s=e.itemProps===!0?Ye(n,["children"])[1]:j(n,e.itemProps),r={title:o,value:a,...s};return{type:t,title:r.title,value:r.value,props:r,children:t==="item"&&i?dt(e,i):void 0,raw:n}}function dt(e,n){const t=[];for(const o of n)t.push(bn(e,o));return t}function wn(e){return{items:C(()=>dt(e,e.items))}}const Sn=L({baseColor:String,activeColor:String,activeClass:String,bgColor:String,disabled:Boolean,lines:{type:[Boolean,String],default:"one"},nav:Boolean,...Nt({selectStrategy:"single-leaf",openStrategy:"list"}),...Ht(),...ee(),...Wt(),...it(),...qt(),itemType:{type:String,default:"type"},...yn(),...jt(),...Oe(),...Se(),...zt({variant:"text"})},"VList"),eo=K()({name:"VList",props:Sn(),emits:{"update:selected":e=>!0,"update:opened":e=>!0,"click:open":e=>!0,"click:select":e=>!0},setup(e,n){let{slots:t}=n;const{items:o}=wn(e),{themeClasses:a}=pe(e),{backgroundColorClasses:i,backgroundColorStyles:s}=rt(V(e,"bgColor")),{borderClasses:r}=Gt(e),{densityClasses:l}=Kt(e),{dimensionStyles:f}=st(e),{elevationClasses:d}=Ut(e),{roundedClasses:y}=Yt(e),{open:g,select:h}=$t(e),v=C(()=>e.lines?`v-list--${e.lines}-line`:void 0),c=V(e,"activeColor"),m=V(e,"baseColor"),p=V(e,"color");tt(),pt({VListGroup:{activeColor:c,baseColor:m,color:p},VListItem:{activeClass:V(e,"activeClass"),activeColor:c,baseColor:m,color:p,density:V(e,"density"),disabled:V(e,"disabled"),lines:V(e,"lines"),nav:V(e,"nav"),variant:V(e,"variant")}});const b=z(!1),u=G();function T(O){b.value=!0}function N(O){b.value=!1}function W(O){var F;!b.value&&!(O.relatedTarget&&((F=u.value)!=null&&F.contains(O.relatedTarget)))&&B()}function q(O){if(u.value){if(O.key==="ArrowDown")B("next");else if(O.key==="ArrowUp")B("prev");else if(O.key==="Home")B("first");else if(O.key==="End")B("last");else return;O.preventDefault()}}function B(O){if(u.value)return ye(u.value,O)}return Z(()=>w(e.tag,{ref:u,class:["v-list",{"v-list--disabled":e.disabled,"v-list--nav":e.nav},a.value,i.value,r.value,l.value,d.value,v.value,y.value,e.class],style:[s.value,f.value,e.style],tabindex:e.disabled||b.value?-1:0,role:"listbox","aria-activedescendant":void 0,onFocusin:T,onFocusout:N,onFocus:W,onKeydown:q},{default:()=>[w(ut,{items:o.value},t)]})),{open:g,select:h,focus:B}}});function vt(){const n=xe("useScopeId").vnode.scopeId;return{scopeId:n?{[n]:""}:void 0}}function ce(e,n){return{x:e.x+n.x,y:e.y+n.y}}function pn(e,n){return{x:e.x-n.x,y:e.y-n.y}}function Me(e,n){if(e.side==="top"||e.side==="bottom"){const{side:t,align:o}=e,a=o==="left"?0:o==="center"?n.width/2:o==="right"?n.width:o,i=t==="top"?0:t==="bottom"?n.height:t;return ce({x:a,y:i},n)}else if(e.side==="left"||e.side==="right"){const{side:t,align:o}=e,a=t==="left"?0:t==="right"?n.width:t,i=o==="top"?0:o==="center"?n.height/2:o==="bottom"?n.height:o;return ce({x:a,y:i},n)}return ce({x:n.width/2,y:n.height/2},n)}const mt={static:En,connected:On},xn=L({locationStrategy:{type:[String,Function],default:"static",validator:e=>typeof e=="function"||e in mt},location:{type:String,default:"bottom"},origin:{type:String,default:"auto"},offset:[Number,String,Array]},"VOverlay-location-strategies");function Cn(e,n){const t=G({}),o=G();Y&&(Ce(()=>!!(n.isActive.value&&e.locationStrategy),i=>{var s,r;M(()=>e.locationStrategy,i),H(()=>{o.value=void 0}),typeof e.locationStrategy=="function"?o.value=(s=e.locationStrategy(n,e,t))==null?void 0:s.updateLocation:o.value=(r=mt[e.locationStrategy](n,e,t))==null?void 0:r.updateLocation}),window.addEventListener("resize",a,{passive:!0}),H(()=>{window.removeEventListener("resize",a),o.value=void 0}));function a(i){var s;(s=o.value)==null||s.call(o,i)}return{contentStyles:t,updateLocation:o}}function En(){}function Pn(e,n){n?e.style.removeProperty("left"):e.style.removeProperty("right");const t=et(e);return n?t.x+=parseFloat(e.style.right||0):t.x-=parseFloat(e.style.left||0),t.y-=parseFloat(e.style.top||0),t}function On(e,n,t){on(e.activatorEl.value)&&Object.assign(t.value,{position:"fixed",top:0,[e.isRtl.value?"right":"left"]:0});const{preferredAnchor:a,preferredOrigin:i}=xt(()=>{const v=Te(n.location,e.isRtl.value),c=n.origin==="overlap"?v:n.origin==="auto"?le(v):Te(n.origin,e.isRtl.value);return v.side===c.side&&v.align===ue(c).align?{preferredAnchor:Be(v),preferredOrigin:Be(c)}:{preferredAnchor:v,preferredOrigin:c}}),[s,r,l,f]=["minWidth","minHeight","maxWidth","maxHeight"].map(v=>C(()=>{const c=parseFloat(n[v]);return isNaN(c)?1/0:c})),d=C(()=>{if(Array.isArray(n.offset))return n.offset;if(typeof n.offset=="string"){const v=n.offset.split(" ").map(parseFloat);return v.length<2&&v.push(0),v}return typeof n.offset=="number"?[n.offset,0]:[0,0]});let y=!1;const g=new ResizeObserver(()=>{y&&h()});M([e.activatorEl,e.contentEl],(v,c)=>{let[m,p]=v,[b,u]=c;b&&g.unobserve(b),m&&g.observe(m),u&&g.unobserve(u),p&&g.observe(p)},{immediate:!0}),H(()=>{g.disconnect()});function h(){if(y=!1,requestAnimationFrame(()=>{requestAnimationFrame(()=>y=!0)}),!e.activatorEl.value||!e.contentEl.value)return;const v=e.activatorEl.value.getBoundingClientRect(),c=Pn(e.contentEl.value,e.isRtl.value),m=ae(e.contentEl.value),p=12;m.length||(m.push(document.documentElement),e.contentEl.value.style.top&&e.contentEl.value.style.left||(c.x-=parseFloat(document.documentElement.style.getPropertyValue("--v-body-scroll-x")||0),c.y-=parseFloat(document.documentElement.style.getPropertyValue("--v-body-scroll-y")||0)));const b=m.reduce((k,P)=>{const S=P.getBoundingClientRect(),E=new se({x:P===document.documentElement?0:S.x,y:P===document.documentElement?0:S.y,width:P.clientWidth,height:P.clientHeight});return k?new se({x:Math.max(k.left,E.left),y:Math.max(k.top,E.top),width:Math.min(k.right,E.right)-Math.max(k.left,E.left),height:Math.min(k.bottom,E.bottom)-Math.max(k.top,E.top)}):E},void 0);b.x+=p,b.y+=p,b.width-=p*2,b.height-=p*2;let u={anchor:a.value,origin:i.value};function T(k){const P=new se(c),S=Me(k.anchor,v),E=Me(k.origin,P);let{x:_,y:$}=pn(S,E);switch(k.anchor.side){case"top":$-=d.value[0];break;case"bottom":$+=d.value[0];break;case"left":_-=d.value[0];break;case"right":_+=d.value[0];break}switch(k.anchor.align){case"top":$-=d.value[1];break;case"bottom":$+=d.value[1];break;case"left":_-=d.value[1];break;case"right":_+=d.value[1];break}return P.x+=_,P.y+=$,P.width=Math.min(P.width,l.value),P.height=Math.min(P.height,f.value),{overflows:Ve(P,b),x:_,y:$}}let N=0,W=0;const q={x:0,y:0},B={x:!1,y:!1};let O=-1;for(;!(O++>10);){const{x:k,y:P,overflows:S}=T(u);N+=k,W+=P,c.x+=k,c.y+=P;{const E=Fe(u.anchor),_=S.x.before||S.x.after,$=S.y.before||S.y.after;let X=!1;if(["x","y"].forEach(A=>{if(A==="x"&&_&&!B.x||A==="y"&&$&&!B.y){const x={anchor:{...u.anchor},origin:{...u.origin}},I=A==="x"?E==="y"?ue:le:E==="y"?le:ue;x.anchor=I(x.anchor),x.origin=I(x.origin);const{overflows:U}=T(x);(U[A].before<=S[A].before&&U[A].after<=S[A].after||U[A].before+U[A].after<(S[A].before+S[A].after)/2)&&(u=x,X=B[A]=!0)}}),X)continue}S.x.before&&(N+=S.x.before,c.x+=S.x.before),S.x.after&&(N-=S.x.after,c.x-=S.x.after),S.y.before&&(W+=S.y.before,c.y+=S.y.before),S.y.after&&(W-=S.y.after,c.y-=S.y.after);{const E=Ve(c,b);q.x=b.width-E.x.before-E.x.after,q.y=b.height-E.y.before-E.y.after,N+=E.x.before,c.x+=E.x.before,W+=E.y.before,c.y+=E.y.before}break}const F=Fe(u.anchor);return Object.assign(t.value,{"--v-overlay-anchor-origin":`${u.anchor.side} ${u.anchor.align}`,transformOrigin:`${u.origin.side} ${u.origin.align}`,top:D(fe(W)),left:e.isRtl.value?void 0:D(fe(N)),right:e.isRtl.value?D(fe(-N)):void 0,minWidth:D(F==="y"?Math.min(s.value,v.width):s.value),maxWidth:D(_e(Ae(q.x,s.value===1/0?0:s.value,l.value))),maxHeight:D(_e(Ae(q.y,r.value===1/0?0:r.value,f.value)))}),{available:q,contentBox:c}}return M(()=>[a.value,i.value,n.offset,n.minWidth,n.minHeight,n.maxWidth,n.maxHeight],()=>h()),re(()=>{const v=h();if(!v)return;const{available:c,contentBox:m}=v;m.height>c.y&&requestAnimationFrame(()=>{h(),requestAnimationFrame(()=>{h()})})}),{updateLocation:h}}function fe(e){return Math.round(e*devicePixelRatio)/devicePixelRatio}function _e(e){return Math.ceil(e*devicePixelRatio)/devicePixelRatio}let he=!0;const ie=[];function kn(e){!he||ie.length?(ie.push(e),be()):(he=!1,e(),be())}let Ne=-1;function be(){cancelAnimationFrame(Ne),Ne=requestAnimationFrame(()=>{const e=ie.shift();e&&e(),ie.length?be():he=!0})}const oe={none:null,close:Ln,block:Tn,reposition:Bn},An=L({scrollStrategy:{type:[String,Function],default:"block",validator:e=>typeof e=="function"||e in oe}},"VOverlay-scroll-strategies");function Vn(e,n){if(!Y)return;let t;Ee(async()=>{t==null||t.stop(),n.isActive.value&&e.scrollStrategy&&(t=Xe(),await re(),t.active&&t.run(()=>{var o;typeof e.scrollStrategy=="function"?e.scrollStrategy(n,e,t):(o=oe[e.scrollStrategy])==null||o.call(oe,n,e,t)}))}),H(()=>{t==null||t.stop()})}function Ln(e){function n(t){e.isActive.value=!1}yt(e.activatorEl.value??e.contentEl.value,n)}function Tn(e,n){var s;const t=(s=e.root.value)==null?void 0:s.offsetParent,o=[...new Set([...ae(e.activatorEl.value,n.contained?t:void 0),...ae(e.contentEl.value,n.contained?t:void 0)])].filter(r=>!r.classList.contains("v-overlay-scroll-blocked")),a=window.innerWidth-document.documentElement.offsetWidth,i=(r=>ke(r)&&r)(t||document.documentElement);i&&e.root.value.classList.add("v-overlay--scroll-blocked"),o.forEach((r,l)=>{r.style.setProperty("--v-body-scroll-x",D(-r.scrollLeft)),r.style.setProperty("--v-body-scroll-y",D(-r.scrollTop)),r!==document.documentElement&&r.style.setProperty("--v-scrollbar-offset",D(a)),r.classList.add("v-overlay-scroll-blocked")}),H(()=>{o.forEach((r,l)=>{const f=parseFloat(r.style.getPropertyValue("--v-body-scroll-x")),d=parseFloat(r.style.getPropertyValue("--v-body-scroll-y"));r.style.removeProperty("--v-body-scroll-x"),r.style.removeProperty("--v-body-scroll-y"),r.style.removeProperty("--v-scrollbar-offset"),r.classList.remove("v-overlay-scroll-blocked"),r.scrollLeft=-f,r.scrollTop=-d}),i&&e.root.value.classList.remove("v-overlay--scroll-blocked")})}function Bn(e,n,t){let o=!1,a=-1,i=-1;function s(r){kn(()=>{var d,y;const l=performance.now();(y=(d=e.updateLocation).value)==null||y.call(d,r),o=(performance.now()-l)/(1e3/60)>2})}i=(typeof requestIdleCallback>"u"?r=>r():requestIdleCallback)(()=>{t.run(()=>{yt(e.activatorEl.value??e.contentEl.value,r=>{o?(cancelAnimationFrame(a),a=requestAnimationFrame(()=>{a=requestAnimationFrame(()=>{s(r)})})):s(r)})})}),H(()=>{typeof cancelIdleCallback<"u"&&cancelIdleCallback(i),cancelAnimationFrame(a)})}function yt(e,n){const t=[document,...ae(e)];t.forEach(o=>{o.addEventListener("scroll",n,{passive:!0})}),H(()=>{t.forEach(o=>{o.removeEventListener("scroll",n)})})}const we=Symbol.for("vuetify:v-menu"),Fn=L({closeDelay:[Number,String],openDelay:[Number,String]},"delay");function In(e,n){const t={},o=a=>()=>{if(!Y)return Promise.resolve(!0);const i=a==="openDelay";return t.closeDelay&&window.clearTimeout(t.closeDelay),delete t.closeDelay,t.openDelay&&window.clearTimeout(t.openDelay),delete t.openDelay,new Promise(s=>{const r=parseInt(e[a]??0,10);t[a]=window.setTimeout(()=>{n==null||n(i),s(i)},r)})};return{runCloseDelay:o("closeDelay"),runOpenDelay:o("openDelay")}}const Dn=L({activator:[String,Object],activatorProps:{type:Object,default:()=>({})},openOnClick:{type:Boolean,default:void 0},openOnHover:Boolean,openOnFocus:{type:Boolean,default:void 0},closeOnContentClick:Boolean,...Fn()},"VOverlay-activator");function Rn(e,n){let{isActive:t,isTop:o}=n;const a=G();let i=!1,s=!1,r=!0;const l=C(()=>e.openOnFocus||e.openOnFocus==null&&e.openOnHover),f=C(()=>e.openOnClick||e.openOnClick==null&&!e.openOnHover&&!l.value),{runOpenDelay:d,runCloseDelay:y}=In(e,u=>{u===(e.openOnHover&&i||l.value&&s)&&!(e.openOnHover&&t.value&&!o.value)&&(t.value!==u&&(r=!0),t.value=u)}),g={onClick:u=>{u.stopPropagation(),a.value=u.currentTarget||u.target,t.value=!t.value},onMouseenter:u=>{var T;(T=u.sourceCapabilities)!=null&&T.firesTouchEvents||(i=!0,a.value=u.currentTarget||u.target,d())},onMouseleave:u=>{i=!1,y()},onFocus:u=>{Et&&!u.target.matches(":focus-visible")||(s=!0,u.stopPropagation(),a.value=u.currentTarget||u.target,d())},onBlur:u=>{s=!1,u.stopPropagation(),y()}},h=C(()=>{const u={};return f.value&&(u.onClick=g.onClick),e.openOnHover&&(u.onMouseenter=g.onMouseenter,u.onMouseleave=g.onMouseleave),l.value&&(u.onFocus=g.onFocus,u.onBlur=g.onBlur),u}),v=C(()=>{const u={};if(e.openOnHover&&(u.onMouseenter=()=>{i=!0,d()},u.onMouseleave=()=>{i=!1,y()}),l.value&&(u.onFocusin=()=>{s=!0,d()},u.onFocusout=()=>{s=!1,y()}),e.closeOnContentClick){const T=Pe(we,null);u.onClick=()=>{t.value=!1,T==null||T.closeParents()}}return u}),c=C(()=>{const u={};return e.openOnHover&&(u.onMouseenter=()=>{r&&(i=!0,r=!1,d())},u.onMouseleave=()=>{i=!1,y()}),u});M(o,u=>{u&&(e.openOnHover&&!i&&(!l.value||!s)||l.value&&!s&&(!e.openOnHover||!i))&&(t.value=!1)});const m=G();Ee(()=>{m.value&&re(()=>{a.value=Ct(m.value)})});const p=xe("useActivator");let b;return M(()=>!!e.activator,u=>{u&&Y?(b=Xe(),b.run(()=>{Mn(e,p,{activatorEl:a,activatorEvents:h})})):b&&b.stop()},{flush:"post",immediate:!0}),H(()=>{b==null||b.stop()}),{activatorEl:a,activatorRef:m,activatorEvents:h,contentEvents:v,scrimEvents:c}}function Mn(e,n,t){let{activatorEl:o,activatorEvents:a}=t;M(()=>e.activator,(l,f)=>{if(f&&l!==f){const d=r(f);d&&s(d)}l&&re(()=>i())},{immediate:!0}),M(()=>e.activatorProps,()=>{i()}),H(()=>{s()});function i(){let l=arguments.length>0&&arguments[0]!==void 0?arguments[0]:r(),f=arguments.length>1&&arguments[1]!==void 0?arguments[1]:e.activatorProps;l&&Qt(l,R(a.value,f))}function s(){let l=arguments.length>0&&arguments[0]!==void 0?arguments[0]:r(),f=arguments.length>1&&arguments[1]!==void 0?arguments[1]:e.activatorProps;l&&en(l,R(a.value,f))}function r(){var d,y;let l=arguments.length>0&&arguments[0]!==void 0?arguments[0]:e.activator,f;if(l)if(l==="parent"){let g=(y=(d=n==null?void 0:n.proxy)==null?void 0:d.$el)==null?void 0:y.parentNode;for(;g.hasAttribute("data-no-activator");)g=g.parentNode;f=g}else typeof l=="string"?f=document.querySelector(l):"$el"in l?f=l.$el:f=l;return o.value=(f==null?void 0:f.nodeType)===Node.ELEMENT_NODE?f:null,o.value}}function _n(){if(!Y)return z(!1);const{ssr:e}=Pt();if(e){const n=z(!1);return ze(()=>{n.value=!0}),n}else return z(!0)}const Nn=L({eager:Boolean},"lazy");function $n(e,n){const t=z(!1),o=C(()=>t.value||e.eager||n.value);M(n,()=>t.value=!0);function a(){e.eager||(t.value=!1)}return{isBooted:t,hasContent:o,onAfterLeave:a}}const $e=Symbol.for("vuetify:stack"),J=Ze([]);function Hn(e,n,t){const o=xe("useStack"),a=!t,i=Pe($e,void 0),s=Ze({activeChildren:new Set});Je($e,s);const r=z(+n.value);Ce(e,()=>{var y;const d=(y=J.at(-1))==null?void 0:y[1];r.value=d?d+10:+n.value,a&&J.push([o.uid,r.value]),i==null||i.activeChildren.add(o.uid),H(()=>{if(a){const g=Ot(J).findIndex(h=>h[0]===o.uid);J.splice(g,1)}i==null||i.activeChildren.delete(o.uid)})});const l=z(!0);a&&Ee(()=>{var y;const d=((y=J.at(-1))==null?void 0:y[0])===o.uid;setTimeout(()=>l.value=d)});const f=C(()=>!s.activeChildren.size);return{globalTop:Ge(l),localTop:f,stackStyles:C(()=>({zIndex:r.value}))}}function Wn(e){return{teleportTarget:C(()=>{const t=e.value;if(t===!0||!Y)return;const o=t===!1?document.body:typeof t=="string"?document.querySelector(t):t;if(o==null)return;let a=o.querySelector(":scope > .v-overlay-container");return a||(a=document.createElement("div"),a.className="v-overlay-container",o.appendChild(a)),a})}}function qn(){return!0}function gt(e,n,t){if(!e||ht(e,t)===!1)return!1;const o=lt(n);if(typeof ShadowRoot<"u"&&o instanceof ShadowRoot&&o.host===e.target)return!1;const a=(typeof t.value=="object"&&t.value.include||(()=>[]))();return a.push(n),!a.some(i=>i==null?void 0:i.contains(e.target))}function ht(e,n){return(typeof n.value=="object"&&n.value.closeConditional||qn)(e)}function jn(e,n,t){const o=typeof t.value=="function"?t.value:t.value.handler;n._clickOutside.lastMousedownWasOutside&&gt(e,n,t)&&setTimeout(()=>{ht(e,t)&&o&&o(e)},0)}function He(e,n){const t=lt(e);n(document),typeof ShadowRoot<"u"&&t instanceof ShadowRoot&&n(t)}const zn={mounted(e,n){const t=a=>jn(a,e,n),o=a=>{e._clickOutside.lastMousedownWasOutside=gt(a,e,n)};He(e,a=>{a.addEventListener("click",t,!0),a.addEventListener("mousedown",o,!0)}),e._clickOutside||(e._clickOutside={lastMousedownWasOutside:!1}),e._clickOutside[n.instance.$.uid]={onClick:t,onMousedown:o}},unmounted(e,n){e._clickOutside&&(He(e,t=>{var i;if(!t||!((i=e._clickOutside)!=null&&i[n.instance.$.uid]))return;const{onClick:o,onMousedown:a}=e._clickOutside[n.instance.$.uid];t.removeEventListener("click",o,!0),t.removeEventListener("mousedown",a,!0)}),delete e._clickOutside[n.instance.$.uid])}};function Gn(e){const{modelValue:n,color:t,...o}=e;return w(me,{name:"fade-transition",appear:!0},{default:()=>[e.modelValue&&w("div",R({class:["v-overlay__scrim",e.color.backgroundColorClasses.value],style:e.color.backgroundColorStyles.value},o),null)]})}const bt=L({absolute:Boolean,attach:[Boolean,String,Object],closeOnBack:{type:Boolean,default:!0},contained:Boolean,contentClass:null,contentProps:null,disabled:Boolean,noClickAnimation:Boolean,modelValue:Boolean,persistent:Boolean,scrim:{type:[Boolean,String],default:!0},zIndex:{type:[Number,String],default:2e3},...Dn(),...ee(),...it(),...Nn(),...xn(),...An(),...Se(),...Xt()},"VOverlay"),We=K()({name:"VOverlay",directives:{ClickOutside:zn},inheritAttrs:!1,props:{_disableGlobalStack:Boolean,...bt()},emits:{"click:outside":e=>!0,"update:modelValue":e=>!0,afterLeave:()=>!0},setup(e,n){let{slots:t,attrs:o,emit:a}=n;const i=Qe(e,"modelValue"),s=C({get:()=>i.value,set:x=>{x&&e.disabled||(i.value=x)}}),{teleportTarget:r}=Wn(C(()=>e.attach||e.contained)),{themeClasses:l}=pe(e),{rtlClasses:f,isRtl:d}=kt(),{hasContent:y,onAfterLeave:g}=$n(e,s),h=rt(C(()=>typeof e.scrim=="string"?e.scrim:null)),{globalTop:v,localTop:c,stackStyles:m}=Hn(s,V(e,"zIndex"),e._disableGlobalStack),{activatorEl:p,activatorRef:b,activatorEvents:u,contentEvents:T,scrimEvents:N}=Rn(e,{isActive:s,isTop:c}),{dimensionStyles:W}=st(e),q=_n(),{scopeId:B}=vt();M(()=>e.disabled,x=>{x&&(s.value=!1)});const O=G(),F=G(),{contentStyles:k,updateLocation:P}=Cn(e,{isRtl:d,contentEl:F,activatorEl:p,isActive:s});Vn(e,{root:O,contentEl:F,activatorEl:p,isActive:s,updateLocation:P});function S(x){a("click:outside",x),e.persistent?A():s.value=!1}function E(){return s.value&&v.value}Y&&M(s,x=>{x?window.addEventListener("keydown",_):window.removeEventListener("keydown",_)},{immediate:!0});function _(x){var I,U;x.key==="Escape"&&v.value&&(e.persistent?A():(s.value=!1,(I=F.value)!=null&&I.contains(document.activeElement)&&((U=p.value)==null||U.focus())))}const $=Zt();Ce(()=>e.closeOnBack,()=>{Jt($,x=>{v.value&&s.value?(x(!1),e.persistent?A():s.value=!1):x()})});const X=G();M(()=>s.value&&(e.absolute||e.contained)&&r.value==null,x=>{if(x){const I=tn(O.value);I&&I!==document.scrollingElement&&(X.value=I.scrollTop)}});function A(){e.noClickAnimation||F.value&&Q(F.value,[{transformOrigin:"center"},{transform:"scale(1.03)"},{transformOrigin:"center"}],{duration:150,easing:ge})}return Z(()=>{var x;return w(Lt,null,[(x=t.activator)==null?void 0:x.call(t,{isActive:s.value,props:R({ref:b},u.value,e.activatorProps)}),q.value&&y.value&&w(At,{disabled:!r.value,to:r.value},{default:()=>[w("div",R({class:["v-overlay",{"v-overlay--absolute":e.absolute||e.contained,"v-overlay--active":s.value,"v-overlay--contained":e.contained},l.value,f.value,e.class],style:[m.value,{top:D(X.value)},e.style],ref:O},B,o),[w(Gn,R({color:h,modelValue:s.value&&!!e.scrim},N.value),null),w(ot,{appear:!0,persisted:!0,transition:e.transition,target:p.value,onAfterLeave:()=>{g(),a("afterLeave")}},{default:()=>{var I;return[Ke(w("div",R({ref:F,class:["v-overlay__content",e.contentClass],style:[W.value,k.value]},T.value,e.contentProps),[(I=t.default)==null?void 0:I.call(t,{isActive:s})]),[[Ue,s.value],[Vt("click-outside"),{handler:S,closeConditional:E,include:()=>[p.value]}]])]}})])]})])}),{activatorEl:p,animateClick:A,contentEl:F,globalTop:v,localTop:c,updateLocation:P}}}),de=Symbol("Forwarded refs");function ve(e,n){let t=e;for(;t;){const o=Reflect.getOwnPropertyDescriptor(t,n);if(o)return o;t=Object.getPrototypeOf(t)}}function Kn(e){for(var n=arguments.length,t=new Array(n>1?n-1:0),o=1;o<n;o++)t[o-1]=arguments[o];return e[de]=t,new Proxy(e,{get(a,i){if(Reflect.has(a,i))return Reflect.get(a,i);if(!(typeof i=="symbol"||i.startsWith("__"))){for(const s of t)if(s.value&&Reflect.has(s.value,i)){const r=Reflect.get(s.value,i);return typeof r=="function"?r.bind(s.value):r}}},has(a,i){if(Reflect.has(a,i))return!0;if(typeof i=="symbol"||i.startsWith("__"))return!1;for(const s of t)if(s.value&&Reflect.has(s.value,i))return!0;return!1},getOwnPropertyDescriptor(a,i){var r;const s=Reflect.getOwnPropertyDescriptor(a,i);if(s)return s;if(!(typeof i=="symbol"||i.startsWith("__"))){for(const l of t){if(!l.value)continue;const f=ve(l.value,i)??("_"in l.value?ve((r=l.value._)==null?void 0:r.setupState,i):void 0);if(f)return f}for(const l of t){const f=l.value&&l.value[de];if(!f)continue;const d=f.slice();for(;d.length;){const y=d.shift(),g=ve(y.value,i);if(g)return g;const h=y.value&&y.value[de];h&&d.push(...h)}}}}})}const Un=L({id:String,...Tt(bt({closeDelay:250,closeOnContentClick:!0,locationStrategy:"connected",openDelay:300,scrim:!1,scrollStrategy:"reposition",transition:{component:rn}}),["absolute"])},"VMenu"),to=K()({name:"VMenu",props:Un(),emits:{"update:modelValue":e=>!0},setup(e,n){let{slots:t}=n;const o=Qe(e,"modelValue"),{scopeId:a}=vt(),i=Bt(),s=C(()=>e.id||`v-menu-${i}`),r=G(),l=Pe(we,null),f=z(0);Je(we,{register(){++f.value},unregister(){--f.value},closeParents(){setTimeout(()=>{f.value||(o.value=!1,l==null||l.closeParents())},40)}}),M(o,v=>{v?l==null||l.register():l==null||l.unregister()});function d(){l==null||l.closeParents()}function y(v){var c,m;e.disabled||v.key==="Tab"&&(o.value=!1,(m=(c=r.value)==null?void 0:c.activatorEl)==null||m.focus())}function g(v){var m;if(e.disabled)return;const c=(m=r.value)==null?void 0:m.contentEl;c&&o.value?v.key==="ArrowDown"?(v.preventDefault(),ye(c,"next")):v.key==="ArrowUp"&&(v.preventDefault(),ye(c,"prev")):["ArrowDown","ArrowUp"].includes(v.key)&&(o.value=!0,v.preventDefault(),setTimeout(()=>setTimeout(()=>g(v))))}const h=C(()=>R({"aria-haspopup":"menu","aria-expanded":String(o.value),"aria-owns":s.value,onKeydown:g},e.activatorProps));return Z(()=>{const[v]=We.filterProps(e);return w(We,R({ref:r,class:["v-menu",e.class],style:e.style},v,{modelValue:o.value,"onUpdate:modelValue":c=>o.value=c,absolute:!0,activatorProps:h.value,"onClick:outside":d,onKeydown:y},a),{activator:t.activator,default:function(){for(var c=arguments.length,m=new Array(c),p=0;p<c;p++)m[p]=arguments[p];return w(nt,{root:"VMenu"},{default:()=>{var b;return[(b=t.default)==null?void 0:b.call(t,...m)]}})}})}),Kn({id:s,ΨopenChildren:f},r)}});export{eo as V,vt as a,vn as b,to as c,$n as d,We as e,bt as f,Kn as g,tn as h,yn as i,rn as j,Qn as k,Nn as m,sn as u};
