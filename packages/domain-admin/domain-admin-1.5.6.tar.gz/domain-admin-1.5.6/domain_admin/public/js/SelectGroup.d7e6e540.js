import{aw as u,ah as a,o as s,O as r,P as i,c,a8 as d,F as h,L as g,al as _}from"./vendor-vue.9e61e0af.js";import{H as f,_ as O}from"./index.12198a8e.js";const S=u({id:"group-store",state:()=>({groupOptions:[]}),getters:{getGroupOptions:e=>e.groupOptions},actions:{setGroupOptions(e){this.groupOptions=e.map(t=>({...t,value:t.id,label:t.name}))},async updateGroupOptions(){const e=await f.getGroupList();e.code==0&&this.setGroupOptions(e.data.list)}}}),G={name:"SelectGroup",props:{showNotGroup:{type:Boolean,default:!1}},components:{},data(){return{groupOptions:[]}},computed:{options(){return this.showNotGroup?[...this.groupOptions,{value:0,label:"\u672A\u5206\u7EC4"}]:this.groupOptions}},methods:{async getData(){const e=await this.$http.getGroupList();e.ok&&(this.groupOptions=e.data.list.map(t=>(t.label=t.name,t.value=t.id,t.disabled=!t.has_edit_permission,t)))}},created(){this.getData()}};function b(e,t,m,v,w,n){const p=a("el-option"),l=a("el-select");return s(),r(l,g(e.$attrs,_(e.$events),{placeholder:"\u5206\u7EC4"}),{default:i(()=>[(s(!0),c(h,null,d(n.options,o=>(s(),r(p,{key:o.value,label:o.label,value:o.value,disabled:o.disabled},null,8,["label","value","disabled"]))),128))]),_:1},16)}const y=O(G,[["render",b]]);export{y as S,S as u};
