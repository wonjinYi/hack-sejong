<template>
  <div class="user-view">
    <input type="text" v-model="userId" />
    <button @click="submitUserId">인증 요청</button>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { postUser } from "@/api.js";
const userId = ref("");
function submitUserId() {
  //   console.log(userId.value);
  //   const res = await postUser(userId.value);
  //   console.log(res);

  setTimeout(() => {
    alert("인증 요청이 완료되었습니다.");
  }, 500);
}
</script>

<style lang="scss" scoped>
.user-view {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  input {
    margin-bottom: 20px;
    font-size: 2rem;
  }
  button {
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    background-color: #ec4899;
    color: white;
    cursor: pointer;
  }
}
</style>
