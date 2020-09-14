<template>
  <!--begin::Main-->
  <div class="d-flex flex-column flex-root" style="height: 100%;">
    <!--begin::Login-->
    <div class="login login-5 wizard d-flex flex-column flex-lg-row flex-column-fluid">
      <!--begin::Aside-->
      <div class="login-aside d-flex flex-column flex-row-auto">
        <!--begin::Aside Top-->
        <div class="d-flex flex-column-auto flex-column pt-lg-40 pt-15">
          <!--begin::Aside header-->
          <a href="#" class="login-logo text-center pt-lg-25 pb-10">
            <img src="@/assets/logo.png" class="max-h-70px" alt="" />
          </a>
          <!--end::Aside header-->
          <!--begin::Aside Title-->
          <h3 class="font-weight-bolder text-center font-size-h4 text-dark-50">User Experience &amp; Interface Design
          <br />Strategy SaaS Solutions</h3>
          <!--end::Aside Title-->
        </div>
        <!--end::Aside Top-->
        <!--begin::Aside Bottom-->
        <div class="aside-img d-flex flex-row-fluid bgi-no-repeat bgi-position-x-center" style="background-position-y: calc(100% + 1rem); background-image: url(img/svg/login-visual.svg)"></div>
        <!--end::Aside Bottom-->
      </div>
      <!--begin::Aside-->
      <!--begin::Content-->
      <div class="login-content flex-row-fluid d-flex flex-column p-10">
        <!--begin::Wrapper-->
        <div class="d-flex flex-row-fluid flex-center">
          <router-view />
        </div>
        <!--end::Wrapper-->
      </div>
      <!--end::Content-->
    </div>
    <!--end::Login-->
  </div>
  <!--end::Main-->
</template>

<script src="./layout.ts"></script>

<style lang="scss" scoped>
  @import "@/assets/scss/index.scss";
  @import "@/assets/scss/pages/login/login-5.scss";
</style>