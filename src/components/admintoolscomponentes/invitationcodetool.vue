<template>
  <div class="max-w-4xl mx-auto grid flex-col items-center containersDash">
    <!-- Campo de descripción y generación de código -->
    <div class="mb-4">
      <label class="block text-gray-700 text-sm font-bold mb-2">Descripción:</label>
      <input v-model="formData.description" type="text" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="Ingrese una descripción" required>
    </div>
    <div class="mb-4">
      <label class="block text-gray-700 text-sm font-bold mb-2">Código generado:</label>
      <input type="text" :value="codigo" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" readonly>
    </div>
    <button @click="createInvitationCode" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="button">Generar</button>
    
    <!-- Tabla con códigos y descripciones generados previamente -->
    <div class="mt-8">
      <h2 class="text-lg font-bold mb-2">Códigos generados</h2>
      <table class="min-w-full bg-white border border-gray-300">
        <thead>
          <tr>
            <th class="px-4 py-2 border-b">Descripción</th>
            <th class="px-4 py-2 border-b">Código</th>
            <th class="px-4 py-2 border-b">Fecha de Generación</th>
            <th class="px-4 py-2 border-b">Usuarios Registrados</th>
            <th class="px-4 py-2 border-b">Creado por</th>
            <th class="px-4 py-2 border-b"></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in items" :key="item.id">
            <td class="px-4 py-2 border-b">{{ item.description }}</td>
            <td class="px-4 py-2 border-b">{{ item.invitationCodes }}</td>
            <td class="px-4 py-2 border-b">{{ item.created_at }}</td>
            <td class="px-4 py-2 border-b">{{ item.countUsers }}</td>
            <td class="px-4 py-2 border-b">{{ item.created_by.name}}</td>
            <td class="px-4 py-2 border-b">
              <button @click="deleteInvitationCode(item.id)" class="text-red-600 font-semibold hover:text-red-800">Eliminar</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style>
.flex {
  display: flex;
}

.items-center {
  align-items: center;
}
</style>

<script>
import axios from 'axios';
import Cookie from 'js-cookie'



export default {
  data() {
    return{
      items: [],
      formData: {
        description: ""
      }
    };
  },
  created() {
    this.getInvitationsCode()
  },
  methods: {
    async getInvitationsCode() {
         await axios.get("http://127.0.0.1:8000/api/users/invitations", {
            headers: {
              Authorization: `Token ${Cookie.get('token')}`,
            },
          }).then(response => {console.log(response.data); this.items = response.data;})
          .catch(error => {console.log(error)});
      },

    async createInvitationCode() {
      await axios.post("http://127.0.0.1:8000/api/users/invitations",{description: this.formData.description} ,{
          headers: {
              Authorization: `Token ${Cookie.get('token')}`,
            },
      }).then(response => {console.log(response.data); this.getInvitationsCode()})
      .catch(error => {console.log(error.response.data)});
      },

    async deleteInvitationCode(Id) {
      await axios.delete(`http://127.0.0.1:8000/api/users/invitations/${Id}`, {
        headers: {
          Authorization: `Token ${Cookie.get('token')}`
        }
      })
      .then(response => {console.log(response.data); this.getInvitationsCode()})
      .catch(error => {console.log(error.response.data)});
    }
    }
} // Agrega el nombre del creador predeterminado aquí
//     };
//   },
//   methods: {
//     generarCodigo() {
//       const caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
//       let codigoGenerado = '';
//       for (let i = 0; i < 16; i++) {
//         codigoGenerado += caracteres.charAt(Math.floor(Math.random() * caracteres.length));
//       }
//       this.codigo = codigoGenerado;
      
//       // Agregar el código, la descripción, la fecha de generación, la cantidad de usuarios registrados y el nombre del creador a la lista de códigos generados
//       this.codigosGenerados.push({
//         descripcion: this.descripcion,
//         codigo: this.codigo,
//         fechaGeneracion: new Date().toLocaleString(), // Obtener la fecha actual
//         usuariosRegistrados: 0, // Inicialmente, no hay usuarios registrados
//         creadoPor: this.creadoPor,
//       });
      
//       // Limpiar el campo de descripción y reiniciar el campo de código
//       this.descripcion = '';
//       this.codigo = '';
//     },
//     eliminarCodigo(index) {
//       this.codigosGenerados.splice(index, 1);
//     },
//   },
// };
</script>
