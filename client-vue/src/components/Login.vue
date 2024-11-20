<!-- <template>
  <div class="login">
    <h2>Login</h2>
    <form @submit.prevent="loginUser">
      <input type="email" v-model="email" placeholder="Email" required />
      <br>
      <input type="password" v-model="password" placeholder="Password" required />
      <br>
      <button type="submit">Login</button>
    </form>
    <p>{{ message }}</p>
    <router-link to="/register">Don't have an account? Register</router-link>
    <router-link to="/reset-password">Forgot Password?</router-link>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
      message: '',
    };
  },
  methods: {
    async loginUser() {
      try {
        const response = await axios.post('/api/authenticate/login/', {
          email: this.email,
          password: this.password,
        });
        this.message = response.data.message;
        // Redirect or handle login success
      } catch (error) {
        this.message = error.response.data.error || 'Login failed.';
      }
    },
  },
};
</script>

<style scoped>
/* Add your styles here */
</style> -->
<template>
  <div class="login">
    <h2>Login</h2>
    <form @submit.prevent="loginUser">
      <input type="email" v-model="email" placeholder="Email" required />
      <br />
      <input type="password" v-model="password" placeholder="Password" required />
      <br />
      <button type="submit">Login</button>
    </form>
    <p>{{ message }}</p>
    <router-link to="/register">Don't have an account? Register</router-link>
    <router-link to="/reset-password">Forgot Password?</router-link>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
      message: '',
    };
  },
  methods: {
    async loginUser() {
      try {
        const response = await axios.post(`${import.meta.env.VITE_SERVER_URL}/api/authenticate/login/`, {
          email: this.email,
          password: this.password,
        }, {
          withCredentials: true,
        });
        this.message = response.data.message;
        // Handle successful login, e.g., redirect or update user state
        if (response.status === 200) {
          const userInfoResponse = await axios.get(`${import.meta.env.VITE_SERVER_URL}/api/database/get-user-information/`, { withCredentials: true });
          const isAdmin = userInfoResponse.data.is_admin;
          if (isAdmin) {
            this.$router.push('/admin');
          } else {
            this.$router.push('/landing');
          }
        };
      } catch (error) {
        this.message = error.response.data.error || 'Login failed.';
      }
    },
  },
};
</script>

<style scoped>
/* Add your styles here */
</style>
