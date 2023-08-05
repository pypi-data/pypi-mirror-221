import{_ as v,f}from"./ItemsListing.vue_vue_type_style_index_0_lang-8e142c2f.js";import{_ as g,a as I}from"./ProviderDetails.vue_vue_type_script_setup_true_lang-86038b27.js";import{l as T,r as u,c as V,aq as m,w as D,o as A,H as o,ao as M,b as B,v as n,A as E,j as $,x as c,D as d,I as b}from"./index-8ef8125d.js";import"./ListviewItem-ade956db.js";import"./MediaItemThumb.vue_vue_type_style_index_0_lang-3622812c.js";import"./ListItem-bba986fb.js";import"./VBtn-49774b84.js";import"./VMenu-a805d6b6.js";import"./index-a4f9d82d.js";import"./VListItem-b049d12d.js";import"./VCheckboxBtn-4c08e900.js";import"./VCard-e81591ba.js";/* empty css                             */import"./PanelviewItem.vue_vue_type_style_index_0_lang-a068cbe2.js";import"./contextmenu-7e32a8e5.js";import"./eventbus-d154090d.js";import"./Alert-bdc4de4a.js";import"./Container-32d4da6e.js";/* empty css              */import"./VToolbar-b4c95f12.js";import"./VTextField-be284f64.js";import"./VBadge-8b6f3afa.js";import"./VRow-08fca7f1.js";import"./layout-2c008654.js";import"./VDialog-b35e6970.js";const F=b("br",null,null,-1),N=b("br",null,null,-1),oe=T({__name:"TrackDetails",props:{itemId:{},provider:{},album:{}},setup(k){const a=k,_=u(""),s=u(!1),r=u(),h=V(()=>{var t;if(((t=r.value)==null?void 0:t.provider)!=="library")return[];const e=["library"];for(const i of m(r.value))e.push(i.provider_instance);return e}),p=async function(){console.log("props",a),r.value=await o.getTrack(a.itemId,a.provider,a.album),_.value="versions"};D(()=>a.itemId,e=>{e&&p()},{immediate:!0}),A(()=>{const e=o.subscribe(M.MEDIA_ITEM_ADDED,t=>{var l;const i=t.data;((l=r.value)==null?void 0:l.uri)==i.uri&&(s.value=!0)});B(e)});const y=async function(e){const t=[];if(e.refresh&&(await p(),s.value=!1),a.provider=="library"){const i=await o.getTrackVersions(a.itemId,a.provider);t.push(...i)}for(const i of m(r.value)){const l=await o.getTrackVersions(i.item_id,i.provider_instance);t.push(...l)}return f(t,e)},w=async function(e){let t=[];if(e.refresh&&(await p(),s.value=!1),!r.value)t=[];else if(e.providerFilter&&e.providerFilter!="library"){for(const i of m(r.value))if(i.provider_instance==e.providerFilter){t=await o.getTrackAlbums(i.item_id,i.provider_instance);break}}else t=await o.getTrackAlbums(r.value.item_id,r.value.provider);return f(t,e)};return(e,t)=>(n(),E("section",null,[$(g,{item:r.value,"active-provider":e.provider},null,8,["item","active-provider"]),r.value?(n(),c(v,{key:0,itemtype:"trackalbums","parent-item":r.value,"show-provider":!0,"show-favorites-only-filter":!1,"show-library":!0,"show-track-number":!1,"load-data":w,"sort-keys":["provider","sort_name","duration"],"update-available":s.value,title:e.$t("appears_on"),checksum:e.provider+e.itemId,"provider-filter":h.value},null,8,["parent-item","update-available","title","checksum","provider-filter"])):d("",!0),F,r.value?(n(),c(v,{key:1,itemtype:"trackversions","parent-item":r.value,"show-provider":!0,"show-favorites-only-filter":!1,"show-library":!0,"show-track-number":!1,"load-data":y,"sort-keys":["provider","sort_name","duration"],"update-available":s.value,title:e.$t("other_versions"),"hide-on-empty":!0,checksum:e.provider+e.itemId},null,8,["parent-item","update-available","title","checksum"])):d("",!0),N,r.value?(n(),c(I,{key:2,"item-details":r.value},null,8,["item-details"])):d("",!0)]))}});export{oe as default};
