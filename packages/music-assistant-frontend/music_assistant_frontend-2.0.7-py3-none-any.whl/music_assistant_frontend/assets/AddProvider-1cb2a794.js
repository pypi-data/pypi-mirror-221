import{n as w}from"./index.browser-7e542916.js";import{l as M,a6 as N,r as g,o as S,H as t,ao as B,b as E,w as P,v as f,A as b,j as i,y as l,q as a,N as c,J as d,x as h,I as r,D as v}from"./index-8ef8125d.js";import{_ as T}from"./EditConfig.vue_vue_type_style_index_0_lang-74792501.js";import{c as $,b as _,V as j}from"./VCard-e81591ba.js";import{b as A,e as D}from"./VMenu-a805d6b6.js";import{x as I}from"./VBtn-49774b84.js";import"./VExpansionPanel-523a6df6.js";import"./VTextField-be284f64.js";import"./index-a4f9d82d.js";import"./VCheckboxBtn-4c08e900.js";import"./VListItem-b049d12d.js";import"./VSpacer-b8926de0.js";import"./VDialog-b35e6970.js";const U={key:0,style:{"margin-left":"-5px","margin-right":"-5px"}},H=r("br",null,null,-1),O=["href"],q=r("br",null,null,-1),z=r("br",null,null,-1),J=r("br",null,null,-1),ne=M({__name:"AddProvider",props:{domain:{}},setup(y){const u=y,V=N(),m=g([]),p=w(11),s=g(!1);S(()=>{const e=t.subscribe(B.AUTH_SESSION,o=>{if(o.object_id!==p)return;const n=o.data;window.open(n,"_blank").focus()});E(e)}),P(()=>u.domain,async e=>{e&&(m.value=await t.getProviderConfigEntries(u.domain,void 0,void 0,{session_id:p}))},{immediate:!0});const k=async function(e){s.value=!0,t.saveProviderConfig(u.domain,e).then(()=>{s.value=!1,V.push({name:"providersettings"})}).catch(o=>{alert(o),s.value=!1})},C=async function(e,o){s.value=!0;for(const n of m.value)n.value!==void 0&&o[n.key]==null&&(o[n.key]=n.value);o.session_id=p,t.getProviderConfigEntries(u.domain,void 0,e,o).then(n=>{m.value=n,s.value=!1}).catch(n=>{alert(n),s.value=!1})};return(e,o)=>(f(),b("section",null,[i(j,null,{default:l(()=>[a(t).providerManifests[e.domain]?(f(),b("div",U,[i($,null,{default:l(()=>[c(d(e.$t("settings.setup_provider",[a(t).providerManifests[e.domain].name])),1)]),_:1}),i(_,null,{default:l(()=>[c(d(a(t).providerManifests[e.domain].description),1)]),_:1}),H,a(t).providerManifests[e.domain].codeowners.length?(f(),h(_,{key:0},{default:l(()=>[r("b",null,d(e.$t("settings.codeowners"))+": ",1),c(d(a(t).providerManifests[e.domain].codeowners.join(" / ")),1)]),_:1})):v("",!0),a(t).providerManifests[e.domain].documentation?(f(),h(_,{key:1},{default:l(()=>[r("b",null,d(e.$t("settings.need_help_setup_provider")),1),c("  "),r("a",{href:a(t).providerManifests[e.domain].documentation,target:"_blank"},d(e.$t("settings.check_docs")),9,O)]),_:1})):v("",!0)])):v("",!0),q,i(A),z,J,i(T,{"config-entries":m.value,disabled:!1,onSubmit:k,onAction:C},null,8,["config-entries"])]),_:1}),i(D,{modelValue:s.value,"onUpdate:modelValue":o[0]||(o[0]=n=>s.value=n),scrim:"true",persistent:"",style:{display:"flex","align-items":"center","justify-content":"center"}},{default:l(()=>[i(I,{indeterminate:"",size:"64",color:"primary"})]),_:1},8,["modelValue"])]))}});export{ne as default};
