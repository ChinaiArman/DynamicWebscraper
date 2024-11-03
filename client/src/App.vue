<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <!-- <header>
    <div class="wrapper">

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header> -->

  <RouterView />
</template>

<style scoped>
/* Global styles */
:root {
  --color-background: #f8f9fa;
  --color-primary: #007bff;
  --color-text: #212529;
  --color-border: #dee2e6;
}

body {
  font-family: 'Arial', sans-serif;
  color: var(--color-text);
  background-color: var(--color-background);
  margin: 0;
  padding: 0;
}

/* Header styling */
header {
  background-color: var(--color-primary);
  color: #ffffff;
  padding: 1rem 0;
}

.wrapper {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 1.5rem;
}

.logo h1 {
  font-size: 1.5rem;
  font-weight: bold;
  margin: 0;
}

nav {
  display: flex;
  gap: 1rem;
}

nav a {
  color: #ffffff;
  font-size: 1rem;
  text-decoration: none;
  padding: 0.5rem 1rem;
  transition: background-color 0.3s ease;
}

nav a:hover {
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 5px;
}

nav a.router-link-exact-active {
  background-color: rgba(255, 255, 255, 0.3);
  font-weight: bold;
  border-radius: 5px;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .wrapper {
    flex-direction: column;
    align-items: flex-start;
  }

  nav {
    flex-direction: column;
    width: 100%;
    margin-top: 1rem;
  }

  nav a {
    padding: 0.5rem;
    text-align: left;
    width: 100%;
  }
}
</style>
