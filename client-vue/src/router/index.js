import { createRouter, createWebHistory } from "vue-router";
import LoginView from "../views/LoginView.vue";
import RegisterView from "../views/RegisterView.vue";
import ResetPasswordView from "../views/ResetPasswordView.vue"; // Assuming you have this view
import Admin from "../components/Admin.vue";
import Landing from "../components/Landing.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "login",
      component: LoginView,
    },
    {
      path: "/register",
      name: "register",
      component: RegisterView,
    },
    {
      path: "/reset-password",
      name: "reset-password",
      component: ResetPasswordView,
    },
    {
      path: "/about",
      name: "about",
      component: () => import("../views/AboutView.vue"),
    },
    {
      path: "/admin",
      name: "admin",
      component: Admin,
    },
    {
      path: "/landing",
      name: "landing",
      component: Landing,
    }
  ],
});

export default router;
