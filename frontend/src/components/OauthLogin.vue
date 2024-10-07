<template>
  <div>
    <button id="g_id_onload">Login with Google</button>
  </div>
</template>

<script>
import { useRouter } from 'vue-router';

export default {
  setup() {
    const router = useRouter();

    const loadGoogleSDK = () => {
      const script = document.createElement('script');
      script.src = 'https://accounts.google.com/gsi/client';
      script.async = true;
      script.defer = true;
      script.onload = () => {
        initializeGoogleSignIn();
      };
      document.head.appendChild(script);
    };

    const initializeGoogleSignIn = () => {
      window.google.accounts.id.initialize({
        client_id:
          '911758764582-2vfr2isc8q8h6h5m7udeh7ft93te9i3r.apps.googleusercontent.com',
        callback: handleCredentialResponse,
      });

      window.google.accounts.id.renderButton(
        document.getElementById('g_id_onload'),
        { theme: 'outline', size: 'large' }
      );
    };

    const handleCredentialResponse = async (response) => {
      try {
        const token = response.credential;

        const res = await fetch('http://localhost:8000/api/login/google/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            token: token,
          }),
        });

        if (res.status === 200) {
          router.push('/github');
        }
      } catch (error) {
        console.error('Login failed', error);
      }
    };

    if (typeof window.google !== 'undefined' && window.google.accounts) {
      initializeGoogleSignIn();
    } else {
      loadGoogleSDK();
    }
  },
};
</script>
