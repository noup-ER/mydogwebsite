<template>
  <div>
    <titlebar></titlebar>
    <searchbar></searchbar>
    <navbar></navbar>
  </div>
</template>

<script>
export default {
  name: "APP",
  components:{
    titlebar:()=>import("titlebar/App"),
    searchbar:()=>import("searchbar/App"),
    navbar:()=>import("navbar/App"),
  }
}
</script>

<style scoped>

</style>