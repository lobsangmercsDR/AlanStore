<template>
    <div>
      <navbar-component></navbar-component>
      <main class="bg-gray-300">
        <section class="container mx-auto px-4">
          <div class="flex justify-center mt-10">
            <div class="w-full lg:w-4/12 px-4 logoutContainer">
              <div style="background: white;" class=" relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-gray-300 border-0">
                <div class="rounded-t mb-0 px-6 py-6">
                  <div class="text-center mb-3">
                    <h6 class="text-gray-600 text-sm font-bold">Sign out</h6>
                  </div>
                  <hr class="mt-6 border-b-1 border-gray-400" />
                </div>
                <div class="flex-auto px-4 lg:px-10 py-10 pt-0">
                  <div class="text-gray-500 text-center mb-3 font-bold">
                    <p>¿Está seguro de que desea salir?</p>
                  </div>
                  
                  <div class="text-center">
                    <button
                      class="bg-gray-900 text-white active:bg-gray-700 text-sm font-bold uppercase px-4 py-2 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1"
                      type="button"
                      @click="logout"
                      style="transition: all 0.15s ease 0s;"
                    >
                      Sign Out
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>
      <footer-component></footer-component>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import Cookies from 'js-cookie';
  
  export default {
    methods: {
      async logout() {
        try {
          await axios.get("http://127.0.0.1:8000/api/users/logout", {
            headers: {
              Authorization: `Token ${Cookies.get('token')}`,
            },
          });
          Cookies.remove('token');
          Cookies.remove('svg')
          this.$router.push('/homePageEcommerce');
        } catch (error) {
          console.log(error);
        }
      },
    },
  };
  </script>
<style>

</style>