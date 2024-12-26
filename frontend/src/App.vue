<template>
  <router-view></router-view>
</template>

<script setup>
import { ref } from "vue";
</script>

<style lang="scss" scoped></style>

<!-- global style -->
<style lang="scss">
@import "@/assets/globalStyles/reset.css";
@import "@/assets/globalStyles/main.scss";
</style>

<!-- transition -->
<style lang="scss">
// loading backdrop transition
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

// tooptip
.fade-fast-enter-active,
.fade-fast-leave-active {
  transition: opacity 0.2s ease;
}

.fade-fast-enter-from,
.fade-fast-leave-to {
  opacity: 0;
}
</style>
