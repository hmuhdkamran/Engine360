<template>
  <li v-if="hasChildrens">
    <a href="javascript:;" :class="{'menu-toggle':isOpened}" @click="isOpened = !isOpened">
      <span class="icon is-small">
        <i :class="userMenu.icon"></i>
      </span>
      <span>{{userMenu.name}}</span>
      <span class="icon is-small is-angle">
        <i class="fa fa-angle-down"></i>
      </span>
    </a>
    <div
      v-if="isOpened"
      class="menu-subcontainer"
      :style="{height: (userMenu.children.length * 30 + 10) + 'px'}"
    >
      <ul>
        <menu-item v-for="link in userMenu.children" :userMenu="link" :key="link.name" />
      </ul>
    </div>
  </li>
  <li class="nav-item" v-else>
    <router-link :to="userMenu.route" v-if="userMenu.isVisable">
      <span class="icon is-small">
        <i :class="userMenu.icon"></i>
      </span>
      <span v-text="userMenu.name"></span>
    </router-link>
  </li>
</template>

<script src="./menu-item.ts"></script>