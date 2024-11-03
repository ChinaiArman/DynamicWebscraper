<template>
  <div class="reset-password">
    <h2>Forgot Password</h2>
    <form @submit.prevent="sendResetEmail">
      <input type="email" v-model="email" placeholder="Enter your email" required />
      <br>
      <button type="submit">Send Reset Code</button>
    </form>
    <p>{{ message }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      message: '',
    };
  },
  methods: {
    async sendResetEmail() {
      try {
        const response = await axios.post('http://localhost:5000/api/authenticate/send-reset-code/', {
          email: this.email,
        });
        this.message = response.data.message;
        // Optionally, redirect to the page where user can enter the reset code and new password
      } catch (error) {
        this.message = error.response?.data?.error || 'Failed to send reset code.';
      }
    },
  },
};
</script>

<style scoped>
/* Add your styles here */
</style>
