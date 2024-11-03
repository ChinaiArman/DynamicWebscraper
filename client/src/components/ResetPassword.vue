<template>
  <div class="reset-password">
    <h2>Reset Password</h2>
    <form @submit.prevent="resetPassword">
      <input type="email" v-model="email" placeholder="Email" required />
      <br>
      <input type="text" v-model="resetCode" placeholder="Reset Code" required />
      <br>
      <input type="password" v-model="newPassword" placeholder="New Password" required />
      <br>
      <button type="submit">Reset Password</button>
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
      resetCode: '',
      newPassword: '',
      message: '',
    };
  },
  methods: {
    async resetPassword() {
      try {
        const response = await axios.post('/api/authenticate/reset-password/', {
          email: this.email,
          reset_code: this.resetCode,
          password: this.newPassword,
        });
        this.message = response.data.message;
        // Redirect or handle reset password success
      } catch (error) {
        this.message = error.response.data.error || 'Reset password failed.';
      }
    },
  },
};
</script>

<style scoped>
/* Add your styles here */
</style>
