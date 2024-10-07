<template>
  <div>
    <button @click="linkGitHubAccount">Link GitHub Account</button>
  </div>
</template>

<script>
export default {
  methods: {
    linkGitHubAccount() {
      const clientId = 'Ov23liw6wJDuXjKKc8zO';
      const redirectUri = 'http://localhost:8000/api/github/callback';
      const scope = 'user,repo';
      const state = this.generateState();

      const authUrl = `https://github.com/login/oauth/authorize?client_id=${clientId}&redirect_uri=${encodeURIComponent(
        redirectUri
      )}&scope=${scope}&state=${state}`;

      window.location.href = authUrl;
    },
    generateState() {
      return Math.random().toString(36).substring(2);
    },
    mounted() {
      const urlParams = new URLSearchParams(window.location.search);
      const code = urlParams.get('code');

      if (code) {
        this.handleGitHubCallback(code);
      }
    },
    async handleGitHubCallback(code) {
      try {
        const response = await fetch('http://localhost:8000/api/github/link', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ code }),
        });

        if (response.ok) {
          const data = await response.json();
          console.log('Successfully linked GitHub:', data);
        } else {
          console.error('Error linking GitHub:', response.statusText);
        }
      } catch (error) {
        console.error('Error:', error);
      }
    },
  },
};
</script>
