<template>
  <div>
    <mobile-view />
    <div class="d-flex flex-column flex-root">
      <div class="d-flex flex-row flex-column-fluid page">
        <menu-view />
        <!--begin::Wrapper-->
        <div class="d-flex flex-column flex-row-fluid wrapper" id="kt_wrapper">
          <tool-bar />
          <router-view v-slot="{ Component, route }">
            <transition :name="route.meta.transition || 'fade'">
              <component :is="Component" />
            </transition>
          </router-view>
          <footer-view />
        </div>
      </div>
    </div>
    <quick-notifications />
    <quick-actions />
    <quick-panel />
    <quick-user />
  </div>
</template>

<script src="./layout.ts"></script>
