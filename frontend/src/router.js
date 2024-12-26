import { createRouter, createWebHistory } from "vue-router";

// 뷰 불러오기 ------------------------------------
// 공통 뷰
import NotFoundView from "@/views/NotFoundView.vue";
import LandingView from "@/views/LandingView.vue";
import DashboardView from "@/views/DashboardView.vue";
import UserView from "@/views/UserView.vue";

// 라우터 설정 ------------------------------------
const routes = [
  // 공통 뷰
  {
    path: "/:pathMatch(.*)*",
    name: "NotFound",
    component: NotFoundView,
  },
  {
    path: "/",
    name: "Landing",
    component: LandingView,
  },
  ,
  {
    path: "/dashboard",
    name: "Dashboard",
    component: DashboardView,
  },
  ,
  {
    path: "/user",
    name: "User",
    component: UserView,
  },
];

// 라우터 객체 생성
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
