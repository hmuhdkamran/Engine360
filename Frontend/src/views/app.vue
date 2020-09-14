<template>
  <div style="height: 100%;">
    <loader v-show="isLoading" />
    <router-view />
  </div>
</template>

<script src="./app.ts"></script>

<style lang="scss">
@import "@/assets/scss/index.scss";
</style>
