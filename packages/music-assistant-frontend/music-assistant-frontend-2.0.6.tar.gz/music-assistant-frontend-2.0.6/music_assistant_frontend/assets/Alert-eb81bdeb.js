import{p as T,aH as I,m as L,g as z,f as F,c as n,d as j,t as w,ad as E,j as a,k,v as R,x as H,W as O,B as J,y as K,Z as M}from"./index-dcf0de03.js";import{a as N}from"./ListItem-6dad7331.js";import{d as W}from"./VListItem-943ee224.js";import{a as Z,n as q,J as G,b as Q,y as U,z as X,c as Y,d as ee,A as te,D as ae,p as le,K as se,f as ne,B as oe,C as re,g as ie,H as ce,E as ue,j as de,F as f,V as ve}from"./VBtn-a0da5efe.js";const me=W("v-alert-title"),ye=["success","info","warning","error"],fe=T({border:{type:[Boolean,String],validator:e=>typeof e=="boolean"||["top","end","bottom","start"].includes(e)},borderColor:String,closable:Boolean,closeIcon:{type:I,default:"$close"},closeLabel:{type:String,default:"$vuetify.close"},icon:{type:[Boolean,String,Function,Object],default:null},modelValue:{type:Boolean,default:!0},prominent:Boolean,title:String,text:String,type:{type:String,validator:e=>ye.includes(e)},...Z(),...q(),...G(),...Q(),...U(),...X(),...Y(),...ee(),...L(),...te({variant:"flat"})},"VAlert"),ke=z()({name:"VAlert",props:fe(),emits:{"click:close":e=>!0,"update:modelValue":e=>!0},setup(e,o){let{emit:r,slots:t}=o;const c=F(e,"modelValue"),l=n(()=>{if(e.icon!==!1)return e.type?e.icon??`$${e.type}`:e.icon}),d=n(()=>({color:e.color??e.type,variant:e.variant})),{themeClasses:i}=j(e),{colorClasses:_,colorStyles:b,variantClasses:P}=ae(d),{densityClasses:p}=le(e),{dimensionStyles:C}=se(e),{elevationClasses:V}=ne(e),{locationStyles:g}=oe(e),{positionClasses:x}=re(e),{roundedClasses:S}=ie(e),{textColorClasses:A,textColorStyles:B}=ce(w(e,"borderColor")),{t:$}=E(),v=n(()=>({"aria-label":$(e.closeLabel),onClick(u){c.value=!1,r("click:close",u)}}));return()=>{const u=!!(t.prepend||l.value),h=!!(t.title||e.title),D=!!(t.close||e.closable);return c.value&&a(e.tag,{class:["v-alert",e.border&&{"v-alert--border":!!e.border,[`v-alert--border-${e.border===!0?"start":e.border}`]:!0},{"v-alert--prominent":e.prominent},i.value,_.value,p.value,V.value,x.value,S.value,P.value,e.class],style:[b.value,C.value,g.value,e.style],role:"alert"},{default:()=>{var m,y;return[ue(!1,"v-alert"),e.border&&a("div",{key:"border",class:["v-alert__border",A.value],style:B.value},null),u&&a("div",{key:"prepend",class:"v-alert__prepend"},[t.prepend?a(f,{key:"prepend-defaults",disabled:!l.value,defaults:{VIcon:{density:e.density,icon:l.value,size:e.prominent?44:28}}},t.prepend):a(de,{key:"prepend-icon",density:e.density,icon:l.value,size:e.prominent?44:28},null)]),a("div",{class:"v-alert__content"},[h&&a(me,{key:"title"},{default:()=>{var s;return[((s=t.title)==null?void 0:s.call(t))??e.title]}}),((m=t.text)==null?void 0:m.call(t))??e.text,(y=t.default)==null?void 0:y.call(t)]),t.append&&a("div",{key:"append",class:"v-alert__append"},[t.append()]),D&&a("div",{key:"close",class:"v-alert__close"},[t.close?a(f,{key:"close-defaults",defaults:{VBtn:{icon:e.closeIcon,size:"x-small",variant:"text"}}},{default:()=>{var s;return[(s=t.close)==null?void 0:s.call(t,{props:v.value})]}}):a(ve,k({key:"close-btn",icon:e.closeIcon,size:"x-small",variant:"text"},v.value),null)])]}})}}}),_e={setup(e,o){const r=n(()=>({}));return{alertProps:n(()=>({...r.value,...o.attrs}))}}};function be(e,o,r,t,c,l){return R(),H(ke,k(t.alertProps,{class:"alert",color:"primary",density:"compact",prominent:""}),O({_:2},[J(e.$slots,(d,i)=>({name:i,fn:K(()=>[M(e.$slots,i)])}))]),1040)}const ge=N(_e,[["render",be]]);export{ge as A};
