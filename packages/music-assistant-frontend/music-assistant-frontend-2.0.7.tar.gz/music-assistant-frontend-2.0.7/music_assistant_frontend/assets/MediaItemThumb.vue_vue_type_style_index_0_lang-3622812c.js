import{l as I,c as k,E as D,H as d,v as h,x as b,y as o,k as J,I as l,J as u,D as R,j as g,N as f,q as B,Y as p,A as w,aD as m,r as C,ac as y,w as H,aj as v}from"./index-8ef8125d.js";import{_ as O}from"./ListItem-bba986fb.js";import{V as M}from"./VCheckboxBtn-4c08e900.js";import{V as Y,b as N,c as E}from"./VMenu-a805d6b6.js";import{V as S,c as X}from"./VListItem-b049d12d.js";import{a as U}from"./VCard-e81591ba.js";import{x as L,l as P}from"./VBtn-49774b84.js";const T=""+new URL("crossfade-ba51f69a.png",import.meta.url).href,Z="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAABmJLR0QAAAAAAAD5Q7t/AAAACXBIWXMAAABgAAAAYADwa0LPAAAAnElEQVRYw+2UwQ6AMAhDwfjh+OXzZrgslqxjW8K7GWdtRqlIUYyh/qG1Zt8LVYuKzTDUnCGNy41zrfhpGRrhZgn5/HmiWdzuhsrQH7QMicjDENmuGKEbQjaotiwLaGSZeUIzZB2jhnwfAdqyzFAze+gXxPSZxcgaB6JDa+rUDLG2DNFJ3TLkzDlN3bveGWc83ZFlctTIKOVWFCt5AYSDaENMYFhMAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIyLTA0LTE1VDEzOjExOjE0KzAwOjAwADepDgAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMi0wNC0xNVQxMzoxMToxNCswMDowMHFqEbIAAAAASUVORK5CYII=",x={class:"d-flex justify-center",style:{width:"100%"}},G={style:{height:"50px",display:"flex","align-items":"center"}},K={style:{height:"50px",display:"flex","align-items":"center"}},V=["src"],Q={key:0,style:{height:"50px",display:"flex","align-items":"center"}},j={key:1,style:{height:"50px",display:"flex","align-items":"center"}},W=new URL(""+new URL("logo-c9d5d6ab.png",import.meta.url).href,self.location).href,q=new URL("data:image/png;base64,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",self.location).href,_=new URL("data:image/png;base64,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",self.location).href,z=new URL("data:image/png;base64,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",self.location).href,$=new URL("data:image/png;base64,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",self.location).href;new URL("data:image/png;base64,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",self.location).href;const ee=new URL(""+new URL("m4a-45331b05.png",import.meta.url).href,self.location).href,me=new URL(""+new URL("hires-438c7046.png",import.meta.url).href,self.location).href,te=new URL(""+new URL("cover_dark-75402cd0.png",import.meta.url).href,self.location).href,Ae=new URL(""+new URL("cover_light-b832ae9e.png",import.meta.url).href,self.location).href,fe=I({__name:"QualityDetailsBtn",setup(e){const t=k(()=>{if(D.selectedPlayer)return d.queues[D.selectedPlayer.active_source]}),a=k(()=>{var A,s;return(s=(A=t.value)==null?void 0:A.current_item)==null?void 0:s.streamdetails}),i=function(A){return A==m.AAC?q:A==m.FLAC?_:A==m.MP3||A==m.MPEG?z:A==m.OGG?$:A==m.M4A?ee:W};return(A,s)=>a.value?(h(),b(E,{key:0,location:"bottom end","close-on-content-click":!1},{activator:o(({props:r})=>{var n,c;return[a.value?(h(),b(M,J({key:0,disabled:!t.value||!((n=t.value)!=null&&n.active)||((c=t.value)==null?void 0:c.items)==0,class:"mediadetails-content-type-btn",label:"",ripple:!1},r),{default:o(()=>[l("div",x,u(a.value.audio_format.content_type.toUpperCase()),1)]),_:2},1040,["disabled"])):R("",!0)]}),default:o(()=>[g(U,{class:"mx-auto",width:"300"},{default:o(()=>[g(Y,{style:{overflow:"hidden"}},{default:o(()=>{var r,n;return[g(S,{class:"list-item list-item-main","min-height":5},{default:o(()=>[g(X,{class:"text-h5 mb-1"},{default:o(()=>[f(u(A.$t("stream_details")),1)]),_:1})]),_:1}),g(N),l("div",G,[g(O,{domain:a.value.provider,size:35,style:{"object-fit":"contain","margin-left":"10px","margin-right":"5px"}},null,8,["domain"]),f(" "+u(((r=B(d).providerManifests[a.value.provider])==null?void 0:r.name)||((n=B(d).providers[a.value.provider])==null?void 0:n.name)),1)]),l("div",K,[l("img",{height:"30",width:"50",src:i(a.value.audio_format.content_type),style:p(A.$vuetify.theme.current.dark?"object-fit: contain;":"object-fit: contain;filter: invert(100%);")},null,12,V),f(" "+u(a.value.audio_format.sample_rate/1e3)+" kHz / "+u(a.value.audio_format.bit_depth)+" bits ",1)]),t.value&&t.value.crossfade_enabled?(h(),w("div",Q,[l("img",{height:"30",width:"50",contain:"",src:T,style:p(A.$vuetify.theme.current.dark?"object-fit: contain;":"object-fit: contain;filter: invert(100%);")},null,4),f(" "+u(A.$t("crossfade_enabled")),1)])):R("",!0),a.value.gain_correct?(h(),w("div",j,[l("img",{height:"30",width:"50",contain:"",src:Z,style:p(A.$vuetify.theme.current.dark?"object-fit: contain;":"object-fit: contain;filter: invert(100%);")},null,4),f(" "+u(a.value.gain_correct)+" dB ",1)])):R("",!0)]}),_:1})]),_:1})]),_:1})):R("",!0)}});const ie={class:"d-flex align-center justify-center fill-height"},ae=function(e,t=v.THUMB,a=!1){if(e){if("image"in e&&e.image)return e.image;if("metadata"in e&&e.metadata.images){for(const i of e.metadata.images)if(!(i.provider=="http"&&!a)&&i.type==t)return i}if("album"in e&&e.album&&"metadata"in e.album&&e.album.metadata&&e.album.metadata.images){for(const i of e.album.metadata.images)if(!(i.provider=="http"&&!a)&&i.type==t)return i}if("artist"in e&&"metadata"in e.artist&&e.artist.metadata&&e.artist.metadata.images){for(const i of e.artist.metadata.images)if(!(i.provider=="http"&&!a)&&i.type==t)return i}if("artists"in e&&e.artists){for(const i of e.artists)if("metadata"in i&&i.metadata.images){for(const A of i.metadata.images)if(!(A.provider=="http"&&!a)&&A.type==t)return A}}}},re=function(e,t=v.THUMB,a){var s,r;if(!e)return;let i="";const A=ae(e,t,!0);if(A){if(A.provider!=="url"){if(!((s=d.providers[A.provider])!=null&&s.available))return;const n=encodeURIComponent(encodeURIComponent(A.path)),c="metadata"in e?(r=e.metadata)==null?void 0:r.checksum:"";i=`${d.baseUrl}/imageproxy?path=${n}&provider=${A.provider}&checksum=${c}`}else i=A.path;return a?i.includes("imageproxy")?i+`&size=${a}`:`https://images.weserv.nl/?url=${i}&w=${a}&h=${a}&fit=cover&a=attention`:i}},he=I({__name:"MediaItemThumb",props:{item:{},width:{default:"100%"},height:{default:"auto"},size:{},aspectRatio:{default:"1/1"},cover:{type:Boolean,default:!0},fallback:{default:void 0},thumb:{type:Boolean,default:!0},lazySrc:{},rounded:{type:Boolean,default:!0}},setup(e){const t=e,a=C(),i=y(),A=k(()=>t.fallback?t.fallback:t.item?i.current.value.dark?`https://ui-avatars.com/api/?name=${t.item.name}&size=${s.value||256}&bold=true&background=1d1d1d&color=383838`:`https://ui-avatars.com/api/?name=${t.item.name}&size=${s.value||256}&bold=true&background=a0a0a0&color=cccccc`:""),s=k(()=>typeof t.size=="number"?t.size:typeof t.width=="number"&&typeof t.height=="number"?t.height>t.width?t.height:t.width:t.thumb?256:0);return H(()=>t.item,async r=>{r&&(a.value=re(r,v.THUMB,s.value)||A.value)},{immediate:!0}),(r,n)=>{var c,F;return h(),b(P,{key:"uri"in r.item?(c=r.item)==null?void 0:c.uri:(F=r.item)==null?void 0:F.queue_item_id,style:p(`height:${r.size||r.height}px; width:${r.size||r.width}px; ${r.rounded?"border-radius: 4px;":""}`),cover:r.cover,src:a.value,"aspect-ratio":r.aspectRatio,"lazy-src":r.lazySrc?r.lazySrc:r.$vuetify.theme.current.dark?B(te):B(Ae),onError:n[0]||(n[0]=()=>{a.value=A.value})},{placeholder:o(()=>[l("div",ie,[g(L,{indeterminate:""})])]),_:1},8,["style","cover","src","aspect-ratio","lazy-src"])}}});export{he as _,Ae as a,fe as b,W as c,me as d,re as g,te as i};
