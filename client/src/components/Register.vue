<template>
  <div class="register">
    <h2>Register</h2>
    <form @submit.prevent="registerUser">
      <input type="text" v-model="name" placeholder="Name" required />
      <br>
      <input type="email" v-model="email" placeholder="Email" required />
      <br>
      <input type="password" v-model="password" placeholder="Password" required />
      <br>
      <button type="submit">Register</button>
    </form>
    <p>{{ message }}</p>
    <router-link to="/login">Already have an account? Login</router-link>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      email: '',
      password: '',
      message: '',
    };
  },
  methods: {
    async registerUser() {
      try {
        const response = await axios.post('/api/authenticate/register/', {
          name: this.name,
          email: this.email,
          password: this.password,
        });
        this.message = response.data.message;
        // Redirect or handle registration success
      } catch (error) {
        this.message = error.response.data.error || 'Registration failed.';
      }
    },
  },
};
</script>

<style scoped>
/* Add your styles here */
</style>
