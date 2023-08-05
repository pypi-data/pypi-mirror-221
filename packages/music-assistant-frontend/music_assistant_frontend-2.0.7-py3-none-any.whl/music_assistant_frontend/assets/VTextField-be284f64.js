import{p as N,g as O,c as u,j as l,R as X,ah as le,aH as G,b2 as J,m as re,d as ue,u as de,as as ce,r as S,t as fe,w as ve,a as me,F as w,k as M,b3 as ge,aI as ye,f as be,aJ as xe,af as Ce,b4 as he,n as Z,b5 as Ve}from"./index-8ef8125d.js";import{d as ke,n as _e,a as Ie,e as Pe,s as Fe}from"./index-a4f9d82d.js";import{a as Y,G as Se,i as U,M as Be,O as we,c as Re,L as Te,g as Le,e as $e,H as pe,N as Ae,P as De}from"./VBtn-49774b84.js";import{i as Ee,k as Me,u as te,l as Ne,m as Oe,c as ee}from"./VCheckboxBtn-4c08e900.js";import{g as Ue}from"./VMenu-a805d6b6.js";const je=N({active:Boolean,max:[Number,String],value:{type:[Number,String],default:0},...Y(),...Se({transition:{component:ke}})},"VCounter"),He=O()({name:"VCounter",functional:!0,props:je(),setup(e,y){let{slots:a}=y;const V=u(()=>e.max?`${e.value} / ${e.max}`:String(e.value));return U(()=>l(Be,{transition:e.transition},{default:()=>[X(l("div",{class:["v-counter",e.class],style:e.style},[a.default?a.default({counter:V.value,max:e.max,value:e.value}):V.value]),[[le,e.active]])]})),{}}});const We=N({floating:Boolean,...Y()},"VFieldLabel"),E=O()({name:"VFieldLabel",props:We(),setup(e,y){let{slots:a}=y;return U(()=>l(Ee,{class:["v-field-label",{"v-field-label--floating":e.floating},e.class],style:e.style,"aria-hidden":e.floating||void 0},a)),{}}}),qe=["underlined","outlined","filled","solo","solo-inverted","solo-filled","plain"],ne=N({appendInnerIcon:G,bgColor:String,clearable:Boolean,clearIcon:{type:G,default:"$clear"},active:Boolean,centerAffix:{type:Boolean,default:void 0},color:String,baseColor:String,dirty:Boolean,disabled:{type:Boolean,default:null},error:Boolean,flat:Boolean,label:String,persistentClear:Boolean,prependInnerIcon:G,reverse:Boolean,singleLine:Boolean,variant:{type:String,default:"filled",validator:e=>qe.includes(e)},"onClick:clear":J(),"onClick:appendInner":J(),"onClick:prependInner":J(),...Y(),...we(),...Re(),...re()},"VField"),ae=O()({name:"VField",inheritAttrs:!1,props:{id:String,...Me(),...ne()},emits:{"update:focused":e=>!0,"update:modelValue":e=>!0},setup(e,y){let{attrs:a,emit:V,slots:t}=y;const{themeClasses:b}=ue(e),{loaderClasses:x}=Te(e),{focusClasses:j,isFocused:R,focus:T,blur:L}=te(e),{InputIcon:B}=Ne(e),{roundedClasses:H}=Le(e),{rtlClasses:$}=de(),C=u(()=>e.dirty||e.active),f=u(()=>!e.singleLine&&!!(e.label||t.label)),W=ce(),o=u(()=>e.id||`input-${W}`),q=u(()=>`${o.value}-messages`),p=S(),k=S(),A=S(),n=u(()=>["plain","underlined"].includes(e.variant)),{backgroundColorClasses:d,backgroundColorStyles:c}=$e(fe(e,"bgColor")),{textColorClasses:v,textColorStyles:K}=pe(u(()=>e.error||e.disabled?void 0:C.value&&R.value?e.color:e.baseColor));ve(C,s=>{if(f.value){const i=p.value.$el,m=k.value.$el;requestAnimationFrame(()=>{const g=_e(i),r=m.getBoundingClientRect(),I=r.x-g.x,P=r.y-g.y-(g.height/2-r.height/2),h=r.width/.75,F=Math.abs(h-g.width)>1?{maxWidth:me(h)}:void 0,D=getComputedStyle(i),Q=getComputedStyle(m),ie=parseFloat(D.transitionDuration)*1e3||150,oe=parseFloat(Q.getPropertyValue("--v-field-label-scale")),se=Q.getPropertyValue("color");i.style.visibility="visible",m.style.visibility="hidden",Ie(i,{transform:`translate(${I}px, ${P}px) scale(${oe})`,color:se,...F},{duration:ie,easing:Fe,direction:s?"normal":"reverse"}).finished.then(()=>{i.style.removeProperty("visibility"),m.style.removeProperty("visibility")})})}},{flush:"post"});const _=u(()=>({isActive:C,isFocused:R,controlRef:A,blur:L,focus:T}));function z(s){s.target!==document.activeElement&&s.preventDefault()}return U(()=>{var I,P,h;const s=e.variant==="outlined",i=t["prepend-inner"]||e.prependInnerIcon,m=!!(e.clearable||t.clear),g=!!(t["append-inner"]||e.appendInnerIcon||m),r=t.label?t.label({..._.value,label:e.label,props:{for:o.value}}):e.label;return l("div",M({class:["v-field",{"v-field--active":C.value,"v-field--appended":g,"v-field--center-affix":e.centerAffix??!n.value,"v-field--disabled":e.disabled,"v-field--dirty":e.dirty,"v-field--error":e.error,"v-field--flat":e.flat,"v-field--has-background":!!e.bgColor,"v-field--persistent-clear":e.persistentClear,"v-field--prepended":i,"v-field--reverse":e.reverse,"v-field--single-line":e.singleLine,"v-field--no-label":!r,[`v-field--variant-${e.variant}`]:!0},b.value,d.value,j.value,x.value,H.value,$.value,e.class],style:[c.value,K.value,e.style],onClick:z},a),[l("div",{class:"v-field__overlay"},null),l(Ae,{name:"v-field",active:!!e.loading,color:e.error?"error":typeof e.loading=="string"?e.loading:e.color},{default:t.loader}),i&&l("div",{key:"prepend",class:"v-field__prepend-inner"},[e.prependInnerIcon&&l(B,{key:"prepend-icon",name:"prependInner"},null),(I=t["prepend-inner"])==null?void 0:I.call(t,_.value)]),l("div",{class:"v-field__field","data-no-activator":""},[["filled","solo","solo-inverted","solo-filled"].includes(e.variant)&&f.value&&l(E,{key:"floating-label",ref:k,class:[v.value],floating:!0,for:o.value},{default:()=>[r]}),l(E,{ref:p,for:o.value},{default:()=>[r]}),(P=t.default)==null?void 0:P.call(t,{..._.value,props:{id:o.value,class:"v-field__input","aria-describedby":q.value},focus:T,blur:L})]),m&&l(Pe,{key:"clear"},{default:()=>[X(l("div",{class:"v-field__clearable",onMousedown:F=>{F.preventDefault(),F.stopPropagation()}},[t.clear?t.clear():l(B,{name:"clear"},null)]),[[le,e.dirty]])]}),g&&l("div",{key:"append",class:"v-field__append-inner"},[(h=t["append-inner"])==null?void 0:h.call(t,_.value),e.appendInnerIcon&&l(B,{key:"append-icon",name:"appendInner"},null)]),l("div",{class:["v-field__outline",v.value]},[s&&l(w,null,[l("div",{class:"v-field__outline__start"},null),f.value&&l("div",{class:"v-field__outline__notch"},[l(E,{ref:k,floating:!0,for:o.value},{default:()=>[r]})]),l("div",{class:"v-field__outline__end"},null)]),n.value&&f.value&&l(E,{ref:k,floating:!0,for:o.value},{default:()=>[r]})])])}),{controlRef:A}}});function ze(e){const y=Object.keys(ae.props).filter(a=>!ge(a)&&a!=="class"&&a!=="style");return ye(e,y)}const Ge=["color","file","time","date","datetime-local","week","month"],Je=N({autofocus:Boolean,counter:[Boolean,Number,String],counterValue:Function,prefix:String,placeholder:String,persistentPlaceholder:Boolean,persistentCounter:Boolean,suffix:String,type:{type:String,default:"text"},modelModifiers:Object,...Oe(),...ne()},"VTextField"),el=O()({name:"VTextField",directives:{Intersect:De},inheritAttrs:!1,props:Je(),emits:{"click:control":e=>!0,"mousedown:control":e=>!0,"update:focused":e=>!0,"update:modelValue":e=>!0},setup(e,y){let{attrs:a,emit:V,slots:t}=y;const b=be(e,"modelValue"),{isFocused:x,focus:j,blur:R}=te(e),T=u(()=>typeof e.counterValue=="function"?e.counterValue(b.value):(b.value??"").toString().length),L=u(()=>{if(a.maxlength)return a.maxlength;if(!(!e.counter||typeof e.counter!="number"&&typeof e.counter!="string"))return e.counter}),B=u(()=>["plain","underlined"].includes(e.variant));function H(n,d){var c,v;!e.autofocus||!n||(v=(c=d[0].target)==null?void 0:c.focus)==null||v.call(c)}const $=S(),C=S(),f=S(),W=u(()=>Ge.includes(e.type)||e.persistentPlaceholder||x.value||e.active);function o(){var n;f.value!==document.activeElement&&((n=f.value)==null||n.focus()),x.value||j()}function q(n){V("mousedown:control",n),n.target!==f.value&&(o(),n.preventDefault())}function p(n){o(),V("click:control",n)}function k(n){n.stopPropagation(),o(),Z(()=>{b.value=null,Ve(e["onClick:clear"],n)})}function A(n){var c;const d=n.target;if(b.value=d.value,(c=e.modelModifiers)!=null&&c.trim&&["text","search","password","tel","url"].includes(e.type)){const v=[d.selectionStart,d.selectionEnd];Z(()=>{d.selectionStart=v[0],d.selectionEnd=v[1]})}}return U(()=>{const n=!!(t.counter||e.counter||e.counterValue),d=!!(n||t.details),[c,v]=xe(a),[{modelValue:K,..._}]=ee.filterProps(e),[z]=ze(e);return l(ee,M({ref:$,modelValue:b.value,"onUpdate:modelValue":s=>b.value=s,class:["v-text-field",{"v-text-field--prefixed":e.prefix,"v-text-field--suffixed":e.suffix,"v-text-field--plain-underlined":["plain","underlined"].includes(e.variant)},e.class],style:e.style},c,_,{centerAffix:!B.value,focused:x.value}),{...t,default:s=>{let{id:i,isDisabled:m,isDirty:g,isReadonly:r,isValid:I}=s;return l(ae,M({ref:C,onMousedown:q,onClick:p,"onClick:clear":k,"onClick:prependInner":e["onClick:prependInner"],"onClick:appendInner":e["onClick:appendInner"],role:"textbox"},z,{id:i.value,active:W.value||g.value,dirty:g.value||e.dirty,disabled:m.value,focused:x.value,error:I.value===!1}),{...t,default:P=>{let{props:{class:h,...F}}=P;const D=X(l("input",M({ref:f,value:b.value,onInput:A,autofocus:e.autofocus,readonly:r.value,disabled:m.value,name:e.name,placeholder:e.placeholder,size:1,type:e.type,onFocus:o,onBlur:R},F,v),null),[[Ce("intersect"),{handler:H},null,{once:!0}]]);return l(w,null,[e.prefix&&l("span",{class:"v-text-field__prefix"},[l("span",{class:"v-text-field__prefix__text"},[e.prefix])]),l("div",{class:h,"data-no-activator":""},[t.default?l(w,null,[t.default(),D]):he(D)]),e.suffix&&l("span",{class:"v-text-field__suffix"},[l("span",{class:"v-text-field__suffix__text"},[e.suffix])])])}})},details:d?s=>{var i;return l(w,null,[(i=t.details)==null?void 0:i.call(t,s),n&&l(w,null,[l("span",null,null),l(He,{active:e.persistentCounter||x.value,value:T.value,max:L.value},t.counter)])])}:void 0})}),Ue({},$,C,f)}});export{el as V,Je as m};
