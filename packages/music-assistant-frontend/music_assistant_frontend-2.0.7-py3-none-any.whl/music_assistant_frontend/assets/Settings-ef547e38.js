import{l as m,a6 as d,c as v,Q as f,v as i,A as _,j as t,y as r,N as o,J as s,x as g,S as y}from"./index-8ef8125d.js";import{a as V,V as n}from"./VTabs-1b99b0fa.js";import{V as b}from"./VToolbar-b4c95f12.js";import"./VBtn-49774b84.js";import"./index-a4f9d82d.js";const x=m({__name:"Settings",setup(S){const l=d(),u=v(()=>{var e,a;return(e=l.currentRoute.value.name)!=null&&e.toString().includes("player")?"players":(a=l.currentRoute.value.name)!=null&&a.toString().includes("core")?"core":"providers"});return(e,a)=>{const p=f("router-view");return i(),_("div",null,[t(b,{variant:"flat",color:"transparent",style:{height:"50px"}},{title:r(()=>[t(V,{"model-value":u.value,color:"primary","align-tabs":"end"},{default:r(()=>[t(n,{value:"providers",to:{name:"providersettings"}},{default:r(()=>[o(s(e.$t("settings.providers")),1)]),_:1}),t(n,{value:"players",to:{name:"playersettings"}},{default:r(()=>[o(s(e.$t("settings.players")),1)]),_:1}),t(n,{value:"core",to:{name:"coresettings"}},{default:r(()=>[o(s(e.$t("settings.core")),1)]),_:1})]),_:1},8,["model-value"])]),_:1}),t(p,{app:""},{default:r(({Component:c})=>[(i(),g(y(c)))]),_:1})])}}});export{x as default};
