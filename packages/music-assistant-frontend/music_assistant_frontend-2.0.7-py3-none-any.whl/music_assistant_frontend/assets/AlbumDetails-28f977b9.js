import{_ as v,f as c}from"./ItemsListing.vue_vue_type_style_index_0_lang-8e142c2f.js";import{_ as w,a as A}from"./ProviderDetails.vue_vue_type_script_setup_true_lang-86038b27.js";import{l as g,r as f,c as I,aq as p,w as V,o as D,H as s,ao as M,b as B,v as n,A as E,j as T,x as m,D as d,I as b}from"./index-8ef8125d.js";import"./ListviewItem-ade956db.js";import"./MediaItemThumb.vue_vue_type_style_index_0_lang-3622812c.js";import"./ListItem-bba986fb.js";import"./VBtn-49774b84.js";import"./VMenu-a805d6b6.js";import"./index-a4f9d82d.js";import"./VListItem-b049d12d.js";import"./VCheckboxBtn-4c08e900.js";import"./VCard-e81591ba.js";/* empty css                             */import"./PanelviewItem.vue_vue_type_style_index_0_lang-a068cbe2.js";import"./contextmenu-7e32a8e5.js";import"./eventbus-d154090d.js";import"./Alert-bdc4de4a.js";import"./Container-32d4da6e.js";/* empty css              */import"./VToolbar-b4c95f12.js";import"./VTextField-be284f64.js";import"./VBadge-8b6f3afa.js";import"./VRow-08fca7f1.js";import"./layout-2c008654.js";import"./VDialog-b35e6970.js";const $=b("br",null,null,-1),F=b("br",null,null,-1),ae=g({__name:"AlbumDetails",props:{itemId:{},provider:{},forceProviderVersion:{}},setup(_){const a=_,o=f(!1),t=f(),y=I(()=>{var r;if(((r=t.value)==null?void 0:r.provider)!=="library")return[];const e=["library"];for(const i of p(t.value))e.push(i.provider_instance);return e}),u=async function(){t.value=await s.getAlbum(a.itemId,a.provider)};V(()=>a.itemId,e=>{e&&u()},{immediate:!0}),D(()=>{const e=s.subscribe(M.MEDIA_ITEM_ADDED,r=>{var l;const i=r.data;((l=t.value)==null?void 0:l.uri)==i.uri&&(o.value=!0)});B(e)});const h=async function(e){let r=[];if(e.refresh&&(await u(),o.value=!1),!t.value)r=[];else if(e.providerFilter&&e.providerFilter!="library"){for(const i of p(t.value))if(i.provider_instance==e.providerFilter){r=await s.getAlbumTracks(i.item_id,i.provider_instance);break}}else r=await s.getAlbumTracks(t.value.item_id,t.value.provider);return o.value=!1,c(r,e)},k=async function(e){const r=[];if(e.refresh&&(await u(),o.value=!1),a.provider=="library"){const i=await s.getAlbumVersions(a.itemId,a.provider);r.push(...i)}for(const i of p(t.value)){const l=await s.getAlbumVersions(i.item_id,i.provider_instance);r.push(...l)}return c(r,e)};return(e,r)=>(n(),E("section",null,[T(w,{item:t.value,"active-provider":e.provider},null,8,["item","active-provider"]),t.value?(n(),m(v,{key:0,itemtype:"albumtracks","parent-item":t.value,"show-provider":!1,"show-favorites-only-filter":!1,"load-data":h,"sort-keys":["track_number","sort_name","duration"],"update-available":o.value,title:e.$t("tracks"),"provider-filter":y.value},null,8,["parent-item","update-available","title","provider-filter"])):d("",!0),$,t.value?(n(),m(v,{key:1,itemtype:"albumversions","parent-item":t.value,"show-provider":!0,"show-favorites-only-filter":!1,"load-data":k,"sort-keys":["provider","sort_name","year"],"update-available":o.value,title:e.$t("other_versions"),"hide-on-empty":!0},null,8,["parent-item","update-available","title"])):d("",!0),F,t.value?(n(),m(A,{key:2,"item-details":t.value},null,8,["item-details"])):d("",!0)]))}});export{ae as default};
