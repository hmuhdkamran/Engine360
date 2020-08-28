<template>
  <li :class="isOpened === true ? 'nav-item menu-open' : 'nav-item'" v-if="hasChildrens">
    <a href="javascript:;" class="nav-link" @click="isOpened = !isOpened">
      <i :class="'nav-icon ' + userMenu.icon"></i>
      <p>
        {{userMenu.name}}
        <i class="right fas fa-angle-left"></i>
      </p>
    </a>
    <ul class="nav nav-treeview" :style="isOpened === true ? 'display: block;' : 'display: none;'">
      <menu-item v-for="link in userMenu.children" :userMenu="link" :key="link.name" />
    </ul>
  </li>
  <li class="nav-item" v-else>
    <router-link :to="userMenu.route" class="nav-link" v-if="userMenu.isVisable">
      <i class="far fa-circle nav-icon"></i>
      <p>{{userMenu.name}}</p>
    </router-link>
  </li>
</template>

<script src="./menu-item.ts"></script>