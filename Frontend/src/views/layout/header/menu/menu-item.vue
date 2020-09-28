<template>
  <!-- <li v-if="hasChildrens">
    <a
      href="javascript:;"
      :class="{ 'menu-toggle': isOpened }"
      @click="isOpened = !isOpened"
    >
      <span class="icon is-small">
        <i :class="userMenu.icon"></i>
      </span>
      <span>{{ userMenu.name }}</span>
      <span class="icon is-small is-angle">
        <i class="fa fa-angle-down"></i>
      </span>
    </a>
    <div
      v-if="isOpened"
      class="menu-subcontainer"
      :style="{ height: userMenu.children.length * 30 + 10 + 'px' }"
    >
      <ul>
        <menu-item
          v-for="link in userMenu.children"
          :userMenu="link"
          :key="link.name"
        />
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
  </li> -->

  <li
    class="menu-item menu-item-submenu"
    aria-haspopup="true"
    data-menu-toggle="hover"
    v-if="hasChildrens"
  >
    <a href="javascript:;" class="menu-link menu-toggle">
      <span class="svg-icon menu-icon" v-html="userMenu.icon"> </span>
      <span class="menu-text">{{ userMenu.name }}</span>
      <i class="menu-arrow"></i>
    </a>
    <div class="menu-submenu">
      <i class="menu-arrow"></i>
      <ul class="menu-subnav">
        <li class="menu-item menu-item-parent" aria-haspopup="true">
          <span class="menu-link">
            <span class="menu-text">{{ userMenu.name }}</span>
          </span>
        </li>
        <menu-item
          v-for="link in userMenu.children"
          :userMenu="link"
          :key="link.name"
        />
      </ul>
    </div>
  </li>
  <li class="menu-item" aria-haspopup="true" v-else>
    <router-link
      :to="userMenu.route"
      class="menu-link"
      v-if="userMenu.isVisable"
    >
      <i class="menu-bullet menu-bullet-dot"> <span></span> </i>
      <span class="menu-text">{{ userMenu.name }}</span>
    </router-link>
  </li>
</template>

<script src="./menu-item.ts"></script>