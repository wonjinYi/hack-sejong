<template>
  <div class="dashboard-view">
    <!-- 강의실 탭 -->
    <div class="rooms-menu">
      <div
        class="room-item"
        style="font-weight: 600; background-color: yellowgreen"
      >
        전체
      </div>
      <div class="room-item">강의실 1</div>
      <div class="room-item add-button">+</div>
    </div>

    <!-- 전력량 -->
    <div class="power-viewer">
      <div class="power-history-container">
        <PowerHistoryChart />
      </div>
      <div class="power-sum-container">
        <span>{{ `${powerSum} kWh` }}</span>
      </div>
    </div>

    <!-- 알림 -->
    <div class="notification-viewer">
      <div class="notification-item">알림 1</div>
      <div class="notification-item">알림 2</div>
      <div class="notification-item">알림 3</div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { helloWorld } from "@/api.js";

import PowerHistoryChart from "@/layouts/PowerHistoryChart.vue";

const powerSum = ref(0);

async function init() {
  await helloWorld();
}

init();
</script>

<style lang="scss" scoped>
.dashboard-view {
  display: flex;
  gap: 1rem;
  height: 100vh;
  width: 100vw;
  padding: 1rem;

  background-color: rgb(230, 230, 230);
}

.rooms-menu {
  display: flex;
  gap: 0.5rem;
  flex-direction: column;
  height: 100%;
  width: 128px;
  padding: 0.5rem;
  border-radius: 1rem;
  background-color: white;

  .room-item {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 50px;
    width: 100%;
    border-radius: 1rem;
    background-color: white;
    border: 1px solid gray;

    cursor: pointer;
    transition: all 0.2s;
    &:hover {
      filter: brightness(80%);
    }
  }
  .room-item.add-button {
  }
}

.power-viewer {
  flex: 1;
  padding: 2rem;
  border-radius: 1rem;
  background-color: white;

  // two container with same height
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  .power-history-container {
    height: 100%;
    width: 100%;

    //   padding: 2rem;
    //   border-radius: 1rem;
  }
  .power-sum-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 50px;
    width: 100%;
    background-color: white;
    border: 1px solid gray;
    border-top: none;
  }
}

.notification-viewer {
  width: 20vw;
  height: 100%;
  padding: 2rem;
  border-radius: 1rem;
  background-color: white;
}
</style>
