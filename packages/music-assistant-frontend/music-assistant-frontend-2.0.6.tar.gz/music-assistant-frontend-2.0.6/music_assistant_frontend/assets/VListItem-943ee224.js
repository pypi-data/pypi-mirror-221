import{a as N,n as J,c as Q,S as Pe,d as q,A as W,D as X,p as Y,g as Z,T as Ve,i as ee,l as Ie,j as L,E as te,m as Me,J as Oe,b as Le,Q as Be,R as De,U as Ne,u as Re,K as je,f as _e,F as x}from"./VBtn-a0da5efe.js";import{g as R,aF as Fe,bi as Ge,aG as Te,ag as V,s as P,ae as I,bg as w,r as k,p as j,f as H,c as g,b as ne,at as ze,as as Ee,aH as B,m as ae,d as le,j as f,b2 as K,w as xe,bj as He,R as Ke,af as Ue,F as U}from"./index-dcf0de03.js";function se(e){let r=arguments.length>1&&arguments[1]!==void 0?arguments[1]:"div",l=arguments.length>2?arguments[2]:void 0;return R()({name:l??Fe(Ge(e.replace(/__/g,"-"))),props:{tag:{type:String,default:r},...N()},setup(t,a){let{slots:n}=a;return()=>{var s;return Te(t.tag,{class:[e,t.class],style:t.style},(s=n.default)==null?void 0:s.call(n))}}})}const D=Symbol.for("vuetify:list");function st(){const e=V(D,{hasPrepend:P(!1),updateHasPrepend:()=>null}),r={hasPrepend:P(!1),updateHasPrepend:l=>{l&&(r.hasPrepend.value=l)}};return I(D,r),e}function $e(){return V(D,null)}const Je={open:e=>{let{id:r,value:l,opened:t,parents:a}=e;if(l){const n=new Set;n.add(r);let s=a.get(r);for(;s!=null;)n.add(s),s=a.get(s);return n}else return t.delete(r),t},select:()=>null},ie={open:e=>{let{id:r,value:l,opened:t,parents:a}=e;if(l){let n=a.get(r);for(t.add(r);n!=null&&n!==r;)t.add(n),n=a.get(n);return t}else t.delete(r);return t},select:()=>null},Qe={open:ie.open,select:e=>{let{id:r,value:l,opened:t,parents:a}=e;if(!l)return t;const n=[];let s=a.get(r);for(;s!=null;)n.push(s),s=a.get(s);return new Set(n)}},_=e=>{const r={select:l=>{let{id:t,value:a,selected:n}=l;if(t=w(t),e&&!a){const s=Array.from(n.entries()).reduce((c,y)=>{let[S,m]=y;return m==="on"?[...c,S]:c},[]);if(s.length===1&&s[0]===t)return n}return n.set(t,a?"on":"off"),n},in:(l,t,a)=>{let n=new Map;for(const s of l||[])n=r.select({id:s,value:!0,selected:new Map(n),children:t,parents:a});return n},out:l=>{const t=[];for(const[a,n]of l.entries())n==="on"&&t.push(a);return t}};return r},re=e=>{const r=_(e);return{select:t=>{let{selected:a,id:n,...s}=t;n=w(n);const c=a.has(n)?new Map([[n,a.get(n)]]):new Map;return r.select({...s,id:n,selected:c})},in:(t,a,n)=>{let s=new Map;return t!=null&&t.length&&(s=r.in(t.slice(0,1),a,n)),s},out:(t,a,n)=>r.out(t,a,n)}},qe=e=>{const r=_(e);return{select:t=>{let{id:a,selected:n,children:s,...c}=t;return a=w(a),s.has(a)?n:r.select({id:a,selected:n,children:s,...c})},in:r.in,out:r.out}},We=e=>{const r=re(e);return{select:t=>{let{id:a,selected:n,children:s,...c}=t;return a=w(a),s.has(a)?n:r.select({id:a,selected:n,children:s,...c})},in:r.in,out:r.out}},Xe=e=>{const r={select:l=>{let{id:t,value:a,selected:n,children:s,parents:c}=l;t=w(t);const y=new Map(n),S=[t];for(;S.length;){const i=S.shift();n.set(i,a?"on":"off"),s.has(i)&&S.push(...s.get(i))}let m=c.get(t);for(;m;){const i=s.get(m),u=i.every(o=>n.get(o)==="on"),d=i.every(o=>!n.has(o)||n.get(o)==="off");n.set(m,u?"on":d?"off":"indeterminate"),m=c.get(m)}return e&&!a&&Array.from(n.entries()).reduce((u,d)=>{let[o,p]=d;return p==="on"?[...u,o]:u},[]).length===0?y:n},in:(l,t,a)=>{let n=new Map;for(const s of l||[])n=r.select({id:s,value:!0,selected:new Map(n),children:t,parents:a});return n},out:(l,t)=>{const a=[];for(const[n,s]of l.entries())s==="on"&&!t.has(n)&&a.push(n);return a}};return r},A=Symbol.for("vuetify:nested"),ue={id:P(),root:{register:()=>null,unregister:()=>null,parents:k(new Map),children:k(new Map),open:()=>null,openOnSelect:()=>null,select:()=>null,opened:k(new Set),selected:k(new Map),selectedValues:k([])}},it=j({selectStrategy:[String,Function],openStrategy:[String,Object],opened:Array,selected:Array,mandatory:Boolean},"nested"),rt=e=>{let r=!1;const l=k(new Map),t=k(new Map),a=H(e,"opened",e.opened,i=>new Set(i),i=>[...i.values()]),n=g(()=>{if(typeof e.selectStrategy=="object")return e.selectStrategy;switch(e.selectStrategy){case"single-leaf":return We(e.mandatory);case"leaf":return qe(e.mandatory);case"independent":return _(e.mandatory);case"single-independent":return re(e.mandatory);case"classic":default:return Xe(e.mandatory)}}),s=g(()=>{if(typeof e.openStrategy=="object")return e.openStrategy;switch(e.openStrategy){case"list":return Qe;case"single":return Je;case"multiple":default:return ie}}),c=H(e,"selected",e.selected,i=>n.value.in(i,l.value,t.value),i=>n.value.out(i,l.value,t.value));ne(()=>{r=!0});function y(i){const u=[];let d=i;for(;d!=null;)u.unshift(d),d=t.value.get(d);return u}const S=ze("nested"),m={id:P(),root:{opened:a,selected:c,selectedValues:g(()=>{const i=[];for(const[u,d]of c.value.entries())d==="on"&&i.push(u);return i}),register:(i,u,d)=>{u&&i!==u&&t.value.set(i,u),d&&l.value.set(i,[]),u!=null&&l.value.set(u,[...l.value.get(u)||[],i])},unregister:i=>{if(r)return;l.value.delete(i);const u=t.value.get(i);if(u){const d=l.value.get(u)??[];l.value.set(u,d.filter(o=>o!==i))}t.value.delete(i),a.value.delete(i)},open:(i,u,d)=>{S.emit("click:open",{id:i,value:u,path:y(i),event:d});const o=s.value.open({id:i,value:u,opened:new Set(a.value),children:l.value,parents:t.value,event:d});o&&(a.value=o)},openOnSelect:(i,u,d)=>{const o=s.value.select({id:i,value:u,selected:new Map(c.value),opened:new Set(a.value),children:l.value,parents:t.value,event:d});o&&(a.value=o)},select:(i,u,d)=>{S.emit("click:select",{id:i,value:u,path:y(i),event:d});const o=n.value.select({id:i,value:u,selected:new Map(c.value),children:l.value,parents:t.value,event:d});o&&(c.value=o),m.root.openOnSelect(i,u,d)},children:l,parents:t}};return I(A,m),m.root},Ye=(e,r)=>{const l=V(A,ue),t=Symbol(Ee()),a=g(()=>e.value!==void 0?e.value:t),n={...l,id:a,open:(s,c)=>l.root.open(a.value,s,c),openOnSelect:(s,c)=>l.root.openOnSelect(a.value,s,c),isOpen:g(()=>l.root.opened.value.has(a.value)),parent:g(()=>l.root.parents.value.get(a.value)),select:(s,c)=>l.root.select(a.value,s,c),isSelected:g(()=>l.root.selected.value.get(w(a.value))==="on"),isIndeterminate:g(()=>l.root.selected.value.get(a.value)==="indeterminate"),isLeaf:g(()=>!l.root.children.value.get(a.value)),isGroupActivator:l.isGroupActivator};return!l.isGroupActivator&&l.root.register(a.value,l.id.value,r),ne(()=>{!l.isGroupActivator&&l.root.unregister(a.value)}),r&&I(A,n),n},ut=()=>{const e=V(A,ue);I(A,{...e,isGroupActivator:!0})};const Ze=se("v-list-item-subtitle"),et=se("v-list-item-title");const tt=j({start:Boolean,end:Boolean,icon:B,image:String,...N(),...J(),...Q(),...Pe(),...q(),...ae(),...W({variant:"flat"})},"VAvatar"),$=R()({name:"VAvatar",props:tt(),setup(e,r){let{slots:l}=r;const{themeClasses:t}=le(e),{colorClasses:a,colorStyles:n,variantClasses:s}=X(e),{densityClasses:c}=Y(e),{roundedClasses:y}=Z(e),{sizeClasses:S,sizeStyles:m}=Ve(e);return ee(()=>f(e.tag,{class:["v-avatar",{"v-avatar--start":e.start,"v-avatar--end":e.end},t.value,a.value,c.value,y.value,S.value,s.value,e.class],style:[n.value,m.value,e.style]},{default:()=>{var i;return[e.image?f(Ie,{key:"image",src:e.image,alt:"",cover:!0},null):e.icon?f(L,{key:"icon",icon:e.icon},null):(i=l.default)==null?void 0:i.call(l),te(!1,"v-avatar")]}})),{}}}),nt=j({active:{type:Boolean,default:void 0},activeClass:String,activeColor:String,appendAvatar:String,appendIcon:B,baseColor:String,disabled:Boolean,lines:String,link:{type:Boolean,default:void 0},nav:Boolean,prependAvatar:String,prependIcon:B,ripple:{type:[Boolean,Object],default:!0},subtitle:[String,Number,Boolean],title:[String,Number,Boolean],value:null,onClick:K(),onClickOnce:K(),...Me(),...N(),...J(),...Oe(),...Le(),...Q(),...Be(),...q(),...ae(),...W({variant:"text"})},"VListItem"),ct=R()({name:"VListItem",directives:{Ripple:De},props:nt(),emits:{click:e=>!0},setup(e,r){let{attrs:l,slots:t,emit:a}=r;const n=Ne(e,l),s=g(()=>e.value===void 0?n.href.value:e.value),{select:c,isSelected:y,isIndeterminate:S,isGroupActivator:m,root:i,parent:u,openOnSelect:d}=Ye(s,!1),o=$e(),p=g(()=>{var v;return e.active!==!1&&(e.active||((v=n.isActive)==null?void 0:v.value)||y.value)}),F=g(()=>e.link!==!1&&n.isLink.value),b=g(()=>!e.disabled&&e.link!==!1&&(e.link||n.isClickable.value||e.value!=null&&!!o)),ce=g(()=>e.rounded||e.nav),oe=g(()=>e.color??e.activeColor),de=g(()=>({color:p.value?oe.value??e.baseColor:e.baseColor,variant:e.variant}));xe(()=>{var v;return(v=n.isActive)==null?void 0:v.value},v=>{v&&u.value!=null&&i.open(u.value,!0),v&&d(v)},{immediate:!0});const{themeClasses:ve}=le(e),{borderClasses:ge}=Re(e),{colorClasses:fe,colorStyles:me,variantClasses:ye}=X(de),{densityClasses:Se}=Y(e),{dimensionStyles:he}=je(e),{elevationClasses:pe}=_e(e),{roundedClasses:ke}=Z(ce),be=g(()=>e.lines?`v-list-item--${e.lines}-line`:void 0),M=g(()=>({isActive:p.value,select:c,isSelected:y.value,isIndeterminate:S.value}));function G(v){var C;a("click",v),!(m||!b.value)&&((C=n.navigate)==null||C.call(n,v),e.value!=null&&c(!y.value,v))}function we(v){(v.key==="Enter"||v.key===" ")&&(v.preventDefault(),G(v))}return ee(()=>{const v=F.value?"a":e.tag,C=t.title||e.title,Ae=t.subtitle||e.subtitle,T=!!(e.appendAvatar||e.appendIcon),Ce=!!(T||t.append),z=!!(e.prependAvatar||e.prependIcon),O=!!(z||t.prepend);return o==null||o.updateHasPrepend(O),e.activeColor&&He("active-color",["color","base-color"]),Ke(f(v,{class:["v-list-item",{"v-list-item--active":p.value,"v-list-item--disabled":e.disabled,"v-list-item--link":b.value,"v-list-item--nav":e.nav,"v-list-item--prepend":!O&&(o==null?void 0:o.hasPrepend.value),[`${e.activeClass}`]:e.activeClass&&p.value},ve.value,ge.value,fe.value,Se.value,pe.value,be.value,ke.value,ye.value,e.class],style:[me.value,he.value,e.style],href:n.href.value,tabindex:b.value?o?-2:0:void 0,onClick:G,onKeydown:b.value&&!F.value&&we},{default:()=>{var E;return[te(b.value||p.value,"v-list-item"),O&&f("div",{key:"prepend",class:"v-list-item__prepend"},[t.prepend?f(x,{key:"prepend-defaults",disabled:!z,defaults:{VAvatar:{density:e.density,image:e.prependAvatar},VIcon:{density:e.density,icon:e.prependIcon},VListItemAction:{start:!0}}},{default:()=>{var h;return[(h=t.prepend)==null?void 0:h.call(t,M.value)]}}):f(U,null,[e.prependAvatar&&f($,{key:"prepend-avatar",density:e.density,image:e.prependAvatar},null),e.prependIcon&&f(L,{key:"prepend-icon",density:e.density,icon:e.prependIcon},null)])]),f("div",{class:"v-list-item__content","data-no-activator":""},[C&&f(et,{key:"title"},{default:()=>{var h;return[((h=t.title)==null?void 0:h.call(t,{title:e.title}))??e.title]}}),Ae&&f(Ze,{key:"subtitle"},{default:()=>{var h;return[((h=t.subtitle)==null?void 0:h.call(t,{subtitle:e.subtitle}))??e.subtitle]}}),(E=t.default)==null?void 0:E.call(t,M.value)]),Ce&&f("div",{key:"append",class:"v-list-item__append"},[t.append?f(x,{key:"append-defaults",disabled:!T,defaults:{VAvatar:{density:e.density,image:e.appendAvatar},VIcon:{density:e.density,icon:e.appendIcon},VListItemAction:{end:!0}}},{default:()=>{var h;return[(h=t.append)==null?void 0:h.call(t,M.value)]}}):f(U,null,[e.appendIcon&&f(L,{key:"append-icon",density:e.density,icon:e.appendIcon},null),e.appendAvatar&&f($,{key:"append-avatar",density:e.density,image:e.appendAvatar},null)])])]}}),[[Ue("ripple"),b.value&&e.ripple]])}),{}}});export{ct as V,Ze as a,$ as b,et as c,se as d,Ye as e,$e as f,st as g,rt as h,it as m,ut as u};
