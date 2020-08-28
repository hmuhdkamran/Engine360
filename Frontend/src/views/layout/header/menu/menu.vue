<template>
  <!-- Main Sidebar Container -->
  <aside class="main-sidebar elevation-4 sidebar-light-navy">
    <!-- Brand Logo -->
    <a href="#" class="brand-link navbar-light">
      <img
        src="@/assets/logo.png"
        alt="AdminLTE Logo"
        class="brand-image img-circle elevation-3"
        style="opacity: .8"
      />
      <span class="brand-text font-weight-light">Million Mart</span>
    </a>

    <!-- Sidebar -->
    <div class="sidebar" style="overflow-y:overlay;">
      <!-- Sidebar user panel (optional) -->
      <div class="user-panel mt-3 pb-3 mb-3 d-flex">
        <div class="image">
          <img src="@/assets/logo.png" class="img-circle elevation-2" alt="User Image" />
        </div>
        <div class="info">
          <a href="#" class="d-block">Muhammad Kamran</a>
        </div>
      </div>

      <!-- Sidebar Menu -->
      <nav class="mt-2">
        <ul
          class="nav nav-pills nav-sidebar flex-column nav-compact"
          data-widget="treeview"
          role="menu"
          data-accordion="false"
        >
          <menu-item v-for="link in menuRepo" :userMenu="link" :key="link.name" />
        </ul>
      </nav>
      <!-- /.sidebar-menu -->
    </div>
    <!-- /.sidebar -->
  </aside>
</template>

<script src="./menu.ts"></script>